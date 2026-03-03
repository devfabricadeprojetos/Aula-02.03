import dash
from dash import html 
import pandas as pd
import plotly.express as px 
from config import saidaCSV

df = pd.read_csv(saidaCSV)
df = df.sort_values(by='Nota', ascending = True)

fig = px.bar(
    df,
    x = 'Nota',
    y = 'Titulo',
    orientation = 'h',
    labels = {'Nota':'Nota do Filme','titulo': 'Titulo do filme'},
    title = 'Notas dos Filmes'
)

app = dash.Dash()
app.layout = html.Div([
    html.H1("Grafico de notas dos filmes", style={'text-align':'center'}),
    html.Div([
        html.Iframe(
            srcDoc=fig.to_html(),
            width="100%"
            height="600px"
            style={'border':'none'}
        )
    ]), style={'padding':'15px'}
])

if__name__=='__main__':
    app.run(debug=True)