import dash_mantine_components as dmc
from dash_iconify import DashIconify
import dash_bootstrap_components as dbc
from dash import html
import dash_gif_component as gif
from dash import dcc
import dash

premio_caja_rural = dmc.Card(
    children=[

        dmc.CardSection(
            html.Img(
                src=r'assets/image.jpg',
                height=300,
                width=500,
            )
        ),
        dmc.Group(
            [
                dmc.Text("Winner Award a I+D+I *******", weight=500),
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "Put here your description ******************************************************************************************************************************************************************************************************************************************************************************",
            size="sm",
            color="dimmed",
        ),
        html.Br(),
        html.A(
                dmc.Tooltip(
                    dmc.ThemeIcon(
                        DashIconify(
                            icon="ph:link-bold",
                            width=30,
                        ),
                        radius=30,
                        size=30,
                        variant="outline",
                        color="gray",
                    ),
                    label="Accede al Link",
                    position="center",
                ),
                href="https://***************",
                style={
                        'textAlign': 'center',
                    'Align':'center'
                    }
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 500},
)


video_lidar = dmc.Card(
    children=[

        dmc.CardSection(
            gif.GifPlayer(
                gif=r'assets/lidartrees.gif',
                autoplay=True,
                still=r'assets/image.jpg',
            )
        ),
        dmc.Group(
            [
                dmc.Text("Put here your title.................", weight=500),
                #dmc.Badge("On Sale", color="red", variant="light"),
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "Put here your description *****************************************************************************************************************************************************************************************************************************************************************************",
            size="sm",
            color="dimmed",
        ),
        html.Br(),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 500},
)


matricula_tfg = dmc.Card(
    children=[

        dmc.CardSection(
            gif.GifPlayer(
                gif=r'assets/lidartrees.gif',
                still=r'assets/image.jpg',
                autoplay=True,
            )
        ),
        dmc.Group(
            [
                dmc.Text("Put here your title...........................................", weight=500),
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "Put here your description *****************************************************************************************************************************************************************************************************************************************************************************",
            size="sm",
            color="dimmed",
        ),
        html.Br(),
        html.A(
                dmc.Tooltip(
                    dmc.ThemeIcon(
                        DashIconify(
                            icon="ph:link-bold",
                            width=30,
                        ),
                        radius=30,
                        size=30,
                        variant="outline",
                        color="gray",
                    ),
                    label="Accede al Link",
                    position="center",
                ),
                href="https://************",
                style={
                        'textAlign': 'center',
                    'Align':'center'
                    }
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 500},
)



matricula_tfm = dmc.Card(
    children=[

        dmc.CardSection(
            html.Img(
                src=r'assets/image.jpg',
                height=300,
                width=500,
            )
        ),
        dmc.Group(
            [
                dmc.Text("Put here your title.............................", weight=500),
                #dmc.Badge("On Sale", color="red", variant="light"),
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "Put here your description *****************************************************************************************************************************************************************************************************************************************************************************",
            size="sm",
            color="dimmed",
        ),
        html.Br(),
        html.A(
                dmc.Tooltip(
                    dmc.ThemeIcon(
                        DashIconify(
                            icon="ph:link-bold",
                            width=30,
                        ),
                        radius=30,
                        size=30,
                        variant="outline",
                        color="gray",
                    ),
                    label="Accede al Link",
                    position="center",
                ),
                href="https://**************",
                style={
                        'textAlign': 'center',
                    'Align':'center'
                    }
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 500},
)


carou_raster = dmc.Card(
    children=[

        dmc.CardSection(
        dbc.Carousel(
            items=[
                {"key": "1", "src": r"assets/image.jpg", "header":"Title1"},
                {"key": "2", "src": r"assets/image.jpg", "header":"Title2"},
                {"key": "3", "src": r"assets/image.jpg", "header":"Title3"},
            ],
            controls=True,
            indicators=True,
            interval=4000,
            )
        ),
        dmc.Group(
            [
                dmc.Text("Put here your title....................", weight=500),
                #dmc.Badge("On Sale", color="red", variant="light"),
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "Put here your description *****************************************************************************************************************************************************************************************************************************************************************************",
            size="sm",
            color="dimmed",
        ),
        html.Br(),
        html.A(
                dmc.Tooltip(
                    dmc.ThemeIcon(
                        DashIconify(
                            icon="ph:link-bold",
                            width=30,
                        ),
                        radius=30,
                        size=30,
                        variant="outline",
                        color="gray",
                    ),
                    label="Accede al Link",
                    position="center",
                ),
                href="https://*******",
                style={
                        'textAlign': 'center',
                    'Align':'center'
                    }
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 500},
)

micro_meteo = dmc.Card(
    children=[

        dmc.CardSection(
        dbc.Carousel(
            items=[
                {"key": "1", "src": r"assets/image.jpg"},
                {"key": "2", "src": r"assets/image.jpg"},
                {"key": "3", "src": r"assets/image.jpg"},
                {"key": "3", "src": r"assets/image.jpg"},
            ],
            controls=True,
            indicators=True,
            interval=4000,
            )
        ),
        dmc.Group(
            [
                dmc.Text("Put here your title....................................................", weight=500),
                #dmc.Badge("On Sale", color="red", variant="light"),
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "Put here your description *****************************************************************************************************************************************************************************************************************************************************************************",
            size="sm",
            color="dimmed",
        ),
        html.Br(),
        html.A(
                dmc.Tooltip(
                    dmc.ThemeIcon(
                        DashIconify(
                            icon="ph:link-bold",
                            width=30,
                        ),
                        radius=30,
                        size=30,
                        variant="outline",
                        color="gray",
                    ),
                    label="Accede al Link",
                    position="center",
                ),
                href="https://*************",
                style={
                        'textAlign': 'center',
                    'Align':'center'
                    }
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    style={"width": 500},
)

row_1 = dbc.Row(
    [
        dbc.Col(dbc.Card(premio_caja_rural), width="auto"),
        dbc.Col(dbc.Card(matricula_tfg), width="auto"),
        dbc.Col(dbc.Card(matricula_tfm), width="auto"),

    ],
    #className="mb-4",
)

row_2 = dbc.Row(
    [
        dbc.Col(dbc.Card(video_lidar), width="auto"),
        dbc.Col(dbc.Card(carou_raster), width="auto"),
        dbc.Col(dbc.Card(micro_meteo), width="auto"),
    ],
    #className="mb-4",
)



cards = html.Div([row_1, row_2])







