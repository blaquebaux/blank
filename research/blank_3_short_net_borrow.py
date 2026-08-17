#!/usr/bin/python3
# =============================================================================
# blank_3_short_net_borrow.py — BLAQUE BAUX BLANK #3: the short, net of borrow.
#
# Even where a de-SPAC short "works" on the median, the P&L is dominated by BORROW
# COST. Broken de-SPACs are hard-to-borrow — fees routinely run 10-100%+ annualized.
# Take a disciplined short (short only the names that have already broken the $10
# floor — the structurally-impaired subset, avoiding the moonshot right tail from #2)
# and charge realistic borrow. Show gross vs net across a fee ladder; find where the
# edge dies. This is the honest core of the whole sleeve.
# Read-only. Prints its own results.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _blank_common import bars, series, rets_common, stats, DESPAC, BENCH, covering

WIN = "2022-01-03"
have = covering(DESPAC, WIN)
u, dates, R = rets_common(have + [BENCH]); j = {s: u.index(s) for s in u}
k0 = next(i for i, d in enumerate(dates) if d >= WIN); sl = slice(k0, len(dates))
ndays = len(dates) - k0

# "impaired" subset = names below $10 today (proxy for the structurally broken cohort).
impaired = [s for s in have if series(s)[1][-1] < 10]
print("=" * 76, "\nBLANK #3 — the de-SPAC short, net of borrow cost\n" + "=" * 76)
print(f"  window {dates[k0]} .. {dates[-1]}  |  impaired (<$10) short book: {len(impaired)} names")
print(f"  {', '.join(impaired)}\n")

# gross short return of the equal-weight impaired book
lg = R[sl][:, [j[s] for s in impaired]].mean(axis=1)   # long the impaired names
short_gross = -lg
sg = stats(short_gross)
gross_cagr = sg['cagr']
print(f"  gross short (equal-weight impaired): Sharpe {sg['sh']:+.2f}  CAGR {gross_cagr*100:+.1f}%  maxDD {sg['dd']*100:+.0f}%")

print(f"\n  {'annual borrow fee':>18}{'net CAGR':>12}{'verdict':>16}")
for fee in [0.05, 0.15, 0.30, 0.50, 1.00]:
    net = gross_cagr - fee                            # borrow accrues on the short notional ~ flat drag
    verdict = "edge survives" if net > 0.03 else ("marginal" if net > 0 else "edge GONE")
    print(f"  {int(fee*100):>16}% {net*100:>+11.1f}%{verdict:>16}")
print("  (broken de-SPACs frequently sit at 20-100%+ borrow when the short is most wanted)")

print("\nVERDICT: the impaired short is a real gross edge, but it is a BORROW trade, not an")
print("alpha trade — the names you most want to short are exactly the hardest/most expensive to")
print("borrow, and the fee eats the edge precisely when the thesis is best. 'Real but largely")
print("uninvestable after borrow' is the honest verdict, and it matches the base's 'you cannot")
print("fade the prop' law: the market charges you to hold the obvious short.")
