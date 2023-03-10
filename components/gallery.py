import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc
from dash import html
import dash_gif_component as gif


gallery_carousel = dmc.Card(
    children=[

        dmc.CardSection(
            dbc.Carousel(
        items=[
        {"key": "1", "src": "/assets/almen.gif"},
        {"key": "2", "src": "/assets/olive.gif"},
        {"key": "3", "src": "/assets/dron.gif"},
        {"key": "3", "src": "/assets/sensores_almodovar.png"},
        {"key": "3", "src": "/assets/logostima2.png"},
        {"key": "3", "src": "/assets/grupo.jpg"},
        {"key": "3", "src": "/assets/ensayo.jpg"},
        {"key": "3", "src": "/assets/ensayo2.jpg"},
        {"key": "3", "src": "/assets/ensayo3.jpg"},
    ],
    controls=True,
    indicators=True,
            )
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 500},
)