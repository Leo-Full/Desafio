"""
Desafio 1 - Comissão por vendedor
Regras por venda:
  - abaixo de R$ 100,00      -> sem comissão
  - abaixo de R$ 500,00      -> 1%
  - a partir de R$ 500,00    -> 5%
"""
import json
from decimal import Decimal, ROUND_HALF_UP


def calcular_comissao(valor: Decimal) -> Decimal:
    if valor < 100:
        taxa = Decimal("0")
    elif valor < 500:
        taxa = Decimal("0.01")
    else:
        taxa = Decimal("0.05")
    return (valor * taxa).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def moeda(v: Decimal) -> str:
    return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def main():
    with open("vendas.json", encoding="utf-8") as f:
        # parse_float=Decimal evita erros de arredondamento com dinheiro
        dados = json.load(f, parse_float=Decimal)

    resumo = {}  # vendedor -> {"total": ..., "comissao": ..., "qtd": ...}
    for venda in dados["vendas"]:
        nome = venda["vendedor"]
        valor = Decimal(venda["valor"])
        r = resumo.setdefault(nome, {"total": Decimal("0"), "comissao": Decimal("0"), "qtd": 0})
        r["total"] += valor
        r["comissao"] += calcular_comissao(valor)
        r["qtd"] += 1

    print(f"{'Vendedor':<18}{'Vendas':>7}{'Total vendido':>18}{'Comissão':>14}")
    print("-" * 57)
    for nome, r in resumo.items():
        print(f"{nome:<18}{r['qtd']:>7}{moeda(r['total']):>18}{moeda(r['comissao']):>14}")
    print("-" * 57)
    total_geral = sum(r["comissao"] for r in resumo.values())
    print(f"{'Total de comissões':<43}{moeda(total_geral):>14}")


if __name__ == "__main__":
    main()
