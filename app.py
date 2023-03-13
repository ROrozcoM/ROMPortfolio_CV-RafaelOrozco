# Code source: https://dash-bootstrap-components.opensource.faculty.ai/examples/simple-sidebar/
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import dcc
from dash.dependencies import Input, Output
from components.cards import cards
from components.icons import twitter, github, linkedin
from components.personal import acordion, cards_pers
from components.experience import time_line
from components.skills import skills_grafico
from components.gallery import gallery_carousel, youvideo
from components.map import map_card

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
            "Learn more about me", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("General Information", href="/", active="exact"),
                dbc.NavLink("Experience", href="/page-1-experience", active="exact"),
                dbc.NavLink("Skills", href="/page-2-skills", active="exact"),
                dbc.NavLink("Projects and Awards", href="/page-3-myprojects", active="exact"),
                dbc.NavLink("Gallery", href="/page-4-gallery", active="exact"),
                html.Br(),
                html.Br(),
                linkedin,
                html.Br(),
                github,
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
                html.H1('Personal Information',
                        style={'textAlign':'center'}),
                html.Br(),
                html.Br(),
                html.Br(),

                cards_pers

                ]
    elif pathname == "/page-1-experience":
        return [
                html.H1('Studies and Professional experience',
                        style={'textAlign':'center'}),
                html.Br(),
                html.Br(),
                time_line

                ]
    elif pathname == "/page-2-skills":
        return [
                html.H1('Featured skills',
                        style={'textAlign':'center'}),
                html.Br(),
                html.Br(),
                skills_grafico
                ]
    elif pathname == "/page-3-myprojects":
        return [
                html.H1('Projects and Awards',
                        style={'textAlign':'center'}),
                cards
                ]
    elif pathname == "/page-4-gallery":
        return [
                html.H1('Gallery',
                        style={'textAlign':'center'}),
                youvideo,
                html.Br(),
                html.Br(),
                gallery_carousel,
                html.Br(),
                html.Br(),
                html.H3('Placed where I worked in', style={'textAlign':'center'}),
                map_card
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