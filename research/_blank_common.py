#!/usr/bin/python3
# =============================================================================
# _blank_common.py — shared helpers for the Blaque Baux Blank (SPAC) sketches.
# Alpaca SIP daily bars; reads ALPACA_KEY_ID / ALPACA_SECRET_KEY from env. Read-only.
#
# HONEST DATA CAVEAT, stated once, up front: the worst SPAC busts DELISTED
# (NKLA, RIDE, FSR, GOEV, PTRA, MULN-adjacent, ...) and are NOT retrievable from a
# daily-bars vendor. Every surviving-name result here therefore UNDERSTATES the true
# deSPAC decay — the graveyard is invisible. The short thesis is thus conservative;
# the carry/floor thesis (which relies on the FULL pre-deal universe + trust values +
# redemption dates) is only partially testable on equity bars, and we say so.
# =============================================================================
import os, json, urllib.request, math
import numpy as np

H = {"APCA-API-KEY-ID": os.environ["ALPACA_KEY_ID"], "APCA-API-SECRET-KEY": os.environ["ALPACA_SECRET_KEY"]}
START, END = "2019-01-01", "2026-08-01"
_cache = {}

# A curated basket of well-known de-SPACs (companies that went public via SPAC merger)
# that STILL TRADE — hence survivorship-biased UPWARD. Grouped only for readability.
DESPAC = [
    # EV / mobility (the epicentre of the bust)
    "LCID", "CHPT", "GOEV", "PSNY", "STEM", "EVGO", "HYLN",
    # consumer / platform
    "OPEN", "SOFI", "DKNG", "CLOV", "RUM", "BODY", "GRAB", "HIMS",
    # space / deep tech
    "SPCE", "RKLB", "IONQ", "MP", "ASTS",
]
BENCH = "SPY"
TBILL = "BIL"    # 1-3m T-bill ETF — proxy for the trust-accrual (risk-free) leg of SPAC carry

RECENT = "2026-06-01"   # a name must still trade near the end to enter the basket

def covering(names, win):
    """Names that span [win .. RECENT] — avoids one delisted/renamed ticker (e.g. BODY 2024)
    truncating the whole common window. Dropping delisted busts makes the basket look BETTER
    than reality, so it is conservative for the short thesis; noted honestly in the READMEs."""
    return [s for s in names if len(bars(s)) > 60 and min(bars(s)) <= win and max(bars(s)) >= RECENT]

def bars(s):
    if s in _cache: return _cache[s]
    u = (f"https://data.alpaca.markets/v2/stocks/bars?symbols={s}&timeframe=1Day"
         f"&start={START}&end={END}&adjustment=all&feed=sip&limit=10000")
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=40))
        _cache[s] = {b["t"][:10]: b for b in d.get("bars", {}).get(s, [])}
    except Exception:
        _cache[s] = {}
    return _cache[s]

def series(s):
    b = bars(s); dates = sorted(b)
    return dates, np.array([b[d]["c"] for d in dates], float)

def rets_common(syms):
    D = {s: bars(s) for s in syms}; D = {s: v for s, v in D.items() if len(v) > 60}
    u = list(D); dates = sorted(set.intersection(*[set(D[s]) for s in u]))
    M = np.array([[D[s][d]["c"] for s in u] for d in dates], float)
    return u, dates[1:], M[1:] / M[:-1] - 1

def stats(r):
    r = np.asarray(r, float); r = r[np.isfinite(r)]
    if len(r) < 30 or r.std() == 0: return dict(sh=float('nan'), cagr=float('nan'), dd=float('nan'), vol=float('nan'))
    cum = np.cumprod(1 + r)
    return dict(sh=r.mean() / r.std() * math.sqrt(252), cagr=cum[-1] ** (252 / len(r)) - 1,
                dd=(cum / np.maximum.accumulate(cum) - 1).min(), vol=r.std() * math.sqrt(252))
