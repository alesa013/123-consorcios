# recomendador.py
# Parte da Alessandra: lógica de validação e de recomendação.

from pathlib import Path  # ajuda a localizar arquivos no computador
import pandas as pd       # biblioteca para trabalhar com tabelas

# O catálogo fica na mesma pasta deste arquivo .py,
# não importa de onde o programa seja executado.
CAMINHO_CATALOGO = Path(__file__).parent / "consorcios.csv"


def carregar_catalogo():
    """Lê o consorcios.csv e devolve a tabela (DataFrame)."""
    catalogo = pd.read_csv(CAMINHO_CATALOGO, encoding="utf-8")
    return catalogo


# Este bloco só roda quando executamos "python recomendador.py" direto.
# Se a Esther importar este arquivo, ele é ignorado.
if __name__ == "__main__":
    tabela = carregar_catalogo()
    print(tabela)
    print()
    print(tabela.dtypes)
    print()
    print("Quantidade de consórcios:", len(tabela))