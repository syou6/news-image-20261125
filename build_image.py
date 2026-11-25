#!/usr/bin/env python3
"""Draw entry.png: a one-page newspaper for Wednesday 25 November 2026.

1024x1024, Pillow only. Layout, top to bottom:
  masthead (date huge) / lead block with quake visual /
  four secondary cards / three brief columns / timeline strip.
Palette: paper cream, ink navy, red accent, teal accent, gold accent.
Lead visual names the event at a glance: cracked Caracas skyline,
a seismograph trace, and a big "M7.5" magnitude badge.
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (250, 246, 236)
INK = (18, 24, 38)
RED = (178, 34, 44)
TEAL = (0, 105, 110)
GOLD = (196, 138, 20)
GREY = (92, 96, 104)
CARD = (255, 253, 247)
DARK = (16, 28, 52)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def F(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if draw.textlength(t, font=font) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, xy, text, font, fill, max_w, leading):
    x, y = xy
    for line in wrap(draw, text, font, max_w):
        draw.text((x, y), line, font=font, fill=fill)
        y += leading
    return y


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------- masthead ----------
d.rectangle([0, 0, W, 156], fill=DARK)
d.text((28, 10), "THE WORLD IN ONE PAGE", font=F(SERIF_B, 38), fill=(255, 255, 255))
d.text((28, 56), "25 NOVEMBER 2026", font=F(SANS_B, 58), fill=(255, 205, 80))
d.text((30, 130), "WEDNESDAY  ·  51 STORIES  ·  9 REGIONS  ·  ALL REPORTED TODAY",
       font=F(SANS_B, 16), fill=(210, 220, 235))
d.rectangle([884, 16, 996, 140], outline=(255, 205, 80), width=3)
d.text((900, 30), "ONE", font=F(SANS_B, 26), fill=(255, 255, 255))
d.text((900, 60), "DAY", font=F(SANS_B, 26), fill=(255, 255, 255))
d.text((900, 92), "ONE PAGE", font=F(SANS_B, 15), fill=(255, 205, 80))

# ---------- lead block ----------
LY = 170
d.rectangle([24, LY, 1000, 408], fill=CARD, outline=INK, width=3)
d.rectangle([24, LY, 1000, LY + 30], fill=RED)
d.text((40, LY + 6), "LEAD  ·  DISASTER  ·  LATIN AMERICA", font=F(SANS_B, 17), fill=(255, 255, 255))
d.text((40, LY + 40), "TWIN QUAKES", font=F(SERIF_B, 38), fill=INK)
d.text((40, LY + 82), "SHAKE VENEZUELA", font=F(SERIF_B, 38), fill=INK)
d.text((40, LY + 124), "CARACAS IN RUINS", font=F(SERIF_B, 38), fill=RED)
text_block(d, (40, LY + 168),
           "Two earthquakes, M7.2 and M7.5, strike within seconds. "
           "Toll rising; emergency declared as rescuers dig through rubble.",
           F(SANS, 17), INK, 540, 22)

# lead visual: cracked Caracas skyline, seismograph trace, M7.5 badge
vx, vy = 800, 310
# ground line, cracked
d.line([vx - 150, vy + 78, vx + 150, vy + 78], fill=INK, width=4)
d.line([vx - 20, vy + 78, vx - 4, vy + 96], fill=INK, width=3)
d.line([vx + 60, vy + 78, vx + 78, vy + 96], fill=INK, width=3)
# buildings, tilted and cracked
d.polygon([(vx - 140, vy + 78), (vx - 140, vy - 30), (vx - 96, vy - 30),
           (vx - 96, vy + 78)], fill=(70, 90, 130))
d.polygon([(vx - 88, vy + 78), (vx - 88, vy - 62), (vx - 40, vy - 62),
           (vx - 40, vy + 78)], fill=(38, 92, 160))
d.polygon([(vx - 32, vy + 78), (vx - 32, vy - 44), (vx + 22, vy - 44),
           (vx + 22, vy + 78)], fill=(90, 110, 150))
d.polygon([(vx + 30, vy + 78), (vx + 30, vy - 18), (vx + 78, vy - 18),
           (vx + 78, vy + 78)], fill=(38, 92, 160))
# leaning tower (right, tilted)
d.polygon([(vx + 86, vy + 78), (vx + 96, vy - 70), (vx + 132, vy - 58),
           (vx + 122, vy + 78)], fill=(70, 90, 130))
# cracks on the buildings
d.line([vx - 64, vy - 62, vx - 56, vy - 20, vx - 70, vy + 10], fill=RED, width=3)
d.line([vx - 8, vy - 44, vx + 2, vy - 6, vx - 6, vy + 30], fill=RED, width=3)
d.line([vx + 104, vy - 60, vx + 110, vy - 10, vx + 100, vy + 40], fill=RED, width=3)
# windows
for bx in (vx - 128, vx - 76, vx - 20, vx + 42):
    for wy in range(vy - 16, vy + 70, 22):
        d.rectangle([bx, wy, bx + 18, wy + 10], fill=(255, 205, 80))
# seismograph trace above the skyline
pts = []
for i in range(0, 221, 6):
    amp = 3 if i < 60 else (16 if 60 <= i < 160 else 4)
    pts.append((vx - 70 + i, vy - 88 + (amp if (i // 6) % 2 else -amp)))
d.line(pts, fill=RED, width=3)
# magnitude badge, top left of the visual
# (was 62px circle with 61px-wide "M7.5" — the "5" clipped on the curve)
bcx, bcy, br = 672, 230, 42
d.ellipse([bcx - br, bcy - br, bcx + br, bcy + br], fill=RED, outline=(255, 255, 255), width=3)
mag_f = F(SANS_B, 22)
sub_f = F(SANS_B, 14)
mag = "M7.5"
sub = "7.2"
d.text((bcx - d.textlength(mag, font=mag_f) / 2, bcy - 24), mag, font=mag_f, fill=(255, 255, 255))
d.text((bcx - d.textlength(sub, font=sub_f) / 2, bcy + 4), sub, font=sub_f, fill=(255, 255, 255))

# ---------- secondary cards (2 x 2) ----------
CARDS = [
    ("ASIA · SPACE", TEAL, "SHENZHOU-24 BLASTS OFF",
     "China launches Shenzhou-24 with the first Pakistani astronaut aboard — the first foreign visitor to Tiangong station."),
    ("ECONOMY · TECH", RED, "NVIDIA ROUT DEEPENS",
     "Nasdaq 100 falls 2% as Nvidia drops 5.9% and chip stocks sink 7.9%. Dow regains 50,000; VIX nears 26."),
    ("EUROPE · WAR", RED, "PUTIN VOWS RETALIATION",
     "Putin says Ukraine keeps hitting refineries despite Trump's plea, pledges an 'inevitable' reply. Medvedev warns of a nuclear strike."),
    ("MIDDLE EAST · SHIPPING", TEAL, "HORMUZ SHIPPING HIT",
     "Iran claims tankers hit mines in the Strait. Coalition strikes Hodeidah as Houthis threaten Saudi ports."),
]
cw, chh, gap = 482, 112, 10
for i, (kick, col, head, body) in enumerate(CARDS):
    x = 24 + (i % 2) * (cw + gap)
    y = 420 + (i // 2) * (chh + gap)
    d.rectangle([x, y, x + cw, y + chh], fill=CARD, outline=INK, width=2)
    d.rectangle([x, y, x + cw, y + 24], fill=col)
    d.text((x + 12, y + 4), kick, font=F(SANS_B, 14), fill=(255, 255, 255))
    d.text((x + 12, y + 30), head, font=F(SERIF_B, 23), fill=INK)
    text_block(d, (x + 12, y + 60), body, F(SANS, 14), INK, cw - 24, 18)

# ---------- briefs: three ruled columns of one-liners ----------
BY = 664
d.line([24, BY - 6, 1000, BY - 6], fill=INK, width=3)
d.text((24, BY), "IN BRIEF — 46 MORE STORIES FROM TODAY'S REPORTING", font=F(SANS_B, 17), fill=INK)

BRIEF_COLS = [
    [("EUR", "Ukraine: Libya strike self-defence"),
     ("EUR", "Zelensky confirms Finland ship hit"),
     ("EUR", "Norway pledges $7bn to Ukraine 2027"),
     ("EUR", "Russia budget: defence up 27%"),
     ("EUR", "Moscow summons Latvia envoy"),
     ("EUR", "Magyar meets Zelensky, first talks"),
     ("EUR", "UK warns of Russian sabotage threat"),
     ("MID", "Houthis hit Riyadh tower again: 11 hurt"),
     ("MID", "US warns Americans of Houthi threat"),
     ("MID", "Houthis 60 km from Aden; city holds"),
     ("MID", "Iraq PM moves on Kurdish oilfields"),
     ("MID", "Eisenkot clinches first coalition pact"),
     ("ASIA", "Xi probes Shanghai boss Chen Jining"),
     ("ASIA", "Australia-Solomons pact stymies China"),
     ("ASIA", "US slams Australia social media law"),
     ("ASIA", "Seoul: Russian jets in defence zone")],
    [("ASIA", "Seoul subway strike called off"),
     ("ASIA", "Taiwan local vote tests Lai"),
     ("ASIA", "Australia inflation jumps to 4.9%"),
     ("ASIA", "Rakuten breach leaks client data"),
     ("ASIA", "Huawei guilty on 10 of 12 counts"),
     ("ASIA", "Landmine toll hits 5-year high: 7,000"),
     ("ASIA", "Myanmar rebel vows to fight on"),
     ("ASIA", "Bangladesh students hit out at India"),
     ("AFR", "50 feared dead in Nigeria boat capsize"),
     ("AFR", "37 killed in Borno airstrikes"),
     ("AFR", "Ten killed in Egypt road crash"),
     ("AFR", "Libya wants Zelensky on terror list"),
     ("AMER", "Trump gives Giuliani Medal of Freedom"),
     ("AMER", "Trump pardons turkeys Freedom, Feathers"),
     ("AMER", "WHO: lift US fuel blockade on Cuba")],
    [("AMER", "Fort Hood gunman seeks stay of execution"),
     ("AMER", "US soldier admits selling secrets to China"),
     ("AMER", "Six missing after Mississippi plane crash"),
     ("AMER", "Gunmen hold 25 hostage in Colombia"),
     ("AMER", "Car bomb wounds 20+ in Colombia"),
     ("AMER", "Floods threaten California"),
     ("TECH", "US to unveil new tariffs after probe"),
     ("TECH", "Shein pays $100m to settle US case"),
     ("TECH", "Sanofi to buy Insmed for $41bn"),
     ("TECH", "Sensex jumps 1,500; Nifty tops 25,750"),
     ("SPRT", "Chess Game 1: Gukesh holds Sindarov"),
     ("SPRT", "Real Madrid hit PSV 5-1 in Europe"),
     ("SPRT", "NPB stars Sato, Taira agree MLB deals"),
     ("SPRT", "Norway shuts out Russian skaters"),
     ("CULT", "Thomas Markle indicted in US court")],
]

BF = F(SANS, 13)
KF = F(SANS_B, 9)
for ci, items in enumerate(BRIEF_COLS):
    col_x = 24 + ci * 333
    if ci:
        d.line([col_x - 10, BY + 28, col_x - 10, 950], fill=(200, 195, 180), width=1)
    y = BY + 30
    for kick, line in items:
        d.text((col_x, y + 2), kick, font=KF, fill=RED)
        d.text((col_x + 40, y), line, font=BF, fill=INK)
        y += 16.5

# ---------- timeline strip ----------
TY = 966
d.rectangle([0, TY, W, H], fill=DARK)
d.text((24, TY + 6), "THE DAY AROUND THE CLOCK (UTC):", font=F(SANS_B, 13), fill=(255, 205, 80))
d.text((24, TY + 24),
       "BEIJING SHENZHOU LAUNCH \u2192 SEOUL SUBWAY DEAL \u2192 SYDNEY CPI JUMP \u2192 "
       "CARACAS TWIN QUAKES \u2192 BAGHDAD OILFIELD MOVE",
       font=F(SANS_B, 11), fill=(255, 255, 255))
d.text((24, TY + 41),
       "LONDON SABOTAGE WARNING \u2192 GENEVA CHESS DRAW \u2192 NEW YORK NVIDIA ROUT "
       "\u2192 WASHINGTON MEDAL & PARDON",
       font=F(SANS_B, 11), fill=(255, 255, 255))

img.save("entry.png", optimize=True)
print("saved entry.png")

