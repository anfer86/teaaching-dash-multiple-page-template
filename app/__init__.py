# This Python file uses the following encoding: utf-8
from os import path
import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

import flask
from flask import Flask, request, send_from_directory

import setproctitle as stp

stp.setproctitle('app-name')


# Import dos layouts
from app.frontend.layouts import page_1
from app.frontend.layouts import page_2

from app.backend.callbacks import *
from app.server import app, server

# Describe the layout/ UI of the app
app.layout = html.Div([
    
    # We use this component to inicialize component for the first time
    dcc.Interval(id='interval-component', interval=1000,
                    n_intervals=0, max_intervals=0),

    # Url location
    dcc.Location(id="url", refresh=False),

    # Page content
    html.Div(id="page-content",
             className="page col-lg-8 col-md-8 col-sm-10 col-12")
],

    style={'font-family': 'Open Sans', 'font-size': '1.0rem'}

)

global_pathname = None

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    global global_pathname
    global_pathname = pathname 
    if pathname == "/":
        return page_1.layout
    if pathname.startswith("/page_1"):
        return page_1.layout    
    if pathname.startswith("/page_2"):
        return page_2.layout
    else:
        return page_1.layout


app.config.suppress_callback_exceptions = True
