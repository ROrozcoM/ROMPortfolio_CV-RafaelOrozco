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
                src=r'assets/IMG_20230201_201520.jpg',
                #src='https://fundacioncajaruraldelsur.com/wp-content/uploads/2023/02/230201.-Acto-de-entrega-de-los-premios-Fundacion-Caja-Rural-del-Sur-1-min.jpg',
                #className='align-self-center',
                #withPlaceholder=True,
                #fit=True,
                #autoPlay=True,
                #muted=True,
                height=300,
                width=500,
            )
        ),
        dmc.Group(
            [
                dmc.Text("Ganador Premio a I+D+I de la Fundación Caja Rural del Sur [Proyecto STIMA2]", weight=500),
                #dmc.Badge("On Sale", color="red", variant="light"),
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "El Premio Ricardo López Crespo a Proyectos de I+D+i en el ámbito de la Actividad Agroalimentaria, concedido ex aequo a los proyectos “Stima2. Riego inteligente de alta resolución en el cultivo del almendro” y “Olive2Energy. Valorización energética dual del alpeorujo: biometanización avanzada y producción de carbones para baterías recargables sostenibles”, fueron recogidos por José Antonio Jiménez-Berni y José Ángel Siles, respectivamente.",
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
                href="https://fundacioncajaruraldelsur.com/entregados-los-xii-premios-ricardo-lopez-crespo-de-fundacion-caja-rural-del-sur/",
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
                still=r'assets/cova3.jpg',
            )
        ),
        dmc.Group(
            [
                dmc.Text("Aplicación del LiDAR aéreo sobre explotaciones hortofrutícolas", weight=500),
                #dmc.Badge("On Sale", color="red", variant="light"),
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "La tecnología LIDAR permite a los agricultores recopilar datos detallados de sus cultivos de una manera más rápida y precisa que los métodos tradicionales, lo que les permite tomar decisiones más informadas y efectivas sobre el manejo y cuidado de sus cultivos. Esta tecnología de vanguardia es una herramienta valiosa para cualquier agricultor que busque mejorar la eficiencia y la productividad de su plantación, y el video demuestra claramente cómo la tecnología LIDAR puede ayudar a los agricultores a tomar decisiones más informadas y efectivas para el cuidado de sus cultivos.",
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
                gif=r'assets/treescolor.gif',
                still=r'assets/cova3.jpg',
                autoplay=True,
            )
        ),
        dmc.Group(
            [
                dmc.Text("Matrícula de Honor en TFG: Estímación de parámetros biofísicos en olivares de alta densidad mediante uso de tecnología LiDAR", weight=500),
                #dmc.Badge("On Sale", color="red", variant="light"),
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "En este trabajo evalué la capacidad de la aplicación del láser escáner terrestre, LiDAR (sensor láser LMS400; Sick), para medir parámetros biofísicos en olivares de alta densidad. El sistema cuenta con un sistema de navegación GPS (RTKite GNSS) y una unidad de medición inercial de código abierto (Pixhawk PX4) integrados a través ROS (Sistema Operativo Robótico) con el fin de georreferenciar las mediciones",
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
                href="https://www.linkedin.com/feed/update/urn:li:activity:6792498381362143232/",
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
                src=r'assets/tribunal_tfm.jpeg',
                height=300,
                width=500,
            )
        ),
        dmc.Group(
            [
                dmc.Text("Matrícula de Honor en el TFM desarrollado: Metodología de calibración de cámaras infrarrojas térmicas sobre UAVs", weight=500),
                #dmc.Badge("On Sale", color="red", variant="light"),
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "En este trabajo presenté una metodología de calibración de imágenes térmicas que consta de un equipo hardware y un modelo en software para la corrección de las imágenes térmicas con el fin de usarlas en el ámbito agronómico",
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
                href="https://www.youtube.com/watch?v=TbZgluRee6w",
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
                {"key": "1", "src": r"assets/mapa_alturas.png", "header":"Mapa de alturas"},
                {"key": "2", "src": r"assets/mapa_IR.png", "header":"Mapa de temperaturas"},
                {"key": "3", "src": r"assets/mapa_RGB.png", "header":"Mapa RGB"},
            ],
            controls=True,
            indicators=True,
            interval=4000,
            )
        ),
        dmc.Group(
            [
                dmc.Text("Trabajos de teledección con UAV en la agricultura", weight=500),
                #dmc.Badge("On Sale", color="red", variant="light"),
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "Desd hace unos años, la teledetección en el sector agrícola se ha desarrollado notablemente. Una de las partes de mi trabajo es darle sentido a los datos que se pueden obtener de este tipo de sensores, trabajar con el agricultor y optimizar el uso de recursos en finca según sus necesidades.",
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
                href="https://www.youtube.com/watch?v=TbZgluRee6w",
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
                {"key": "1", "src": r"assets/estacionmeteo2.png"},
                {"key": "2", "src": r"assets/grafana.png"},
                {"key": "3", "src": r"assets/sensores_almodovar.png"},
                {"key": "3", "src": r"assets/logostima2.png"},
            ],
            controls=True,
            indicators=True,
            interval=4000,
            )
        ),
        dmc.Group(
            [
                dmc.Text("Micro-Meteorología a nivel de finca", weight=500),
                #dmc.Badge("On Sale", color="red", variant="light"),
            ],
            position="apart",
            mt="md",
            mb="xs",
        ),
        dmc.Text(
            "La información meteorológica precisa y en tiempo real es crucial para una amplia variedad de actividades agrícolas, como la irrigación, el monitoreo de enfermedades, el control de plagas, la predicción de rendimientos y la planificación de la cosecha.El potencial de las estaciones meteorológicas cost-effective en la micrometeorología es enorme. Estas estaciones proporcionan información meteorológica precisa y en tiempo real a los agricultores, lo que les permite tomar decisiones informadas sobre el manejo de sus cultivos.",
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
                href="https://www.youtube.com/watch?v=TbZgluRee6w",
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







