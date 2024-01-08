#%%
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import numpy as np

df = pd.read_excel('../data/field_production_gross_monthly.xlsx')
df['Year2']=df['Year']+df['Month']/12
app = Dash(__name__)

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    dcc.Dropdown(np.unique(df[df.columns[0]]), 'DRAUGEN', id='dropdown-selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df[df.columns[0]]==value]
    return px.line(dff, x='Year2', y='Gross - oil equivalents \n[mill Sm3]')

if __name__ == '__main__':
    app.run(debug=True)
# %%
