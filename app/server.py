# Dash app initialization
import dash
import dash_bootstrap_components as dbc

# User management initialization
import os

app = dash.Dash(
    __name__,
    title='IFSC COVID-19',
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
        # "https://cdn.datatables.net/1.10.22/css/dataTables.bootstrap4.min.css"
    ],

    external_scripts=[
        'https://code.jquery.com/jquery-3.5.1.js',
        # "https://cdn.datatables.net/1.10.21/js/jquery.dataTables.min.js",
        # "https://cdn.datatables.net/1.10.21/js/dataTables.bootstrap4.min.js",
    ]
)


server = app.server
#app.config.suppress_callback_exceptions = False
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
