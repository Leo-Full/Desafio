# Desafio

Resolução de três exercícios em Python (3.10+), sem dependências externas.
Os arquivos estão na pasta `Desafio/`.

## Como executar

```bash
cd Desafio
python desafio1_comissao.py
python desafio2_estoque.py
python desafio3_juros.py
```

## 1. Comissão de vendedores (`desafio1_comissao.py`)
Lê `vendas.json` e calcula a comissão de cada vendedor:
- Vendas abaixo de R$ 100,00: sem comissão
- Vendas abaixo de R$ 500,00: 1%
- A partir de R$ 500,00: 5%

Usa `Decimal` para evitar erros de arredondamento com valores monetários.

## 2. Movimentação de estoque (`desafio2_estoque.py`)
Menu interativo para lançar entradas e saídas dos produtos de `estoque.json`.
Cada movimentação recebe um ID único sequencial e uma descrição, e é gravada em
`movimentacoes.json`. Ao final, exibe a quantidade final em estoque do produto.
Valida produto inexistente, quantidade inválida e saída maior que o saldo.

## 3. Juros por atraso (`desafio3_juros.py`)
A partir de um valor e de uma data de vencimento, calcula os juros até a data de
hoje com multa de 2,5% ao dia (juros simples). Se não estiver vencido, não há juros.
