from pathlib import Path
from unittest.mock import patch
import runpy

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

pasta_imagens = Path("imagens")
pasta_imagens.mkdir(exist_ok=True)

graficos = {
    "top_10_produtos.py": "top_10_produtos.png",
    "faturamento_mensal.py": "faturamento_mensal.png",
    "vendas_categoria.py": "vendas_categoria.png",
    "vendas_estado.py": "vendas_estado.png",
}

with patch("matplotlib.pyplot.show"):
    for script, nome_imagem in graficos.items():
        runpy.run_path(script, run_name="__main__")

        plt.savefig(
            pasta_imagens / nome_imagem,
            dpi=300,
            bbox_inches="tight",
        )

        plt.close("all")
        print(f"Imagem salva: {pasta_imagens / nome_imagem}")
