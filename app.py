# Code source: https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import dcc
from dash.dependencies import Input, Output
from components.cards import cards
from components.icons import twitter, instagram, linkedin
from components.personal import acordion, cards_pers
from components.experiencia import time_line
from components.skills import skills_grafico
from components.gallery import gallery_carousel

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                             'content': 'width=device-width, initial-scale=0, maximum-scale=1.2, minimum-scale=0.5,'}]
                )


# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "10rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "10rem",
    "margin-right": "0rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Rafael Orozco Morán"),
        html.Hr(),
        html.P(
            "Conoce un poco más sobre mí", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Información General", href="/", active="exact"),
                dbc.NavLink("Experiencia", href="/page-1-experiencia", active="exact"),
                dbc.NavLink("Habilidades", href="/page-2-habilidades", active="exact"),
                dbc.NavLink("Proyectos y Reconocimientos", href="/page-3-misproyectos", active="exact"),
                dbc.NavLink("Galería", href="/page-4-gallery", active="exact"),
                html.Br(),
                html.Br(),
                linkedin,
                html.Br(),
                instagram,
                html.Br(),
                twitter,

            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    #header,
    dcc.Location(id="url"),
    sidebar,
    content
])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [
                html.H1('Información Personal',
                        style={'textAlign':'center'}),
                html.Br(),
                html.Br(),
                html.Br(),

                cards_pers

                ]
    elif pathname == "/page-1-experiencia":
        return [
                html.H1('Estudios y Experiencia profesional',
                        style={'textAlign':'center'}),
                html.Br(),
                html.Br(),
                time_line

                ]
    elif pathname == "/page-2-habilidades":
        return [
                html.H1('Habilidades destacadas',
                        style={'textAlign':'center'}),
                html.Br(),
                html.H3('Lenguajes de Programación'),
                html.Br(),
                skills_grafico
                ]
    elif pathname == "/page-3-misproyectos":
        return [
                html.H1('Proyectos y Premios',
                        style={'textAlign':'center'}),
                cards
                ]
    elif pathname == "/page-4-gallery":
        return [
                html.H1('Galería',
                        style={'textAlign':'center'}),
                gallery_carousel
                ]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )



if __name__ == '__main__':
    app.run_server(debug=False, host="0.0.0.0", port=8080)