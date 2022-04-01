# Dash app initialization
import dash
import dash_bootstrap_components as dbc

# User management initialization
import os

app = dash.Dash(
    __name__,
    title='Project Name',
    meta_tags=[
        {
            'charset': 'utf-8',
        },
        {
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1, shrink-to-fit=no'
        }
    ],
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,        
    ],

    external_scripts=[
        'https://code.jquery.com/jquery-3.5.1.js'
    ]
)


server = app.server
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
