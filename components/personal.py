import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import dash_mantine_components as dmc
from dash_iconify import DashIconify



acordion = dmc.Accordion(
    disableChevronRotation=True,
    children=[
        dmc.AccordionItem(
            [
                dmc.AccordionControl(
                    "Personal Data",
                    icon=DashIconify(
                        icon="tabler:user",
                        color=dmc.theme.DEFAULT_COLORS["blue"][6],
                        width=20,
                    ),
                ),
                dmc.AccordionPanel("Name: Rafael Orozco Morán"),
                dmc.AccordionPanel("Phone number: *********"),
                dmc.AccordionPanel("Birth date: **/**/****"),
                dmc.AccordionPanel("Birth Place: ****, Spain"),
            ],
            value="info",
        ),
        dmc.AccordionItem(
            [
                dmc.AccordionControl(
                    "Adress",
                    icon=DashIconify(
                        icon="tabler:map-pin",
                        color=dmc.theme.DEFAULT_COLORS["red"][6],
                        width=20,
                    ),
                ),
                dmc.AccordionPanel("*****************"),
                dmc.AccordionPanel("**************"),
            ],
            value="addr",
        ),
        dmc.AccordionItem(
            [
                dmc.AccordionControl(
                    "Contact",
                    icon=DashIconify(
                        icon="mdi:email-variant",
                        color=dmc.theme.DEFAULT_COLORS["green"][6],
                        width=20,
                    ),
                ),
                dmc.AccordionPanel("e-mail1: *****@gmail.com"),
                dmc.AccordionPanel("e-mail2: *****@****.es"),
            ],
            value="focus",
        ),
    ],
)


personal_carou = dbc.Carousel(
            items=[
                {"key": "1", "src": r"assets/image.jpg"},
                {"key": "2", "src": r"assets/image.jpg"},
                #{"key": "3", "src": r"assets/rafa_tana_p.jpg"},
                #{"key": "3", "src": r"assets/recoleccion_alm_2_p.jpg"},
            ],
            controls=True,
            indicators=True,
            interval=6000,

            )

row_1 = dbc.Row(
    [
        dbc.Col(personal_carou),
    ],

)

row_2 = dbc.Row(
    [
        dbc.Col(acordion),
    ],

)



cards_pers = html.Div([row_1, row_2])

