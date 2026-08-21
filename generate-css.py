#!/usr/bin/env python3
"""Gera countdown.css — contador de DIAS 100% CSS (sem JS), via @property + steps().

Só funciona bem para "dias restantes": é uma animação single-shot (não repete),
então não sofre o drift que uma animação CSS em loop teria para horas/min/seg
(o total de "steps" nunca bate exatamente com o período real de 24h/60min/60s
em loop infinito — por isso o contador ao vivo continua sendo o countdown-live.svg,
via JS). Este arquivo é regenerado 1x por dia pelo GitHub Actions para não perder
precisão entre uma geração e outra.
"""

from datetime import datetime, timezone, timedelta

TARGET = datetime(2026, 10, 30, 15, 30, 0, tzinfo=timezone.utc)  # 12:30 BRT

TEMPLATE = """/* Gerado automaticamente por generate-css.py — não editar à mão. */
/* Cole em Aparência > Personalizar > CSS Adicional. */

@property --wcbr-days {{
  syntax: '<integer>';
  inherits: false;
  initial-value: {days};
}}

.wcbr-count-days {{
  animation: wcbr-count-days-anim {duration}s steps({days}, end) forwards;
}}

@keyframes wcbr-count-days-anim {{
  from {{ --wcbr-days: {days}; }}
  to   {{ --wcbr-days: 0; }}
}}

.wcbr-count-days::before {{
  counter-reset: wcbr-days var(--wcbr-days);
  content: counter(wcbr-days);
}}
"""

FALLBACK = """/* Gerado automaticamente por generate-css.py — não editar à mão. */

.wcbr-count-days::before {
  content: "0";
}
"""


def main():
    now = datetime.now(timezone.utc)
    diff = TARGET - now

    if diff <= timedelta(0):
        css = FALLBACK
        print("O WordCamp Brasil 2026 já começou — countdown.css zerado.")
    else:
        days = diff.days + 1  # arredonda pra cima: conta o dia corrente também
        duration = days * 86400
        css = TEMPLATE.format(days=days, duration=duration)
        print(f"countdown.css atualizado: {days} dias restantes.")

    with open("countdown.css", "w", encoding="utf-8") as f:
        f.write(css)


if __name__ == "__main__":
    main()
