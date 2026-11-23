import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df_vendas = pd.read_csv("vendas.csv", encoding="utf-8-sig")

vendas_estado = (
    df_vendas.groupby("Estado")["Faturamento"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12, 7))

vendas_estado.plot(kind="bar", color=sns.color_palette("husl", 7))

plt.title("Faturamento por estado", fontsize=16)
plt.xlabel("Estado", fontsize=12)
plt.ylabel("Faturamento (R$)", fontsize=12)
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()
