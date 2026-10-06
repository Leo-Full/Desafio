"""
Desafio 2 - Movimentação de estoque
Cada movimentação tem um ID único e uma descrição; ao final mostra o
estoque final do produto movimentado. As alterações são salvas no JSON.
"""
import json
from datetime import datetime

ARQ_ESTOQUE = "estoque.json"
ARQ_MOVIMENTACOES = "movimentacoes.json"


def carregar(arquivo, padrao):
    try:
        with open(arquivo, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return padrao


def salvar(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)


def proximo_id(movimentacoes):
    return max((m["id"] for m in movimentacoes), default=0) + 1


def movimentar(estoque, movimentacoes, codigo, tipo, quantidade, descricao):
    """tipo: 'E' (entrada) ou 'S' (saída). Retorna a qtde final do produto."""
    produto = next((p for p in estoque["estoque"] if p["codigoProduto"] == codigo), None)
    if produto is None:
        raise ValueError(f"Produto {codigo} não encontrado.")
    if quantidade <= 0:
        raise ValueError("A quantidade deve ser maior que zero.")
    if tipo == "S" and quantidade > produto["estoque"]:
        raise ValueError(f"Estoque insuficiente (disponível: {produto['estoque']}).")

    produto["estoque"] += quantidade if tipo == "E" else -quantidade

    movimentacoes.append({
        "id": proximo_id(movimentacoes),
        "descricao": descricao,
        "tipo": "ENTRADA" if tipo == "E" else "SAIDA",
        "codigoProduto": codigo,
        "quantidade": quantidade,
        "estoqueFinal": produto["estoque"],
        "dataHora": datetime.now().isoformat(timespec="seconds"),
    })
    return produto


def listar(estoque):
    print(f"\n{'Código':<8}{'Produto':<30}{'Estoque':>8}")
    for p in estoque["estoque"]:
        print(f"{p['codigoProduto']:<8}{p['descricaoProduto']:<30}{p['estoque']:>8}")
    print()


def main():
    estoque = carregar(ARQ_ESTOQUE, {"estoque": []})
    movimentacoes = carregar(ARQ_MOVIMENTACOES, [])

    while True:
        listar(estoque)
        opcao = input("[1] Lançar movimentação  [0] Sair: ").strip()
        if opcao == "0":
            break
        if opcao != "1":
            continue
        try:
            codigo = int(input("Código do produto: "))
            tipo = input("Tipo - (E)ntrada ou (S)aída: ").strip().upper()
            if tipo not in ("E", "S"):
                raise ValueError("Tipo inválido, use E ou S.")
            quantidade = int(input("Quantidade: "))
            descricao = input("Descrição (ex: Compra de fornecedor, Venda, Avaria): ").strip()
            if not descricao:
                raise ValueError("A descrição é obrigatória.")

            produto = movimentar(estoque, movimentacoes, codigo, tipo, quantidade, descricao)
            salvar(ARQ_ESTOQUE, estoque)
            salvar(ARQ_MOVIMENTACOES, movimentacoes)

            mov = movimentacoes[-1]
            print(f"\nMovimentação #{mov['id']} registrada ({mov['tipo']} - {mov['descricao']}).")
            print(f"Estoque final de '{produto['descricaoProduto']}': {produto['estoque']}")
        except ValueError as e:
            print(f"\nErro: {e}")


if __name__ == "__main__":
    main()
