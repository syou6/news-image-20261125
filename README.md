# The World in One Page — Wednesday 25 November 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/syou6/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/syou6/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A one-image newspaper front page summing up the world's news of
**Wednesday 25 November 2026**: 51 stories across 9 regions, drawn as a
1024×1024 PNG by `build_image.py` (Python 3 + Pillow). `main.py`
(Python 3.13, standard library only, no network) validates the bundled
`entry.png` — PNG signature, at most 1 MiB, at most 1024×1024 — and
writes it byte-identically to `/output/entry.png` (or to
`MAKEFUN_OUTPUT_DIR` when set). See `NOTES.md` for the research log
behind every item, with sources. Every story happened, or was first
reported, on 25 November 2026; continuing stories appear only with
their new 25 November development, and nothing is recycled from the
24 November front page.

## The lead story

- **Twin quakes shake Venezuela** — Two earthquakes, magnitudes 7.2
  and 7.5, struck Venezuela within seconds on Wednesday, causing
  widespread damage in Caracas and the northern coast. The toll was
  rising as rescuers dug through rubble; interim President Delcy
  Rodriguez declared a state of emergency. The drawn visual — a
  cracked Caracas skyline, a red seismograph trace and a big "M7.5"
  badge — names the event at a glance.

## Secondary stories

- **Shenzhou-24 blasts off** — China launched Shenzhou-24 with the
  first Pakistani astronaut aboard, the first foreign visitor to the
  Tiangong space station (Xinhua, The Japan Times, 25 Nov).
- **Nvidia rout deepens** — the Nasdaq 100 fell 2% as Nvidia dropped
  5.9% and chip stocks sank 7.9%; the Dow regained 50,000 and the
  VIX neared 26, with new US tariff plans weighing (Moneycontrol,
  ATFX, 25 Nov).
- **Putin vows retaliation** — Putin said Ukraine keeps hitting
  Russian refineries despite Trump's plea and promised an
  "inevitable" reply; Medvedev warned of a preventive nuclear
  strike (Reuters, 25 Nov).
- **Hormuz shipping hit** — Iran claimed tankers hit mines in the
  Strait of Hormuz; the Saudi-led coalition struck Hodeidah as the
  Houthis threatened Saudi ports (Arab News, Qatar Tribune, 25 Nov).

## In brief on the page (46 more)

- **Europe:** Ukraine says its Libya ship attack was self-defence ·
  Zelensky confirms the Finland ship hit, Norway urges caution ·
  Norway pledges $7bn to Ukraine in 2027 · Russia's budget: defence
  up 27% · Moscow summons Latvia's envoy · Magyar meets Zelensky
  for the first formal talks · UK warns of a Russian sabotage
  threat.
- **Middle East:** Houthis hit Riyadh's tallest tower again, 11 hurt
  · US warns Americans of the Houthi threat · Houthis 60 km from
  Aden, city holds · Iraq PM moves on Kurdish oilfields · Eisenkot
  clinches a first coalition pact.
- **Asia-Pacific:** Xi probes Shanghai boss Chen Jining ·
  Australia–Solomon Islands pact stymies China · US slams Australia's
  social media law · Seoul: Russian jets in the defence zone · Seoul
  subway strike called off · Taiwan local vote tests Lai · Australia
  inflation jumps to 4.9% · Rakuten breach leaks client data.
- **South Asia:** Huawei guilty on 10 of 12 US counts · landmine toll
  hits a five-year high of 7,000 · Myanmar rebel vows to fight on ·
  Bangladesh student leaders hit out at India.
- **Africa:** 50 feared dead in a Nigeria boat capsize · 37 killed in
  Borno airstrikes · ten killed in an Egypt road crash · Libya wants
  Zelensky on a terror list.
- **Americas:** Trump gives Giuliani the Medal of Freedom · Trump
  pardons turkeys Freedom and Feathers · WHO: lift the US fuel
  blockade on Cuba · Fort Hood gunman seeks a stay of execution ·
  US soldier admits selling secrets to China · six missing after a
  Mississippi plane crash · gunmen hold 25 hostage in Colombia ·
  car bomb wounds 20+ in Colombia · floods threaten California.
- **Economy & tech:** US to unveil new tariffs after a capacity probe
  · Shein pays $100m to settle a US case · Sanofi to buy Insmed for
  $41bn · Sensex jumps 1,500, Nifty tops 25,750.
- **Culture & sport:** chess Game 1 — Gukesh holds Sindarov to a draw
  · Real Madrid hit PSV 5-1 in Europe · NPB stars Sato and Taira
  agree MLB deals · Norway shuts out Russian skaters · Thomas Markle
  indicted in a US court.

A UTC timeline strip at the foot of the page walks the day around the
clock: Beijing → Seoul → Sydney → Caracas → Baghdad → London →
Geneva → New York → Washington.

## Files

- `entry.png` — the finished front page (1024×1024, under 1 MiB).
- `build_image.py` — the Pillow drawing script that produced it.
- `main.py` — the entry program: validates and copies `entry.png`.
- `NOTES.md` — the 25 November 2026 research log (headline, summary,
  region, source and date for every story).
- `LICENSE` — MIT.
