import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

from app.frontend.layouts import header
from app.frontend.layouts.layout_modelo import layout as layout_modelo

layout = html.Div([
    
    header.layout,

    header.get_menu(selected='Geral'),

    html.Div([

        html.P("Title Page 1",
               className='text-center font-weight-bold text-uppercase col-12 my-2'),

        dbc.Row([

            dcc.Graph(
                id='page_1_chart'                
            )           

        ], className="col-12 p-0 m-0 mb-2 row-eq-height"),

    ], className="col-12 m-0")

], className="", id='')
