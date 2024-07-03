import pandas as pd

def save(data: pd.DataFrame, destination: str) -> None:
    """
    Salva os dados transformados para um destino especificado.
    
    Args:
        data (pd.DataFrame): Dados transformados.
        destination (str): Caminho ou URL do destino dos dados.
    """
    # Exemplo de carga para um arquivo CSV
    data.to_csv(destination, index=False)