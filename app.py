from dash import Dash
import dash_bootstrap_components as dbc

# Multi Page Configuration #
# App styling codes #
bootstrap = dbc.themes.BOOTSTRAP
bootstrap_icons = dbc.icons.BOOTSTRAP
local_css = "/assets/styles/styles.css"

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
           use_pages=True,  
           meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
           suppress_callback_exceptions = True,
           url_base_pathname="/pages/Global_Outlook2/"
)

server = app.server

app.title = "World Piracy Map"
