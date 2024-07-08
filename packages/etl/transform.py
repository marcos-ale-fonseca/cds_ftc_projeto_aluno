# # Adicione o caminho do diretório raiz do projeto
import os, sys; sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
from haversine import haversine

def dataframe(df_raw: pd.DataFrame) -> pd.DataFrame:

    """
    Transforma e limpa os dados extraídos.
    
    Args:
        df (pd.DataFrame): Dados extraídos.
    
    Returns:
        pd.DataFrame: Dados transformados.
    """
    
    import utils

    # Copiar dados
    df = df_raw.copy()

    # Renomear colunas
    df = utils.rename_columns(df)
    
    # Apagar valores faltantes e a feature switch_to_order_menu
    df = df.dropna()
    df = df.drop_duplicates()
    df = df.drop('switch_to_order_menu', axis=1)

    # Definir primeiro valor ao converter para lista.
    df["cuisines"] = df.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])

    # Definir o nome da cor para cada cor hexadecimal
    df['rating_color_name'] = df.rating_color.apply(utils.color_name)

    # Definir um nome de avaliação para cada cor hexadecimal
    df['rating_name'] = df.rating_color.apply(utils.rating_name)
    df[[
        'rating_color',
        'rating_color_name', 
        'rating_name', 
        ]].value_counts()
    
    # Adicionar nome do país
    df['country_name'] = df.country_code.apply(utils.country_name)
    df[['country_code', 'country_name']].sample(10)

    # Adicionar tipo para intervalo de preço
    df['price_type'] = df.price_range.apply(utils.create_price_type)
    df[['price_range', 'price_type']].sample(10)

    # Convertendo para categorica
    df.has_table_booking = df.has_table_booking.astype('category')
    df.has_online_delivery = df.has_online_delivery.astype('category')
    df.is_delivering_now = df.is_delivering_now.astype('category')
    df.price_range = df.price_range.astype('category')
    df.rating_color = df.rating_color.astype('category')
    df.rating_name = df.rating_name.astype('category')
    df.rating_color_name = df.rating_color_name.astype('category')
    df.currency = df.currency.astype('category')
    df.select_dtypes(include='category')
    
    return df