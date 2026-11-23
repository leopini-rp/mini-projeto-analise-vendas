import pandas as pd
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import seaborn as sns


df_vendas = pd.read_csv("vendas.csv", encoding="utf-8-sig")

faturamento_categoria = (
    df_vendas.groupby("Categoria")["Faturamento"]
    .sum()
    .sort_values(ascending=False)
)

faturamento_ordenado = faturamento_categoria.sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(12, 7))


def formatar_milhoes(valor, posicao):
    return f"{valor / 1_000_000:g}".replace(".", ",")


ax.yaxis.set_major_formatter(
    FuncFormatter(formatar_milhoes)
)

faturamento_ordenado.plot(
    kind="bar",
    ax=ax,
    color=sns.color_palette("viridis", len(faturamento_ordenado))
)

ax.set_title("Faturamento por categoria", fontsize=16)
ax.set_xlabel("Categoria", fontsize=12)
ax.set_ylabel("Faturamento (R$ milhões)", fontsize=12)

plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
