# Blaque Baux Blank

**SPACs — blank-check shells, mined for carry, shorts, and long/short busts.**

Blank is a member of the Blaque Baux family. The [core repo](https://github.com/blaquebaux/base)
is the **engine and blueprint** — a governed, systematic platform (Julia) with a venue-agnostic
execution controller and a Layer-3 live-money safety gate. Blank points that engine in its own
direction and inherits the governance wholesale.

> **Not investment advice.** Educational/research software. Nothing here is validated. See [LICENSE](LICENSE).

```bash
git clone --recursive https://github.com/blaquebaux/blank.git
julia --project=engine -e 'using Pkg; Pkg.instantiate()'   # one-time engine setup
```

## The thesis

A SPAC is a **blank-check company** — a listed shell that raises cash into a trust, then hunts for a
private company to merge with (the "deSPAC"). The structure is riddled with asymmetries: sponsors get
a cheap ~20% promote, investors get a redemption right plus warrants, and the post-merger entity
often arrives **over-promised and debt-inflated**, facing a redemption cliff, heavy dilution, and
lockup expiries. Many bust. That mix of a **protected pre-deal instrument** and a **structurally
fragile post-deal one** is exactly the kind of terrain a long/short book can work.

Blank studies three distinct trades, not one. **(1) Trust carry** — pre-deal SPACs often trade at or
below the cash in trust; buying near/below trust NAV and holding to redemption is a low-risk,
bond-like carry with an option on the deal. **(2) The deSPAC short** — after the merger, dilution,
warrant overhang, and lockup expiry are identifiable, dated catalysts for decline. **(3) Long/short
around bust signals** — pairing survivors against the shells that are visibly running out of runway.
The sleeve is honest that this is a **crowded, borrow-constrained** corner: the short leg lives or
dies on locate cost and timing, and the base's "you cannot fade the prop" caution applies.

## Research plan (Path A — not yet built)

- **Trust-NAV carry.** Measure the pre-deal discount-to-trust across the SPAC universe and test the
  buy-below-trust, hold-to-redemption carry — return, risk, and capacity, net of the tiny edges.
- **The deSPAC decay curve.** Characterize post-merger returns around the dated catalysts (lockup
  expiry, warrant overhang, redemption-driven float collapse). Is the decline systematic and
  short-able, or already priced?
- **Bust signals, long/short.** Build a runway/dilution/deterioration score and test a market-neutral
  long-survivors / short-shells book — net of **borrow cost**, which likely dominates the P&L here.
- **Crowding and capacity honesty.** This trade is well known; stress it for locate availability,
  squeeze risk, and how quickly the edge decays. A "real but uninvestable after borrow" verdict is a
  valid, valuable outcome.

Nothing above is implemented or validated. This is the map, not the territory.

## Status
**Concept.** Thesis and research plan only — no sketches run, no driver, nothing validated to the
spine's bar. A structural long/short idea whose honest test is dominated by borrow cost and crowding.

## About Blaque Baux

**Blaque Baux** is a quantitative research initiative and a subsidiary of **[Carter Warrens](https://carterwarrens.com)**.
[**BlaqueBaux.com**](https://blaquebaux.com) is the home for the work; the code lives here on GitHub — open to
study, test, and build bespoke strategies on top of.

Anyone can point an AI at a market. The edge is **understanding what the data actually says — and turning it
into something you can act on.** We test relentlessly and put most of it *on the record as rejected, with the
reason*; what survives is built, governed, and validated before it is ever called real. That combination —
honest research, reproducible evidence, and execution you can trust — is why Carter Warrens leads on
**strategy and implementation**, not merely uses the tools everyone now has.

## The Blaque Baux family
This repo is one sleeve of the **Blaque Baux** family — a single governed engine steered in
many directions. The [core repo](https://github.com/blaquebaux/base) is the
base/blueprint and holds the [full family roster](https://github.com/blaquebaux/base#the-blaquebaux-family).

## Layout
```
engine/     the Blaque Baux platform (git submodule -> blaquebaux/base)
research/   the research plan (Path A) — sketches land here once run
live/       governed live drivers (once a sleeve graduates to paper A/B)
```

## License
[MIT](LICENSE). (c) 2026 Carter Warrens.
