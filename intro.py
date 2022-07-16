import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# --------------------------------------------------------
#Import data
df = pd.read_csv("passengers_data.csv")

# --------------------------------------------------------
# App layout
app.layout = html.Div([
    html.H1("Demanda de Pasajeros", style={"text-align": "center"}),
    dcc.Dropdown(id="")
])