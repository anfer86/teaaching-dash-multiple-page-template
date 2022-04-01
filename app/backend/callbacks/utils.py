import pandas as pd
import plotly.express as px
import plotly.io as pio


# ---------------------------------------------------
# Functions used in many callback files, like
# common preprocess functions, create or access 
# datasets or plots
# --------------------------------------------------
def function_name():    
    return None

pio.templates.default = "simple_white"

def create_simple_plot():
    '''
    from https://dash.plotly.com/layout
    '''


    colors = {
        'background': '#111111',
        'text': '#7FDBFF'
    }

    # assume you have a "long-form" data frame
    # see https://plotly.com/python/px-arguments/ for more options
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )

    return fig
   
