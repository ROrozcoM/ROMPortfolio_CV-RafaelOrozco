import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc
from dash import html
import dash_gif_component as gif
import dash_player


gallery_carousel = dmc.Card(
    children=[

        dmc.CardSection(
            dbc.Carousel(
        items=[
        {"key": "1", "src": "/assets/image.jpg"},
        {"key": "2", "src": "/assets/image.jpg"},
        {"key": "3", "src": "/assets/image.jpg"},
        {"key": "3", "src": "/assets/image.jpg"},
        #{"key": "3", "src": "/assets/image.jpg"},
        {"key": "3", "src": "/assets/image.jpg"},
        {"key": "3", "src": "/assets/image.jpg"},
        {"key": "3", "src": "/assets/image.jpg"},
        {"key": "3", "src": "/assets/image.jpg"},
    ],
    controls=True,
    indicators=True,
    interval=6000
            )
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    #style={"width": 500},
)

youvideo = dmc.Card(
    children = [dash_player.DashPlayer(id="player",
                        url="https://www.youtube.com/watch?v=TbZgluRee6w&t=1s",
                        controls=True,
                        )],
    withBorder=True,
    shadow="sm",
    radius="md",
)

