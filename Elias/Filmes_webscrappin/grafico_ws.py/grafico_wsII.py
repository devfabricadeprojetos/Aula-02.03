import dash
from dash import html 
import pandas as pd
import plotly.express as px 
# Certifique-se de que o arquivo config.py existe no mesmo diretório
from config import saidaCSV

# Carregamento e tratamento de dados
df = pd.read_csv(saidaCSV)
df = df.sort_values(by='Nota', ascending=True)

# Criação do gráfico
fig = px.bar(
    df,
    x='Nota',
    y='Titulo',
    orientation='h',
    labels={'Nota': 'Nota do Filme', 'Titulo': 'Título do Filme'}, # Corrigido 'titulo' para 'Titulo'
    title='Notas dos Filmes'
)

# Inicialização do App
app = dash.Dash(__name__) # Recomendado passar __name__

app.layout = html.Div(style={'padding': '15px'}, children=[
    html.H1("Gráfico de notas dos filmes", style={'text-align': 'center'}),
    html.Div([
        html.Iframe(
            srcDoc=fig.to_html(),
            width="100%",        # Adicionada vírgula esquecida
            height="600px",      # Adicionada vírgula esquecida
            style={'border': 'none'}
        )
    ])
]) # Fechamento do layout corrigido

# Execução do servidor
if __name__ == '__main__': # Adicionado espaços e corrigido underline
    app.run_server(debug=True)