import dash
from dash import html, dcc, Output, Input, callback
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

dataSkills=dict(data=[go.Scatterpolar(
                          r = [45, 30, 35, 40, 50, 48, 45],
                          theta = ['Pandas', 'Machine Learning', 'Statistics  ', 'Excel', 'SIG - QGIS',  'Geoespacial', 'Pandas'],
                          fill = 'toself',
                          line = dict(color='salmon'),
                          hoverinfo='none'
                                            )
                           ],

              layout= go.Layout(xaxis=dict(visible=False),
                                yaxis=dict(visible=False),
                                font=dict(size=14),
                                polar = dict(
                                            radialaxis = dict(
                                                              visible = True,
                                                              range = [0, 50],
                                                              tickvals=[15,25,35],
                                                              ticktext=['Basic','Intermediate','Advanced'],
                                                              tickmode='array',
                                                              tickangle=25,
                                                              tickfont=dict(
                                                                    family='Arial',
                                                                    size=13,
                                                                    color='#acb3bf'
                                                                            )
                                                                )
                                              ),
                                showlegend = False,
                                height=600,
                                width=600
                                )
             )

codeSkills=dict(data=[go.Scatterpolar(
                          r = [39, 30, 20, 15, 35, 28, 39],
                          theta = ['Python','Git', 'HTML', 'JavaScript',  '  Google <br>Sheets API', 'Docker', 'Python'],
                          fill = 'toself',
                          line = dict(color='paleturquoise'),
                          hoverinfo='none'
                                            )
                           ],

              layout= go.Layout(xaxis=dict(visible=False),
                                yaxis=dict(visible=False),
                                font=dict(size=14),
                                polar = dict(
                                            radialaxis = dict(
                                                              visible = True,
                                                              range = [0, 50],
                                                              tickvals=[15,25,35],
                                                              ticktext=['Basic','Intermediate','Advanced'],
                                                              tickmode='array',
                                                              tickangle=25,
                                                              tickfont=dict(
                                                                    family='Arial',
                                                                    size=13,
                                                                    color='#acb3bf'
                                                                            )
                                                                )
                                              ),
                                showlegend = False,
                                height=600,
                                width=600
                                )
             )

bizSkills=dict(data=[go.Scatterpolar(
                          r = [35, 38, 25, 20, 28, 39, 35, 35],
                          theta = ['Sales', '   Negotiation', 'Marketing', 'Finance  ', 'Economics   ', 'Project <br>Management', '<br> Presentation', 'Sales'],
                          fill = 'toself',
                          line = dict(color='goldenrod'),
                          hoverinfo='none'
                                            )
                           ],

              layout= go.Layout(xaxis=dict(visible=False),
                                yaxis=dict(visible=False),
                                font=dict(size=14),
                                polar = dict(
                                            radialaxis = dict(
                                                              visible = True,
                                                              range = [0, 50],
                                                              tickvals=[15,25,35],
                                                              ticktext=['Basic','Intermediate','Advanced'],
                                                              tickmode='array',
                                                              tickangle=25,
                                                              tickfont=dict(
                                                                    family='Arial',
                                                                    size=13,
                                                                    color='#acb3bf'
                                                                            )
                                                                )
                                              ),
                                showlegend = False,
                                height=600,
                                width=600
                                )
             )

langSkills=dict(data=[go.Scatterpolar(
                          r = [39, 38, 30, 20, 15, 39],
                          theta = ['Portuguese','English','Spanish', 'German', 'French', 'Portuguese'],
                          fill = 'toself',
                          line = dict(color='lightskyblue'),
                          hoverinfo='none'
                                            )
                           ],

              layout= go.Layout(xaxis=dict(visible=False),
                                yaxis=dict(visible=False),
                                font=dict(size=14),
                                polar = dict(
                                            radialaxis = dict(
                                                              visible = True,
                                                              range = [0, 50],
                                                              tickvals=[15,25,35],
                                                              ticktext=['Basic','Intermediate','Advanced'],
                                                              tickmode='array',
                                                              tickangle=25,
                                                              tickfont=dict(
                                                                    family='Arial',
                                                                    size=13,
                                                                    color='#acb3bf'
                                                                            )
                                                                )
                                              ),
                                showlegend = False,
                                height=700,
                                width=700
                                )
             )



grafico_code=dcc.Graph(id='my-skills',
                                         figure=codeSkills,
                                         config=dict(displayModeBar=False)
                                        )
skills_code = html.Div([html.Div([
                                dcc.Graph(id='my-skills',
                                         figure=codeSkills,
                                         config=dict(displayModeBar=False)
                                        )
                                 ],
                                    className='col-8')
                            ], className='row mx-auto justify-content-center'
                    )


grafico_data = dcc.Graph(id='my-skills',
                                         figure=dataSkills,
                                         config=dict(displayModeBar=False)
                                        )
skills_data = html.Div([html.Div([
                                dcc.Graph(id='my-skills',
                                         figure=dataSkills,
                                         config=dict(displayModeBar=False)
                                        )
                                 ],
                                    className='col-8')
                            ], className='row mx-auto justify-content-center'
                    )
grafico_habilidades = dcc.Graph(id='my-skills',
                                         figure=bizSkills,
                                         config=dict(displayModeBar=False)
                                        )
skills_lang = html.Div([html.Div([
                                dcc.Graph(id='my-skills',
                                         figure=bizSkills,
                                         config=dict(displayModeBar=False)
                                        )
                                 ],
                                    className='col-8')
                            ], className='row mx-auto justify-content-center'
                    )




row_1 = dbc.Row(
    [
        dbc.Col(dbc.Card(grafico_code,className="border-0 bg-transparent")),
        dbc.Col(dbc.Card(grafico_data, className="border-0 bg-transparent")),
        dbc.Col(dbc.Card(grafico_habilidades, className="border-0 bg-transparent")),
    ],
    align='left'
)

row_2 = dbc.Row(
    [
        dbc.Col(dbc.Card(grafico_data), width="auto",),
    ],
    align='left'
)
row_3 = dbc.Row(
    [
        dbc.Col(dbc.Card(grafico_habilidades), width="auto"),
    ],
    #className="mb-4",
    align='left'
)

skills_grafico = html.Div([row_1])