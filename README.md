# LinkFinder – GitHub Backend

English keyword → Google ki **133 languages** mein translate → har mulk ke search results (page 1, 2, 3...) → **duplicates hata kar** → har website ka **traffic** → website / Excel.

## Kaise kaam karta hai

```
Website ──► plan  (languages ko 5 servers mein baantna)
            │
            ├─► search server 1 ┐
            ├─► search server 2 │  sab ek saath
            ├─► ...             │
            └─► search server 5 ┘
                    │
                 merge  (jorna → duplicate hatana → traffic) ──► Website
```

Sab 133 languages par ~5–10 minute lagte hain. GitHub free plan ek waqt mein 20 servers deta hai, is liye 4 searches ek saath chalti hain; baqi line mein intezar karti hain.

## Privacy (public repo)
- Website keyword aur languages ko **AES-256 se encrypt** kar ke bhejti hai (key = `CALLBACK_SECRET`).
- Run ka naam sirf `job <id>` hota hai; logs mein keyword aur translations `***` dikhte hain.
- Beech ki files (artifacts) bhi encrypted hain aur 1 din baad delete.
- Aakhri result seedha website ko jata hai, GitHub par save nahi hota.

## Har result mein kya hai

| Field | Matlab |
|---|---|
| language | Kis language mein mila |
| translated_keyword | Us language mein translate hua keyword |
| google_domain | Us mulk ka Google (google.de, google.co.jp...) |
| page / position | Kis page aur kis number par (ranking) |
| title / url / domain | Website |
| traffic | Monthly visits (e.g. `~4.5M`) |
| tranco_rank | Dunya mein rank (top 10 lakh mein) |
| traffic_source | `Estimate (Tranco rank)` ya `Similarweb` |
| found_in_languages / also_in | Ye link aur kin languages mein bhi aaya (duplicate hata kar) |

## Duplicates
`http`/`https`, `www`, aakhri `/`, aur tracking (`utm_…`, `gclid`, `fbclid`) ko hata kar ek hi link gina jata hai. Jo sab se upar rank par mila woh rehta hai, baqi languages `also_in` mein.

## Traffic
- **Free (default):** [Tranco](https://tranco-list.eu) list se rank, aur rank se **andaza** monthly visits. Ye estimate hai, asli number nahi. Top 10 lakh se bahar ki sites "Low / unknown".
- **Asli traffic (paid, optional):** Similarweb API key ho to Secret `SIMILARWEB_API_KEY` mein daalein.

## Secrets (Repo → Settings → Secrets and variables → Actions)
| Secret | Zaroori? | Kaam |
|---|---|---|
| `CALLBACK_SECRET` | Haan | Website ke saath same password |
| `SERPER_API_KEY` | Nahi | Asli Google results (serper.dev) |
| `SIMILARWEB_API_KEY` | Nahi | Asli traffic |

## Engines
- **free:** koi key nahi. Bing/DuckDuckGo jaise engines se us mulk ke results. Kabhi kabhi kuch languages mein kam results aate hain.
- **serper:** `SERPER_API_KEY` ho to khud use hota hai. Asli Google, har mulk ka domain aur language. Har language × har page = 1 credit.

## Apne computer par
```
pip install -r requirements.txt
python search_tool.py run -k "free games" -l de fr ja -p 2
python search_tool.py run -k "free games" -l all -p 1 -w 4
```

## Language codes (133)
`python -c "from languages import LANGUAGES as L; print(' '.join(L))"`
