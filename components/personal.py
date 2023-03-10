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
                    "Datos Personales",
                    icon=DashIconify(
                        icon="tabler:user",
                        color=dmc.theme.DEFAULT_COLORS["blue"][6],
                        width=20,
                    ),
                ),
                dmc.AccordionPanel("Nombre: Rafael Orozco Morán"),
                dmc.AccordionPanel("Teléfono: 676374405"),
                dmc.AccordionPanel("Fecha de nacimiento: 27/03/1997"),
                dmc.AccordionPanel("Lugar de nacimiento: Córdoba, España"),
            ],
            value="info",
        ),
        dmc.AccordionItem(
            [
                dmc.AccordionControl(
                    "Dirección",
                    icon=DashIconify(
                        icon="tabler:map-pin",
                        color=dmc.theme.DEFAULT_COLORS["red"][6],
                        width=20,
                    ),
                ),
                dmc.AccordionPanel("Calle Teruel N1, Córdoba, España"),
                dmc.AccordionPanel("CP: 14012"),
            ],
            value="addr",
        ),
        dmc.AccordionItem(
            [
                dmc.AccordionControl(
                    "Contacto",
                    icon=DashIconify(
                        icon="mdi:email-variant",
                        color=dmc.theme.DEFAULT_COLORS["green"][6],
                        width=20,
                    ),
                ),
                dmc.AccordionPanel("e-mail1: rafozco@gmail.com"),
                dmc.AccordionPanel("e-mail2: rorozco@ias.csic.es"),
            ],
            value="focus",
        ),
    ],
)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
imagen_personal = dmc.Card(
    children=[
        dmc.CardSection(
            html.Img(
                #src="data:image/jpeg;base64,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",
                src=r'assets/rafa_tana_cova2.png',
                height=400,
                #width=800,
                alt='image'
            )
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    #style={"width": 350},
)

logo_ias = dmc.Center(
    children=[
        dmc.Image(
            #src="data:image/png;base64,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",
            src="https://www.ias.csic.es/wp-content/uploads/2022/10/1._ias_vertical_color.1334570412.jpg",
            width=200
        )
    ]
)

logo_csic = dmc.Center(
    children=[
        dmc.Image(
            # src="data:image/png;base64,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",
            src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Logotipo_del_CSIC.svg/808px-Logotipo_del_CSIC.svg.png",
            width=400
        )
    ]
)


logo_etsiam = dmc.Center(
    children=[
        dmc.Image(
            src="http://www.uco.es/servicios/comunicacion/media/k2/items/cache/5550eaf92cfe1ab426699a95c6aed26a_XL.jpg",
            width=300
        )
    ]
)

personal_carou = dbc.Carousel(
            items=[
                {"key": "1", "src": r"assets/cova2.jpg"},
                {"key": "2", "src": r"assets/trio.jpg"},
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

        #dbc.Col(),
        #dbc.Col(),
    ],
    #className="mb-4",
)

row_2 = dbc.Row(
    [
        dbc.Col(acordion),
        #dbc.Col(dbc.Row([dbc.Col(logo_ias),dbc.Col(logo_csic),dbc.Col(logo_etsiam)])),
        #dbc.Col(),
        #dbc.Col(),

    ],
    #className="mb-4",
)



cards_pers = html.Div([row_1, row_2])

'''dbc.Col( html.Div('Ingeniero Agrónomo',
                          #style={'color': 'dark-gray', 'fontSize': 150,
                                 'font-family':'monospace',
                                 'text-align':'center',
                                 'text-shadow': '2px 2px gray'})),'''