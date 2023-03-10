import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import dcc
from dash.dependencies import Input, Output
import dash_mantine_components as dmc
from dash_iconify import DashIconify



def create_inter_text(string):
    text = dmc.Text(
        [
            string,
        ],
        color="dimmed",
        size="sm",
    )
    return text

time_lines_estudios = dmc.Card([
    html.H3('Información Académica'),
    html.Br(),
    dmc.Timeline(
    active=5,
    bulletSize=15,
    lineWidth=3,
    children=[
        dmc.TimelineItem(
            title="2017 - Comienzo Ingeniería Agroalimentaria y del Medio Rural",
            children=[
                dmc.Text(
                    [
                        "Estudios de Ingeniero Agrónomo por la Universidad de Córdoba y la \t",
                        dmc.Anchor("ETSIAM", href="http://www.uco.es/etsiam/es/grados/gr-ing-agroalimentaria#informacion-general", size="sm"),

                    ],
                    color="dimmed",
                    size="sm",
                ),
                dmc.Text(
                    [
                        "Campus Universitario de Rabanales, Córdoba \t",
                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            title="2019 - Especialización en Explotaciones Agropecuarias",
            children=[
                dmc.Text(
                    [
                        "CEEA1:  Capacidad para conocer, comprender y utilizar los principios de:",
                    ],
                    color="dimmed",
                    size="sm",
                    weight=500,
                ),
                create_inter_text('- Tecnologías de la Producción Animal'),
                create_inter_text('- Anatomía y Fisiología animal'),
                create_inter_text('- Sistemas de producción, protección y explotación animal'),
                create_inter_text('- Genética y mejora animal'),

                dmc.Text(
                    [
                        "CEEA2:  Capacidad para conocer, comprender y utilizar los principios de:",
                    ],
                    color="dimmed",
                    size="sm",
                    weight=500,
                ),
                create_inter_text('- Tecnologías de la Producción Vegetal'),
                create_inter_text('- Protección de cultivos contra plagas y enfermedades'),
                create_inter_text('- Sistemas de producción, protección y explotación vegetal'),
                create_inter_text('- Genética y mejora vegetal'),

                dmc.Text(
                    [
                        "CEEA3:  Capacidad para conocer, comprender y utilizar los principios de:",
                    ],
                    color="dimmed",
                    size="sm",
                    weight=500,
                ),
                create_inter_text('- Ingeniería de las Explotaciones Agropecuarias'),
                create_inter_text('- Electrificación de explotaciones agropecuarias'),
                create_inter_text('- Maquinaria Agrícola, Construcciones agropecuarias e Instalaciones de bienestar animal'),
                create_inter_text('- Sistemas y tecnología del riego'),


            ],
        ),
        dmc.TimelineItem(
            title="2021 - Fin de Estudios de Grado",
            #lineVariant="dashed",
            children=[
                dmc.Text(
                    [
                        "TFG: Desarrollo de LiDAR terrestre para estimar parámetros biofísicos en olivar",
                        create_inter_text('Calificación Matrícula de Honor'),

                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            title="2021 - Comienzo Máster Ingeniería Agronómica",
            #lineVariant="dashed",
            children=[
                dmc.Text(
                    [
                        "Complementación de estudios de grado en la \t",
                        dmc.Anchor("ETSIAM-Master", href="http://www.uco.es/etsiam/es/grados/master-ing-agronomica", size="sm"),

                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            title="2023 - Fin Master Ingeniería Agronómica",
            #lineVariant="dashed",
            children=[
                dmc.Text(
                    [
                        "Titulación de Ingeniero Agrónomo \t",
                        create_inter_text('TFM: Modelo de corrección radiométrica de cámaras térmicas en UAV'),
                        create_inter_text('Calificación Matrícula de Honor'),

                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
                    title="2023 - Comienzo de programa de doctorado",
                    lineVariant="dashed",
                    children=[
                        dmc.Text(
                            [
                                "Tesis doctoral enfocada en riego y caracterización de patrones de almendro  \t",


                            ],
                            color="dimmed",
                            size="sm",
                        ),
                    ],
                ),
    ],
)
    ]
)

time_lines_profesional = dmc.Card([
    html.H3('Información Profesional'),
    html.Br(),
    dmc.Timeline(
    active=5,
    bulletSize=15,
    lineWidth=3,
    children=[
        dmc.TimelineItem(
            title="2018 - Servicio en sala en Bodegas Campos S.L",
            children=[
                dmc.Text(
                    [
                        "Mi primera experiencia profesional fue de camarero en celebraciones \t",
                        dmc.Anchor("Bodegas Campos S.L", href="https://bodegascampos.com/", size="sm"),

                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            title="2020 - Técnico Vendedor en Decathlon España S.A",
            children=[
                create_inter_text('Ventas en a sección de Naturaleza'),
            ],
        ),
        dmc.TimelineItem(
            title="2021 - Ingeniero Técnico Agrónomo en Instituto de Agricultura Sostenible (IAS), CSIC",
            #lineVariant="dashed",
            children=[
                dmc.Text(
                    [
                        "Contrato con cargo a proyecto en el proyecto",
                        dmc.Anchor(" STIMA2", href="https://www.youtube.com/watch?v=TbZgluRee6w", size="sm"),
                        create_inter_text('Riego inteligente de alta resolución en almendro'),
                        create_inter_text('Competencias:'),
                        create_inter_text('- Supervisión de ensayos de campo y realización de medidas'),
                        create_inter_text('- Desarrollo e integración de sensores en campo'),
                        create_inter_text('- Realización de vuelos UAV con cámaras termográficas, RGB y LiDAR'),
                        create_inter_text('- Procesado y análisis de datos'),
                        create_inter_text('- Diseño e impresión 3D'),

                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            title="2023 - Ingeniero Agrónomo en Instituto de Agricultura Sostenible (IAS), CSIC",
            #lineVariant="dashed",
            children=[
                dmc.Text(
                    [
                        "Continuación de la línea de investigación del proyecto STIMA2 \t",
                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
        ),
    ],
)
    ]
)


ring =  dmc.Card(
        [
        html.H3('Idiomas'),
        html.Br(),
        html.H5('Inglés'),
        html.Br(),
        dmc.RingProgress(
            id="ring-progress",
            sections=[{"value": 90, "color": "indigo"}],
            label=dmc.Center(dmc.Text("C1", color="indigo")),
                ),
        html.Br(),
        html.H5('Francés'),
        html.Br(),
        dmc.RingProgress(
            id="ring-progress",
            sections=[{"value": 30, "color": "green"}],
            label=dmc.Center(dmc.Text("B1", color="green")),
                ),
        ]
    ),

cursos_y_acreditaciones =  dmc.Card(
        [
        html.H3('Cursos y Acreditaciones'),
        html.Br(),
        dmc.List(
            icon=dmc.ThemeIcon(
                DashIconify(icon="radix-icons:check-circled", width=16),
                radius="xl",
                color="teal",
                size=24,
            ),
            size="l",
            spacing="sm",
            children=[
                dmc.ListItem("Permiso de conducir B "),
                dmc.ListItem("Remote sensing sources for soil moisture monitoring: scalling and assimilation in hydrological application"),
                dmc.ListItem("Análisis reproducibles y generación de informes con R y Rmarkdown"),
                dmc.ListItem("Piloto de Dron A1/A3 Open Subcategory"),
                dmc.ListItem("Piloto de Dron A2 Open Subcategory"),
                dmc.ListItem("Recurso Preventivo en Salidas de Campo. Prevención de Riesgos Laborales (CSIC)"),
                dmc.ListItem(
                    "Docencia en lenguaje de programación python enfocado al uso de datos agrícolas",
                    icon=dmc.ThemeIcon(
                        DashIconify(icon="radix-icons:pie-chart", width=16),
                        radius="xl",
                        color="blue",
                        size=24,
                    ),
                ),
            ],
        ),
        ]
    ),


row_1 = dbc.Row(
    [
        dbc.Col(time_lines_estudios, width="auto"),
        dbc.Col(time_lines_profesional, width="auto"),
        dbc.Col(ring, width='auto'),
        dbc.Col(cursos_y_acreditaciones, width="auto"),
    ],
    #className="mb-4",
    justify='center',
)

row_2 = dbc.Row(
    [
        dbc.Col(),
        dbc.Col(),
        dbc.Col(),
        dbc.Col(),

    ],
    #className="mb-4",
    justify='center',
)

row_3 = dbc.Row(
    [
        dbc.Col(),
        dbc.Col(),
        #dbc.Col(),
        #dbc.Col(),

    ],
    #className="mb-4",
    justify='center',
)



time_line = html.Div([row_1])