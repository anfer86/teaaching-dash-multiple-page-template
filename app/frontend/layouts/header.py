import dash_bootstrap_components as dbc
from dash import dcc
from dash import html

from app.server import app

link_list = ["Page 1", "Page 2", "Page 3a", "Page 3b"]

def get_link_dict():
    link_dict = {        
        x : html.A(
            x,
            href="/"+x.replace(" ","_").lower(),
            className='btn p-0 m-0'
        ) for x in link_list
    }
    return link_dict

'''
You can build your link dict manually



        'Extrato Indicadores':
        html.A(
            "Extrato",
            href="/extrato_indicadores",
            className='btn p-0 m-0'
        ),


def get_link_dict():
    link_dict = { 

        'Page 1': html.A(
            "Page 1",
            href="/page_1",
            className='btn p-0 m-0'
        ),    

        'Page 2': html.A(
            "Page 2",
            href="/page_2",
            className='btn p-0 m-0'
        ),    
    }

    return link_dict
'''

def get_menu(selected=None):

    link_dict = get_link_dict()

    if (selected is not None):
        if (selected in link_dict):
            pass            
    
    menu = dbc.Row(
        [
            dbc.Button(
                link_dict['Page 1'],
                className="btn btn-light btn-sm col-sm-3 col-6"
            ),

            dbc.Button(
                link_dict['Page 2'],
                className="btn btn-light btn-sm col-sm-3 col-6"
            ),

            dbc.DropdownMenu([
                dbc.DropdownMenuItem(link_dict['Page 3a']),
                dbc.DropdownMenuItem(link_dict['Page 3b']),                
            ],
                label="Page 3",
                group=True, toggleClassName="btn btn-light btn-sm col-12 ",
                className="px-0 mx-0 col-sm-3 col-6"
            ),

        ],

        className='my-1 col-12 px-1 mx-0'
    )

    return menu


layout = dbc.Navbar(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.P(["Título da aplicação ",html.Br(),"(em desenvolvimento)" ],
                           className="font-weight-bold my-1 text-center"),
                    className="", align="center"),

                dbc.Col([
                    html.P('Desenvolvido por', className="col-12 text-center font-weight-bold p-0 m-0", style={'font-size' : '10px'}),
                    html.Img(src='assets/logo_ifsc.png', className="mx-3", height="40px"),                    
                    ], className="col-12 col-sm-auto ml-auto"),
                
            ],
            align="left",
            className="col-12 p-0 d-flex justify-content-end"),

    ],
    className='p-1',
    color="light",
    light=True,
)
