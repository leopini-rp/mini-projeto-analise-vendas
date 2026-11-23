import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

df_vendas = pd.read_csv("vendas.csv", encoding="utf-8-sig")

faturamento_mensal = df_vendas.groupby("Mes")["Faturamento"].sum()

plt.figure(figsize=(12, 6))

ax = faturamento_mensal.plot(
    kind="line", marker="o", linestyle="-", color="green"
    )


def formatar_milhoes(valor, posicao):
    return f"{valor / 1_000_000:g}".replace(".", ",")


ax.yaxis.set_major_formatter(
    FuncFormatter(formatar_milhoes)
)

plt.title("Evolução do faturamento mensal", fontsize=16)
plt.xlabel("Mês", fontsize=12)
plt.ylabel("Faturamento (R$ milhões)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

plt.tight_layout()
plt.show()
