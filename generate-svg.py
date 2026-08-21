#!/usr/bin/env python3
"""Gera countdown.svg (dias restantes até o WordCamp Brasil 2026)."""

from datetime import datetime, timezone, timedelta

TARGET = datetime(2026, 10, 30, 12, 0, 0, tzinfo=timezone.utc)  # 09:00 BRT
CYAN_700 = "#00595D"
SAND_100 = "#FFF8F1"
ORANGE_600 = "#C6360B"

TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" width="320" height="140" viewBox="0 0 320 140" role="img" aria-label="{aria_label}">
  <rect width="320" height="140" rx="16" fill="{cyan}"/>
  <text x="160" y="66" text-anchor="middle" font-family="-apple-system,Segoe UI,Roboto,Arial,sans-serif" font-size="56" font-weight="800" fill="{sand}">{number}</text>
  <text x="160" y="92" text-anchor="middle" font-family="-apple-system,Segoe UI,Roboto,Arial,sans-serif" font-size="14" font-weight="600" letter-spacing="1" fill="{sand}">{unit_label}</text>
  <text x="160" y="122" text-anchor="middle" font-family="-apple-system,Segoe UI,Roboto,Arial,sans-serif" font-size="12" fill="{sand}" opacity="0.85">{footer}</text>
</svg>
"""


def main():
    now = datetime.now(timezone.utc)
    diff = TARGET - now

    if diff <= timedelta(0):
        number = "0"
        unit_label = "O WORDCAMP BRASIL 2026 ESTÁ ROLANDO!"
        aria_label = "O WordCamp Brasil 2026 está rolando"
    else:
        days = diff.days
        number = str(days)
        unit_label = "DIA" if days == 1 else "DIAS PARA O WCBR 2026"
        aria_label = f"Faltam {days} dias para o WordCamp Brasil 2026"

    svg = TEMPLATE.format(
        cyan=CYAN_700,
        sand=SAND_100,
        number=number,
        unit_label=unit_label,
        footer="30 e 31 de outubro · Belo Horizonte (FUMEC)",
        aria_label=aria_label,
    )

    with open("countdown.svg", "w", encoding="utf-8") as f:
        f.write(svg)

    print(f"countdown.svg atualizado: {aria_label}")


if __name__ == "__main__":
    main()
