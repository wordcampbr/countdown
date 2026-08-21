#!/usr/bin/env python3
"""Gera countdown.svg (dias restantes até o WordCamp Brasil 2026).

Visual espelha o componente .wcbr-countdown do site (Poppins 900 no número,
Manrope letter-spaced no rótulo, fundo cyan-700 sólido).
"""

from datetime import datetime, timezone, timedelta

TARGET = datetime(2026, 10, 30, 15, 30, 0, tzinfo=timezone.utc)  # 12:30 BRT
CYAN_700 = "#00595D"
SAND_100 = "#FFF8F1"

FONT_TITLE = "Poppins, -apple-system, Segoe UI, Roboto, Arial, sans-serif"
FONT_LABEL = "Manrope, -apple-system, Segoe UI, Roboto, Arial, sans-serif"

TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" width="280" height="170" viewBox="0 0 280 170" role="img" aria-label="{aria_label}">
  <rect width="280" height="170" rx="16" fill="{cyan}"/>
  <text x="140" y="38" text-anchor="middle" font-family="{font_title}" font-size="14" font-weight="700" letter-spacing="2.3" fill="{sand}">CONTAGEM REGRESSIVA</text>
  <text x="140" y="118" text-anchor="middle" font-family="{font_title}" font-size="72" font-weight="900" fill="{sand}">{number}</text>
  <text x="140" y="146" text-anchor="middle" font-family="{font_label}" font-size="15" font-weight="600" letter-spacing="2" fill="{sand}">{unit_label}</text>
</svg>
"""


def main():
    now = datetime.now(timezone.utc)
    diff = TARGET - now

    if diff <= timedelta(0):
        number = "0"
        unit_label = "DIAS"
        aria_label = "O WordCamp Brasil 2026 está rolando"
    else:
        days = diff.days
        number = str(days)
        unit_label = "DIA" if days == 1 else "DIAS"
        aria_label = f"Faltam {days} dias para o WordCamp Brasil 2026"

    svg = TEMPLATE.format(
        cyan=CYAN_700,
        sand=SAND_100,
        font_title=FONT_TITLE,
        font_label=FONT_LABEL,
        number=number,
        unit_label=unit_label,
        aria_label=aria_label,
    )

    with open("countdown.svg", "w", encoding="utf-8") as f:
        f.write(svg)

    print(f"countdown.svg atualizado: {aria_label}")


if __name__ == "__main__":
    main()
