import pandas as pd
import inflection


DATA_PATH = '/Users/developer/Documents/Learn/DataScience/ComunidadeDS/FTC-AnalisandoDadosComPython/local/ftc_projeto_do_aluno/data/processed/zomato.csv'

height_hack = '''
<script>
    var hide_me_list = window.parent.document.querySelectorAll('iframe');
    for (let i = 0; i < hide_me_list.length; i++) { 
        if (hide_me_list[i].height == 0) {
            hide_me_list[i].parentNode.style.height = 0;
            hide_me_list[i].parentNode.style.marginBottom = '-1rem';
        };
    };
</script>
'''

COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
}

COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "FF7800": "darkred",
    "CBCBC8": "gray",
}

RATING = {
    "3F7E00": "excellent",
    "5BA829": "great",
    "9ACD32": "very_good",
    "CDD614": "good",
    "FFBA00": "average",
    "FF7800": "poor",
    "CBCBC8": 'not_rated',
}

DEFAUT_CUISINES = [
    'Italian',
    'American',
    'Arabian',
    'Japanese',
    'Brazilian',
]

DEFAUT_COUNTRIES = [
    'England', 
    'South Africa', 
    'Brazil', 
    'Australia', 
    'Canada', 
    'Qatar'
]

def df_processed():
    from etl import extract
    return extract.csv(DATA_PATH)

def get_countries(df):
    result = (
        pd.Series(df.country_name.unique())
        .sort_values(ascending=False)
    )
    return result

def get_cuisines(df):
    result = (
        pd.Series(df.cuisines.unique())
        .sort_values(ascending=False)
    )
    return result

def country_name(country_id):
    return COUNTRIES[country_id]

def create_price_type(price_range):
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"

def color_name(color_code):
    return COLORS[color_code]

def rating_name(color_code):
    return RATING[color_code]

def rename_columns(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df
