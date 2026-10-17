"""
Privacy: website keyword ko encrypt kar ke bhejti hai, taake public repo mein
kisi ko searches nazar na aayein (run inputs, logs, artifacts sab mein).

Key = SHA-256(CALLBACK_SECRET)   Cipher = AES-256-GCM
Format = base64( iv[12] | tag[16] | ciphertext )   (PHP openssl ke mutabiq)
"""
import base64
import hashlib
import json
import os
import sys

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def _key():
    s = os.environ.get("CALLBACK_SECRET", "")
    if not s:
        sys.exit("CALLBACK_SECRET set nahi hai.")
    return hashlib.sha256(s.encode()).digest()


def encrypt(obj) -> str:
    iv = os.urandom(12)
    ct = AESGCM(_key()).encrypt(iv, json.dumps(obj, ensure_ascii=False).encode(), None)
    return base64.b64encode(iv + ct[-16:] + ct[:-16]).decode()


def decrypt(token: str):
    raw = base64.b64decode(token)
    iv, tag, ct = raw[:12], raw[12:28], raw[28:]
    return json.loads(AESGCM(_key()).decrypt(iv, ct + tag, None))


def mask(*values):
    """GitHub Actions logs mein in values ko *** bana deta hai."""
    if os.environ.get("GITHUB_ACTIONS") != "true":
        return
    for v in values:
        for part in {str(v), *str(v).split()}:
            if len(part) >= 3:
                print(f"::add-mask::{part}", flush=True)
