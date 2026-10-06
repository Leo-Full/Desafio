"""
Desafio 3 - Juros por atraso
A partir de um valor e de uma data de vencimento, calcula os juros na
data de hoje, com multa de 2,5% ao dia de atraso (juros simples).
"""
from datetime import date, datetime
from decimal import Decimal, ROUND_HALF_UP

TAXA_DIA = Decimal("0.025")


def calcular_juros(valor: Decimal, vencimento: date, hoje: date | None = None):
    hoje = hoje or date.today()
    dias_atraso = max((hoje - vencimento).days, 0)  # sem atraso, sem juros
    juros = (valor * TAXA_DIA * dias_atraso).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return dias_atraso, juros, valor + juros


def moeda(v: Decimal) -> str:
    return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def main():
    try:
        valor = Decimal(input("Valor (ex: 1500,00): ").replace(".", "").replace(",", "."))
        vencimento = datetime.strptime(input("Vencimento (dd/mm/aaaa): ").strip(), "%d/%m/%Y").date()
    except Exception:
        print("Entrada inválida.")
        return

    dias, juros, total = calcular_juros(valor, vencimento)
    print(f"\nData de hoje:   {date.today():%d/%m/%Y}")
    print(f"Dias de atraso: {dias}")
    print(f"Juros (2,5%/dia): {moeda(juros)}")
    print(f"Valor total:    {moeda(total)}")


if __name__ == "__main__":
    main()
