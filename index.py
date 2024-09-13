# Import necessary libraries 
from dash import html, dcc
from dash.dependencies import Input, Output
from dash import Dash
import dash_bootstrap_components as dbc

# Connect to your app pages
from pages import Global_Outlook2

# Connect the navbar to the index
from components import navbar, footer

# Multi Page Configuration #
# App styling codes #
bootstrap = dbc.themes.BOOTSTRAP
bootstrap_icons = dbc.icons.BOOTSTRAP
local_css = "/assets/styles/styles.css"

# Importing and Assigning Navbar and Footer #
nav = navbar.Navbar()
footer_content = footer.Footer()

# App Initiation #
app = Dash(__name__, 
           external_scripts=["https://cdn.plot.ly/plotly-2.18.2.min.js", 
                            "https://raw.githack.com/eKoopmans/html2pdf/master/dist/html2pdf.bundle.js"
            ], 
            external_stylesheets=[
               bootstrap, 
               bootstrap_icons,
               local_css
            ], 
           meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
           suppress_callback_exceptions = True
)

server = app.server

app.title = "World Piracy Map"

# Define the index page layout
app.layout = html.Div([
    dcc.Location(
        id="url", 
        refresh=False,
        pathname="/pages/Global_Outlook2/"
    ),

    nav,

    html.Div(
        id="page-content", 
        children=[]
    ),

    footer_content
])

# Create the callback to handle mutlipage inputs
@app.callback(
    Output("page-content", "children"),
    [
        Input("url", "pathname")
    ],
    prevent_initial_call=False
)
    
def display_page(pathname):
    if pathname == "/pages/Global_Outlook2/":
        return Global_Outlook2.layout
    else: 
        return "404 Page Error!"

# Run the app 
if __name__ == '__main__':
    app.run_server(
        debug=False
    )
