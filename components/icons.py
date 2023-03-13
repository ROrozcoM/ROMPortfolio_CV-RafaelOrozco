import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import dash_mantine_components as dmc

from dash_iconify import DashIconify




twitter = dmc.Group(
                    position="center",
                    align="center",
                    spacing="xl",
                    children=[
                        html.A(
                            dmc.Tooltip(
                                dmc.ThemeIcon(
                                    DashIconify(
                                        icon="logos:twitter",
                                        width=80,
                                    ),
                                    radius=100,
                                    size=100,
                                    variant="outline",
                                    color="gray",
                                ),
                                label="Follow Me!",
                                position="bottom",
                            ),
                            href="https://twitter.com/rafozco20",
                        ),

                    ],
                )

github = dmc.Group(
                    position="center",
                    align="center",
                    spacing="xl",
                    children=[
                        html.A(
                            dmc.Tooltip(
                                dmc.ThemeIcon(
                                    DashIconify(
                                        icon="mdi:github",
                                        width=80,
                                    ),
                                    radius=100,
                                    size=100,
                                    variant="outline",
                                    color="gray",
                                ),
                                label="See Profile",
                                position="bottom",
                            ),
                            href="https://github.com/ROrozcoM",
                        ),

                    ],
                )

linkedin = dmc.Group(
                    position="center",
                    align="center",
                    spacing="xl",
                    children=[
                        html.A(
                            dmc.Tooltip(
                                dmc.ThemeIcon(
                                    DashIconify(
                                        icon="skill-icons:linkedin",
                                        width=80,
                                    ),
                                    radius=100,
                                    size=100,
                                    variant="outline",
                                    color="gray",
                                ),
                                label="Follow Me!",
                                position="bottom",
                            ),
                            href="https://www.linkedin.com/in/rafael-orozco-mor%C3%A1n-882014177/",
                        ),

                    ],
                )