# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc

# Define the navbar structure
def Footer():
    layout = html.Div([
        dbc.Row([
            dbc.Col(
                dbc.Card([
                    dbc.CardBody([
                        html.H2("DEVELOPER INFO", 
                            className="text-center text-white display-4",
                            style={"font-size":"16px"}
                        ),

                        html.Hr(style={"color":"white"}),

                        html.H2(children=["Ayberk Uyanık"], 
                            style={"color":"white",
                                "font-size":"20px"
                            }, 
                            className="card-text display-4", 
                        ),

                        html.Label(
                            children=["Full-stack Developer",
                                    html.Br(),
                                    "Senior Data Geoscientist",
                                    html.Hr(),
                                    html.Div ([
                                        html.A (
                                            [
                                                html.Img(src="/assets/logos/linkedin_2.png", width=40, height=40)
                                            ], 
                                                href="https://www.linkedin.com/in/ayberkuyanik/", 
                                                target="blank", 
                                                style={
                                                    "text-decoration":"none", 
                                                    "color":"#fff", 
                                                    "font-weight":"normal"
                                                }
                                        ),
                                        html.A (
                                            [
                                                html.Img(src="/assets/logos/github.png", width=40, height=40)
                                            ], 
                                                href="https://github.com/Ayberk-Uyanik", 
                                                target="blank", 
                                                style={
                                                    "text-decoration":"none", 
                                                    "color":"#fff", 
                                                    "font-weight":"normal",
                                                    "margin-left":"1em"
                                                }
                                        ),
                                    ], 
                                    style={
                                        "align-items":"center",
                                        "justify-content":"space-between"
                                    }
                                    ),
                            ], 
                            style={"color":"white",
                                "font-size":"16px"
                            }, 
                            className="card-text display-4", 
                        )
                    ])
                ], outline=False, 
                className="card h-100 text-center p-3 mb-2 bg-dark border-0"),
                sm=10, md=6, xl=4
            )
        ], align="center", justify="evenly")
    ], className="bg-dark", style={"margin-top":"1em"})

    return layout


