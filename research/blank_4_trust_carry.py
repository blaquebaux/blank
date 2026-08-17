#!/usr/bin/python3
# =============================================================================
# blank_4_trust_carry.py — BLAQUE BAUX BLANK #4: the pre-deal trust carry, honestly.
#
# The one structurally low-risk SPAC trade: BEFORE a deal, a SPAC is cash in trust
# (~$10/share in T-bills) plus a REDEMPTION RIGHT (a hard floor at trust value) plus
# a free option on the eventual merger. Buy at/below trust, hold to redemption:
#     return ~= T-bill yield  +  discount-to-trust capture  +  option value
# The base (risk-free) leg is boundable with BIL (1-3m T-bill ETF). The EXCESS —
# discount capture + option — needs per-SPAC trust NAV, redemption dates, and the
# FULL (survivorship-complete) pre-deal universe. None of that lives on daily equity
# bars. So we bound what we can and flag the rest honestly. Read-only.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _blank_common import series, stats, TBILL

print("=" * 76, "\nBLANK #4 — the pre-deal trust carry: theory vs. what daily bars can test\n" + "=" * 76)

d, p = series(TBILL)
WIN = "2022-01-03"
k0 = next(i for i, x in enumerate(d) if x >= WIN)
r = p[k0 + 1:] / p[k0:-1] - 1
st = stats(r)
tot = p[-1] / p[k0] - 1
print(f"  base leg — BIL (1-3m T-bill ETF), {d[k0]} .. {d[-1]}:")
print(f"    total return {tot*100:+.1f}%   annualized ~{st['cagr']*100:+.1f}%   vol {st['vol']*100:.1f}%   Sharpe {st['sh']:+.1f}")
print("    ^ this is the near-riskless FLOOR the trust accrues; the carry is at least this.\n")

print("  what the carry adds on top (NOT testable on daily equity bars):")
print("    + discount-to-trust capture : buying at $9.7x vs a $10.1x trust -> a few % pull-to-NAV")
print("    + redemption right          : a hard floor at trust value (downside ~ capped)")
print("    + free option on the deal   : keep the warrant/upside, redeem the share if you dislike it")
print("    - needs: per-SPAC trust NAV, redemption dates, and the survivorship-COMPLETE")
print("             pre-deal universe (most of which delisted or converted) -> a data upgrade.")

print("\nVERDICT: the trust carry is REAL and genuinely low-risk — a T-bill-PLUS instrument with")
print("a redemption floor and a free option — but on this data source it is only boundable, not")
print(f"cleanly measurable: the floor is ~{st['cagr']*100:.0f}%/yr (BIL), the excess is the edge and it")
print("needs SPAC-level trust/redemption data. It is also CAPACITY-CONSTRAINED (small deals, thin")
print("float). Honest status: a promising near-cash carry, PARKED pending a proper SPAC dataset.")
