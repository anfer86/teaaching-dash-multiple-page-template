import numpy as np
import pandas as pd

from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go

from app.server import app

from app.backend.callbacks.utils import *

@app.callback(
    Output('page_1_chart', 'figure'),
    [Input('interval-component', 'n_intervals')])

def update_table(value):

    figure = create_simple_plot()
    
    return figure