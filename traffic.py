"""
Website traffic.

1) Tranco (free, default): dunya ki top 10 lakh websites ki research ranking (tranco-list.eu).
   Rank se monthly visits ka ROUGH andaza nikalta hai (estimate, asli number nahi).
2) Similarweb (paid, optional): SIMILARWEB_API_KEY set ho to asli monthly visits.
"""
import csv
import io
import os
import zipfile
from datetime import date, timedelta

import requests

TRANCO_URL = "https://tranco-list.eu/top-1m.csv.zip"
CACHE = os.environ.get("TRANCO_CACHE", "tranco.csv")


def load_tranco():
    """{domain: rank}. File cache use karta hai (GitHub Actions cache)."""
    if not os.path.exists(CACHE):
        try:
            r = requests.get(TRANCO_URL, timeout=120)
            r.raise_for_status()
            with zipfile.ZipFile(io.BytesIO(r.content)) as z:
                name = z.namelist()[0]
                with open(CACHE, "wb") as f:
                    f.write(z.read(name))
        except Exception as e:
            print(f"! Tranco download fail: {e}")
            return {}
    ranks = {}
    with open(CACHE, newline="", encoding="utf-8") as f:
        for row in csv.reader(f):
            if len(row) >= 2:
                ranks[row[1].strip().lower()] = int(row[0])
    print(f"Tranco: {len(ranks):,} domains loaded")
    return ranks


def lookup_rank(domain, ranks):
    """sub.example.co.uk -> example.co.uk ka rank (agar list mein ho)."""
    parts = domain.lower().split(".")
    for i in range(len(parts) - 1):
        cand = ".".join(parts[i:])
        if cand in ranks:
            return ranks[cand], cand
    return None, None


def estimate_visits(rank):
    """Rough power-law andaza (rank 1 ≈ 90B/month). Sirf idea ke liye."""
    if not rank:
        return None
    return int(9e10 / (rank ** 1.0))


def fmt(n):
    if n is None:
        return ""
    for div, s in ((1e9, "B"), (1e6, "M"), (1e3, "K")):
        if n >= div:
            v = n / div
            return f"{v:.1f}{s}".replace(".0", "")
    return str(int(n))


def tier(rank):
    if not rank:
        return "Not in top 1M"
    for lim in (100, 1_000, 10_000, 100_000, 1_000_000):
        if rank <= lim:
            return f"Top {fmt(lim)}"
    return "Not in top 1M"


def similarweb_visits(domain, key):
    """Similarweb official API: pichle mahine ke total visits."""
    end = date.today().replace(day=1) - timedelta(days=1)
    start = end.replace(day=1)
    url = (f"https://api.similarweb.com/v1/website/{domain}/total-traffic-and-engagement/visits"
           f"?api_key={key}&start_date={start:%Y-%m}&end_date={end:%Y-%m}"
           f"&country=world&granularity=monthly&main_domain_only=false&format=json")
    try:
        r = requests.get(url, timeout=30)
        if r.ok:
            v = r.json().get("visits") or []
            if v:
                return int(v[-1].get("visits") or 0)
    except Exception as e:
        print(f"  ! similarweb {domain}: {e}")
    return None


def add_traffic(rows):
    """Har row mein traffic fields daalta hai. Domain-level cache."""
    ranks = load_tranco()
    sw_key = os.environ.get("SIMILARWEB_API_KEY", "")
    cache = {}
    for r in rows:
        d = r["domain"]
        if d not in cache:
            rank, _ = lookup_rank(d, ranks)
            info = {"tranco_rank": rank, "traffic_tier": tier(rank)}
            visits = similarweb_visits(d, sw_key) if sw_key else None
            if visits is not None:
                info.update(monthly_visits=visits, traffic=fmt(visits), traffic_source="Similarweb")
            else:
                est = estimate_visits(rank)
                info.update(monthly_visits=est,
                            traffic=f"~{fmt(est)}" if est else "Low / unknown",
                            traffic_source="Estimate (Tranco rank)")
            cache[d] = info
        r.update(cache[d])
    return rows
