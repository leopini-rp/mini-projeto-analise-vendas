import pandas as pd


df_vendas = pd.read_csv("vendas.csv", encoding="utf-8-sig")

df_vendas["Faturamento"] = (
    df_vendas["Preco_Unitario"] * df_vendas["Quantidade"]
)

df_vendas["Status_Entrega"] = (
    df_vendas["Estado"].apply(
        lambda estado: "Rápida" if estado in ["SP", "RJ", "MG"] else "Normal"
    )
)

df_vendas["Data_Pedido"] = pd.to_datetime(df_vendas["Data_Pedido"])

df_vendas["Mes"] = (
    df_vendas["Data_Pedido"].dt.to_period("M")
)

df_vendas.to_csv("vendas.csv", encoding="utf-8-sig")
