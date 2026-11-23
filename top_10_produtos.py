# Pandas manipula os dados; seaborn define o estilo; pyplot cria o gráfico.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


# Lê o CSV em um DataFrame
df_vendas = pd.read_csv("vendas.csv", encoding="utf-8-sig")

# Soma as quantidades por produto, ordena do maior para o menor e seleciona 10.
top_10_products = (
    df_vendas.groupby("Nome_Produto")["Quantidade"].sum().sort_values(
        ascending=False).head(10)
    )

# Seleciona os 10 produtos com maior faturamento.
top_10_profit = (
    df_vendas.groupby("Nome_Produto")["Faturamento"].sum().sort_values(
        ascending=False).head(10)
    )

# nlargest seleciona os 10 maiores faturamentos;
top_10 = (
    df_vendas.groupby("Nome_Produto")[["Faturamento", "Quantidade"]]
    .sum()
    .nlargest(10, "Faturamento")
    .sort_values("Faturamento")
)

sns.set_style("whitegrid")

# Cria a figura com tamanho em polegadas e o eixo principal de faturamento.
fig, ax_faturamento = plt.subplots(figsize=(12, 8))
# Cria um eixo horizontal no topo, com escala própria para a quantidade.
# As posições verticais dos produtos são compartilhadas pelos dois eixos.
ax_quantidade = ax_faturamento.twiny()

# Define uma posição vertical para cada produto (0, 1, 2, ...).
posicoes = list(range(len(top_10)))
# Define a espessura das barras nas coordenadas do eixo vertical.
altura = 0.35

# Desenha barras horizontais de faturamento acima do centro de cada produto.
# O deslocamento + altura / 2 separa as barras;
barras_faturamento = ax_faturamento.barh(
    [p + altura / 2 for p in posicoes],
    top_10["Faturamento"],
    height=altura,
    color="skyblue",
    label="Faturamento",
)

# Desenha a quantidade dos mesmos produtos abaixo das barras de faturamento.
# O deslocamento - altura / 2 evita a sobreposição entre as duas barras.
barras_quantidade = ax_quantidade.barh(
    [p - altura / 2 for p in posicoes],
    top_10["Quantidade"],
    height=altura,
    color="orange",
    label="Quantidade",
)

# Define onde ficam as marcações verticais de cada par de barras.
ax_faturamento.set_yticks(posicoes)
# Usa os nomes dos produtos, armazenados no índice, como rótulos verticais.
ax_faturamento.set_yticklabels(top_10.index)

# Identifica a escala inferior de faturamento em reais.
ax_faturamento.set_xlabel("Faturamento (R$ milhões)")
# Identifica a escala superior de quantidade em unidades.
ax_quantidade.set_xlabel("Quantidade vendida(unidades)")
# Nomeia o eixo vertical.
ax_faturamento.set_ylabel("Produto")
# Define o título; pad controla o espaço entre ele e o gráfico.
ax_faturamento.set_title(
    "Top 10 produtos por faturamento",
    pad=20,
)

# Desativa a grade do segundo eixo para evitar duas grades sobrepostas.
ax_quantidade.grid(False)

# Reúne as barras dos dois eixos na legenda, no canto inferior direito.
ax_faturamento.legend(
    handles=[barras_faturamento, barras_quantidade],
    loc="lower right",
)


def formatar_milhoes(valor, posicao):
    return f"{valor / 1_000_000:g}".replace(".", ",")


ax_faturamento.xaxis.set_major_formatter(
    FuncFormatter(formatar_milhoes)
)

# Versão anterior do gráfico;
# top_10_profit.sort_values(
#     ascending=True
# ).plot(
#     kind="barh", color="skyblue"
# )

# plt.title("Top 10 produtos com maior lucratividade", fontsize=16)
# plt.xlabel("Faturamento", fontsize=12)
# plt.ylabel("Produto", fontsize=12)

plt.tight_layout()
plt.show()
