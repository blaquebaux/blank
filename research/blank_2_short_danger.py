#!/usr/bin/python3
# =============================================================================
# blank_2_short_danger.py — BLAQUE BAUX BLANK #2: why the obvious short is dangerous.
#
# "de-SPACs go to zero, so short the basket" is the naive trade. The problem: the
# surviving distribution is hugely right-skewed — a handful of winners (ASTS, RKLB,
# IONQ, MP) run the short over. A short has UNBOUNDED loss on exactly the fat right
# tail this complex produces. Quantify: the dispersion, and the drawdown of a naive
# short-the-basket book (before borrow — #3 adds that).
# Read-only. Prints its own results.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _blank_common import bars, rets_common, stats, DESPAC, BENCH, covering

WIN = "2022-01-03"
have = covering(DESPAC, WIN)
u, dates, R = rets_common(have + [BENCH]); j = {s: u.index(s) for s in u}
k0 = next(i for i, d in enumerate(dates) if d >= WIN); sl = slice(k0, len(dates))

print("=" * 76, "\nBLANK #2 — the dispersion trap: why shorting the complex is dangerous\n" + "=" * 76)
print(f"  window {dates[k0]} .. {dates[-1]}  ({len(have)} names)\n")

# per-name total return over the window — the dispersion
tot = {s: np.prod(1 + R[sl][:, j[s]]) - 1 for s in have}
srt = sorted(tot.items(), key=lambda x: x[1])
med = np.median(list(tot.values()))
print(f"  per-name total return: median {med*100:+.0f}%   "
      f"worst {srt[0][1]*100:+.0f}% ({srt[0][0]})   best {srt[-1][1]*100:+.0f}% ({srt[-1][0]})")
print(f"  winners (>0): {sum(1 for _,v in tot.items() if v>0)}/{len(have)}   "
      f"names that MORE THAN DOUBLED: {sum(1 for _,v in tot.items() if v>1.0)}")
print("  the right tail (short-killers):")
for s, v in srt[-3:][::-1]:
    print(f"    {s:<6} {v*100:+.0f}%  <- a short here loses {v*100:.0f}% of notional")

# naive short-the-equal-weight-basket: return = -basket; its drawdown is the danger
basket = R[sl][:, [j[s] for s in have]].mean(axis=1)
short = -basket
sB, sS = stats(basket), stats(short)
print(f"\n  {'book':<28}{'Sharpe':>8}{'CAGR':>8}{'maxDD':>8}")
print(f"  {'long equal-weight basket':<28}{sB['sh']:>+8.2f}{sB['cagr']*100:>+7.1f}%{sB['dd']*100:>+7.0f}%")
print(f"  {'NAIVE SHORT the basket':<28}{sS['sh']:>+8.2f}{sS['cagr']*100:>+7.1f}%{sS['dd']*100:>+7.0f}%")
print("  (short return is BEFORE borrow cost — #3 charges it)")

print("\nVERDICT: the median de-SPAC craters, but the basket is NOT a clean short — a few")
print("moonshots create a fat right tail, and a short's loss on that tail is unbounded. The")
print("tradeable statement is 'the MEDIAN is a short', not 'the basket is'. Any real short must")
print("be single-name, catalyst-timed, and capped — which runs straight into borrow cost (#3).")
