# Import necessary libraries 
from dash import html, dcc
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app

# Connect to your app pages
from pages import Global_Outlook2

# Connect the navbar to the index
from components import navbar, footer

# Importing and Assigning Navbar and Footer #
nav = navbar.Navbar()
footer_content = footer.Footer()

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
    ]
              
)
    
def display_page(pathname):
    if pathname == "/pages/Global_Outlook2/":
        return Global_Outlook2.layout
    else: 
        return "404 Page Error!"

# Run the app 
if __name__ == '__main__':
    app.run_server(
        debug=False,
        port="8080"
    )
