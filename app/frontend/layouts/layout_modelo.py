import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

layout = [
    dbc.Row([

        html.Div([

            html.Div([
                "Painel de 2 Colunas"
            ], className="", style={'height': '200px'}),

        ], className="col-lg-2 bloco"),

        html.Div([
            html.Div([
                "Painel de 4 Colunas"
            ], className="", style={'height': '200px'}),
        ], className="col-lg-4 bloco"),

        html.Div([
            html.Div([
                "Painel de 6 Colunas"
            ], className="", style={'height': '200px'}),
        ], className="col-lg-6 bloco"),

        html.Div([
            html.Div([
                "Painel de 6 Colunas"
            ], className="", style={'height': '200px'}),
        ], className="col-lg-6 bloco"),

        html.Div([
            html.Div([
                "Painel de 6 Colunas"
            ], className="", style={'height': '200px'}),
        ], className="col-lg-6 bloco"),

        html.Div([
            html.Div([
                "Painel de 12 Colunas"
            ], className="", style={'height': '200px'}),
        ], className="col-lg-12 bloco"),

    ], className="m-2")
]
