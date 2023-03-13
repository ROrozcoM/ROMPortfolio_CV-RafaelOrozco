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
    html.H3('Academic Information'),
    html.Br(),
    dmc.Timeline(
    active=5,
    bulletSize=15,
    lineWidth=3,
    children=[
        dmc.TimelineItem(
            title="2017 - Start Ingeniería Agroalimentaria y del Medio Rural",
            children=[
                dmc.Text(
                    [
                        "Studies in Agricultural Engineering at the University of Córdoba and",
                        dmc.Anchor("ETSIAM", href="http://www.uco.es/etsiam/es/grados/gr-ing-agroalimentaria#informacion-general", size="sm"),

                    ],
                    color="dimmed",
                    size="sm",
                ),
                dmc.Text(
                    [
                        "Rabanales University Campus, Córdoba",
                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            title="2019 - Specialization in Agricultural Operations",
            children=[
                dmc.Text(
                    [
                        "CEEA1:  Ability to know, understand and use the principles of:",
                    ],
                    color="dimmed",
                    size="sm",
                    weight=500,
                ),
                create_inter_text('- Animal Production Technologies'),
                create_inter_text('- Animal Anatomy and Physiology'),
                create_inter_text('- Animal production, protection and exploitation systems'),
                create_inter_text('- Genetics and animal improvement'),

                dmc.Text(
                    [
                        "CEEA2:  Ability to know, understand and use the principles of:",
                    ],
                    color="dimmed",
                    size="sm",
                    weight=500,
                ),
                create_inter_text('- Vegetable Production Technologies'),
                create_inter_text('- Crop protection against pests and diseases'),
                create_inter_text('- Plant production, protection and exploitation systems'),
                create_inter_text('- Genetics and plant improvement'),

                dmc.Text(
                    [
                        "CEEA3:  Ability to know, understand and use the principles of:",
                    ],
                    color="dimmed",
                    size="sm",
                    weight=500,
                ),
                create_inter_text('- Farm Engineering'),
                create_inter_text('- Electrification of agricultural exploitations'),
                create_inter_text('- Agricultural machinery, agricultural buildings and animal welfare facilities'),
                create_inter_text('- Systems and technology irrigation'),


            ],
        ),
        dmc.TimelineItem(
            title="2021 - End of Degree Studies",
            #lineVariant="dashed",
            children=[
                dmc.Text(
                    [
                        "TFG: Development of terrestrial LiDAR to estimate biophysical parameters in olive groves",
                        create_inter_text('Honors Qualification'),

                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            title="2021 - Beginning of the Master's Degree in Agronomic Engineering",
            #lineVariant="dashed",
            children=[
                dmc.Text(
                    [
                        "Complementation of degree studies at",
                        dmc.Anchor("ETSIAM-Master", href="http://www.uco.es/etsiam/es/grados/master-ing-agronomica", size="sm"),

                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            title="2023 - End Master Agronomic Engineering",
            #lineVariant="dashed",
            children=[
                dmc.Text(
                    [
                        "Agricultural Engineer Oficial Superior \t",
                        create_inter_text('TFM: Radiometric correction model of thermal cameras in UAVs'),
                        create_inter_text('Honors Qualification'),

                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
                    title="2023 - Start of doctoral program",
                    lineVariant="dashed",
                    children=[
                        dmc.Text(
                            [
                                "Doctoral thesis focused on irrigation and characterization of almond patterns  \t",


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
    html.H3('Professional Information'),
    html.Br(),
    dmc.Timeline(
    active=5,
    bulletSize=15,
    lineWidth=3,
    children=[
        dmc.TimelineItem(
            title="2018 - **********************",
            children=[
                dmc.Text(
                    [
                        "******************** \t",
                        dmc.Anchor("*************", href="*****************", size="sm"),

                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            title="2020 - ********************",
            children=[
                create_inter_text('*******************'),
            ],
        ),
        dmc.TimelineItem(
            title="2021 - *********************",
            #lineVariant="dashed",
            children=[
                dmc.Text(
                    [
                        "*****************",
                        dmc.Anchor(" STIMA2", href="https://www.youtube.com/watch?v=TbZgluRee6w", size="sm"),
                        create_inter_text('***************'),
                        create_inter_text('****************'),
                        create_inter_text('- ****************'),
                        create_inter_text('- **************'),
                        create_inter_text('- **************'),
                        create_inter_text('- ****************'),
                        create_inter_text('- ****************'),

                    ],
                    color="dimmed",
                    size="sm",
                ),
            ],
        ),
        dmc.TimelineItem(
            title="2023 - Agronomist Technical Engineer at Agricultura Sostenible (IAS), CSIC",
            #lineVariant="dashed",
            children=[
                dmc.Text(
                    [
                        "***** \t",
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
        html.H3('Idioms'),
        html.Br(),
        html.H5('English'),
        html.Br(),
        dmc.RingProgress(
            id="ring-progress",
            sections=[{"value": 90, "color": "indigo"}],
            label=dmc.Center(dmc.Text("C1", color="indigo")),
                ),
        html.Br(),
        html.H5('French'),
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
        html.H3('Courses and Accreditations'),
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
                dmc.ListItem("************* "),
                dmc.ListItem("*************"),
                dmc.ListItem("**************"),
                dmc.ListItem("*************"),
                dmc.ListItem("*************"),
                dmc.ListItem("*************"),
                dmc.ListItem(
                    "**********************",
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