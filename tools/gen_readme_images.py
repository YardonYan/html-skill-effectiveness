# -*- coding: utf-8 -*-
"""为 html-skill-effectiveness 生成 README 配图。

字体约定：中文一律走 msyh / msyhbd，Consolas 只用于纯英文与代码片段，
否则中文字形会渲染成方块。
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")

REG = "C:/Windows/Fonts/msyh.ttc"
BOLD = "C:/Windows/Fonts/msyhbd.ttc"
MONO = "C:/Windows/Fonts/consola.ttf"
# 宋体的 ASCII 是半角等宽，且自带 CJK 字形，用来模拟 markdown 源码最合适；
# Consolas 没有中文字形，直接用来写「# 方案对比」会渲染成方块。
SRC = "C:/Windows/Fonts/simsun.ttc"

BG_TOP = (20, 19, 17)
BG_BOT = (38, 33, 30)
PANEL = (28, 27, 25)
LINE = (74, 66, 60)
TXT = (250, 250, 247)
SUB = (156, 148, 140)
DIM = (110, 103, 97)

ACCENT = (201, 100, 66)
ACCENT_SOFT = (232, 168, 145)
PAPER = (250, 250, 247)
INK = (26, 25, 22)
MUTED = (107, 105, 100)
HAIRLINE = (232, 229, 223)


def f(path, size):
    return ImageFont.truetype(path, size)


def vgrad(size, c1, c2):
    w, h = size
    strip = Image.new("RGB", (1, h))
    d = ImageDraw.Draw(strip)
    for y in range(h):
        t = y / max(h - 1, 1)
        d.point((0, y), fill=tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3)))
    return strip.resize((w, h))


def card(draw, box, radius=16, fill=PANEL, outline=LINE, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def bar(draw, x, y, w, h, color, radius=None):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=radius if radius is not None else h / 2,
                           fill=color)


def dots(draw, x, y, color=DIM):
    for i in range(3):
        cx = x + i * 16
        draw.ellipse([cx - 5, y - 5, cx + 5, y + 5], fill=color)


def hero():
    W, H = 1500, 560
    img = vgrad((W, H), BG_TOP, BG_BOT)
    d = ImageDraw.Draw(img)

    d.text((70, 56), "把略读的文档，变成会读的文档", font=f(BOLD, 46), fill=TXT)
    d.text((70, 124), "Trade documents people skim for documents people actually read",
           font=f(REG, 23), fill=SUB)
    d.text((70, 162), "13 种实战模式 · 7 条工艺规则 · 零依赖单文件",
           font=f(REG, 20), fill=DIM)

    PY0, PY1 = 214, 496

    # ── 左：Markdown ──────────────────────────────────────────────
    card(d, [70, PY0, 660, PY1], radius=18, fill=PANEL, outline=LINE)
    dots(d, 102, PY0 + 26)
    d.text((102, PY0 + 48), "PLAIN MARKDOWN", font=f(MONO, 14), fill=DIM)

    lines = ["# 方案对比",
             "",
             "- 方案 A：性能更好",
             "- 方案 B：上手更快",
             "",
             "**结论**：见下文分析……"]
    for i, s in enumerate(lines):
        d.text((102, PY0 + 86 + i * 27), s, font=f(SRC, 17), fill=(130, 122, 114))

    for i, w in enumerate((438, 392, 448, 330, 414, 280)):
        bar(d, 102, PY0 + 262 + i * 22, w, 9, (60, 54, 49), radius=5)

    # ── 右：HTML ─────────────────────────────────────────────────
    RX0, CX = 840, 868
    d.rounded_rectangle([RX0, PY0, 1430, PY1], radius=18, fill=PAPER, outline=HAIRLINE, width=2)
    d.ellipse([CX - 4, PY0 + 20, CX + 10, PY0 + 34], fill=ACCENT)
    d.text((CX + 22, PY0 + 18), "rendered page · single file · zero deps",
           font=f(MONO, 13), fill=MUTED)

    d.text((CX, PY0 + 54), "并排对比，一眼看清取舍", font=f(BOLD, 27), fill=INK)
    d.text((CX, PY0 + 94), "Side-by-side, trade-offs at a glance", font=f(REG, 16), fill=MUTED)
    d.line([CX, PY0 + 122, 1396, PY0 + 122], fill=HAIRLINE, width=1)

    for i, (cx, name) in enumerate(((CX, "方案 A"), (CX + 264, "方案 B"))):
        d.rounded_rectangle([cx, PY0 + 136, cx + 256, PY0 + 216], radius=10,
                            fill=(255, 255, 255), outline=HAIRLINE)
        d.rounded_rectangle([cx + 16, PY0 + 150, cx + 22, PY0 + 174],
                            radius=3, fill=ACCENT if i == 0 else ACCENT_SOFT)
        d.text((cx + 34, PY0 + 150), name, font=f(BOLD, 16), fill=INK)
        bar(d, cx + 34, PY0 + 176, 106, 6, HAIRLINE, radius=3)
        bar(d, cx + 16, PY0 + 194, 158, 6, HAIRLINE, radius=3)
        bar(d, cx + 186, PY0 + 194, 54, 6, HAIRLINE, radius=3)

    for i, hh in enumerate((26, 48, 34, 62, 40, 54)):
        bx = CX + i * 34
        d.rounded_rectangle([bx, PY0 + 266 - hh, bx + 20, PY0 + 266], radius=4,
                            fill=ACCENT if i % 2 == 0 else ACCENT_SOFT)
    d.text((CX + 258, PY0 + 242), "可缩放点击的图表", font=f(REG, 15), fill=MUTED)

    # ── 中缝 ─────────────────────────────────────────────────────
    d.text([750 - d.textlength("这个 Skill 做的事", font=f(REG, 18)) / 2, PY0 + 112],
           "这个 Skill 做的事", font=f(REG, 18), fill=ACCENT_SOFT)
    ax0, ax1, ay = 678, 822, PY0 + 162
    d.line([ax0, ay, ax1 - 14, ay], fill=ACCENT, width=4)
    d.polygon([(ax1, ay), (ax1 - 16, ay - 9), (ax1 - 16, ay + 9)], fill=ACCENT)

    img.save(os.path.join(OUT, "hero.png"))
    print("hero.png")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    hero()
