# Blaque Baux Blank — research

First-pass Path-A research on SPACs / blank-check companies. All sketches read Alpaca SIP daily
bars, are read-only, and print their own results. 2022-01 – 2026-08.

> **Survivorship caveat, stated up front.** The worst SPAC busts **delisted** (NKLA, RIDE, FSR,
> GOEV-adjacent, PTRA, …) and cannot be pulled from a daily-bars vendor. Every surviving-name result
> here therefore **understates** the true de-SPAC decay — the graveyard is invisible. That makes the
> "de-SPAC is a bad complex" finding conservative, and it is one reason the pre-deal carry (which
> needs the *full* universe + trust values + redemption dates) is only partially testable here.

```bash
export $(grep -v '^#' ~/.config/blaquebaux/alpaca.env | xargs)   # or source it
python research/blank_1_despac_decay.py     # the complex vs the market
python research/blank_2_short_danger.py     # why the obvious short is dangerous  (flagship)
python research/blank_3_short_net_borrow.py # the disciplined short, net of borrow
python research/blank_4_trust_carry.py      # the pre-deal trust carry — theory vs. testable
```

## Scorecard

| # | Question | Result | Verdict |
|---|----------|--------|---------|
| 1 | Is the de-SPAC complex structurally bad? | equal-weight basket **+3.3%** CAGR vs SPY +11.9% (−8.7pp/yr), **52% vol, −62% DD**; **60% trade below the $10 trust price** | ✅ confirmed — a bad complex (and understated) |
| 2 | Can you just short the basket? | naive short **−26%/yr, −89% DD**; median name −43% but **ASTS +643%, RKLB +429%, HIMS +324%** run the short over | ❌ **flagship null** — the right tail kills the short |
| 3 | Does shorting only the *broken* (<$10) subset work? | gross short **−7.6%/yr, −74% DD** (dead-cat/OPEN-style squeezes); at 5–50% borrow: **−13% → −58%/yr** | ❌ null — a borrow trade, not alpha; the fee buries it |
| 4 | The pre-deal trust carry? | base (T-bill) leg boundable at **~3.9%/yr** (BIL); the excess (discount capture + option) needs per-SPAC trust/redemption data | ⏸️ **parked** — real near-cash carry, not testable on daily bars |

## The synthesis

**Blank is a risk map, not a tradeable short — a diagnostic, not a strategy.** The thesis is
*confirmed*: the de-SPAC complex is genuinely bad, underperforming the market by ~9pp/yr on the
surviving names alone (worse in truth, since the busts delisted) with 60% of names having broken the
$10 trust floor. And yet **every route to monetize that is closed:**

1. **You cannot short the basket.** Over 2022–2026 the naive short *loses 26%/yr with an 89%
   drawdown*. The median de-SPAC craters, but the surviving distribution is violently right-skewed —
   ASTS (+643%), RKLB (+429%), HIMS (+324%) — and a short's loss on that fat tail is unbounded. The
   tradeable statement is "the **median** is a short," never "the **basket** is."
2. **You cannot even short the broken subset cleanly.** Restricting to the sub-$10 impaired names, the
   short still *loses gross* — violent dead-cat and meme squeezes (OPEN's 2025 rip is the archetype) —
   and realistic borrow (broken de-SPACs routinely cost 20–100%+ to borrow, exactly when you most want
   them) turns a small gross bleed into a −13%-to-−58%/yr disaster. This is the base's **"you cannot
   fade the prop"** law in its purest form: the market charges you to hold the obvious short.
3. **The one structurally sound trade — the pre-deal trust carry — is out of reach of this data.** A
   pre-deal SPAC is T-bills in trust + a redemption floor + a free option: a genuine near-cash
   carry. But its excess-over-T-bills edge needs per-SPAC trust NAV, redemption dates, and the
   survivorship-complete universe — none of which live on daily equity bars. Floor ~3.9%/yr (BIL);
   the rest is parked pending a proper SPAC dataset, and it is capacity-constrained regardless.

So Blank joins [Bubble](https://github.com/blaquebaux/bubble) and
[Brute-Force](https://github.com/blaquebaux/brute-force) on the honest shelf: **a real market
pathology that resists being traded.** The value is the risk lesson — *don't be long the de-SPAC
right tail thinking you own value, and don't be short it thinking gravity is free* — not a sleeve.

## Status
**Research: first pass complete — a diagnostic null** (`research/`). The de-SPAC decay is real but
untradeable (short run over by the tail, then buried by borrow); the sound trust carry needs data
beyond daily bars and is parked. No keeper, no live driver; nothing validated to the spine's bar.
