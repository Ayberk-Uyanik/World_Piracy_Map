# Import necessary libraries
from dash import html
import dash_bootstrap_components as dbc

# Define the navbar structure
def Navbar():
    layout = dbc.Row(
        [
            dbc.Col(
                html.Div ([
                    html.H1 ("Piracy Map of NW Indian Ocean between 1993-2020", 
                        className="text-center display-4",
                        style={
                            "font-size": "26px",  
                            "color": "black", 
                            "height":"25px", 
                            "letter-spacing":"0.4px"
                        }
                    )
                ]), width=4, sm=0, md=4, lg=8
            )
        ], 
        style={ 
            "background-color":"lightgray", 
            "justify-content":"space-between",  
            "padding":"10px 10px" 
        }, 
        align="center", 
        justify="evenly"
    )
    
    return layout