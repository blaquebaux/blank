#!/usr/bin/python3
# =============================================================================
# blank_1_despac_decay.py — BLAQUE BAUX BLANK #1: the de-SPAC complex vs the market.
#
# SPACs IPO at $10 (cash in trust). After the merger, dilution + warrant overhang +
# redemption-driven float collapse tend to crush the stock: "de-SPAC decay." Measure
# it two ways on the SURVIVING names (the busts that delisted are invisible, so this
# UNDERSTATES the damage): (a) an equal-weight de-SPAC basket vs SPY over a common
# post-mania window, and (b) the cross-sectional outcome — how many broke the $10
# trust floor, and how skewed the distribution is.
# Read-only. Prints its own results.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _blank_common import bars, series, rets_common, stats, DESPAC, BENCH, covering

print("=" * 76, "\nBLANK #1 — de-SPAC decay: the complex vs the market\n" + "=" * 76)
print("(surviving names only — delisted busts are invisible, so this UNDERSTATES the decay)\n")

# ---- (a) equal-weight basket vs SPY over a clean common window (post-mania) ----
WIN = "2022-01-03"                                   # by here essentially all had merged & renamed
have = covering(DESPAC, WIN)
u, dates, R = rets_common(have + [BENCH])
j = {s: u.index(s) for s in u}
k0 = next(i for i, d in enumerate(dates) if d >= WIN)
sl = slice(k0, len(dates))
basket = R[sl][:, [j[s] for s in have]].mean(axis=1)   # equal-weight, daily rebalance
spy = R[sl][:, j[BENCH]]
sb, ss = stats(basket), stats(spy)
print(f"  common window {dates[k0]} .. {dates[-1]}  ({len(basket)} days, {len(have)} names)")
print(f"  {'book':<26}{'Sharpe':>8}{'CAGR':>8}{'vol':>7}{'maxDD':>8}")
print(f"  {'equal-weight de-SPAC':<26}{sb['sh']:>+8.2f}{sb['cagr']*100:>+7.1f}%{sb['vol']*100:>6.1f}%{sb['dd']*100:>+7.0f}%")
print(f"  {'SPY':<26}{ss['sh']:>+8.2f}{ss['cagr']*100:>+7.1f}%{ss['vol']*100:>6.1f}%{ss['dd']*100:>+7.0f}%")
print(f"  --> de-SPAC basket CAGR gap vs SPY: {(sb['cagr']-ss['cagr'])*100:+.1f}pp/yr\n")

# ---- (b) cross-sectional outcome: who broke the $10 trust floor? ----
print("  cross-section (current price vs the $10 SPAC IPO/trust price):")
outs = []
for s in DESPAC:
    d, p = series(s)
    if len(d) < 60: continue
    outs.append((s, p[-1]))
below = [s for s, px in outs if px < 10]
print(f"    {len(below)}/{len(outs)} de-SPACs trade BELOW $10 — value destroyed vs the trust ({100*len(below)/len(outs):.0f}%)")
outs.sort(key=lambda x: x[1])
worst = ", ".join(f"{s} ${px:.2f}" for s, px in outs[:4])
best = ", ".join(f"{s} ${px:.2f}" for s, px in outs[-4:][::-1])
print(f"    worst: {worst}")
print(f"    best:  {best}")
print("\nVERDICT: the MEDIAN de-SPAC is a wreck (most broke the $10 floor) — a structurally")
print("bad complex, and worse than shown because the true busts delisted. But the surviving")
print("distribution is violently RIGHT-SKEWED by a few real winners, which #2 shows is exactly")
print("what makes the 'obvious short' dangerous.")
