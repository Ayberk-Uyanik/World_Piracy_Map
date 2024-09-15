# Importing Necessary Libraries #
from dash import html, dcc, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_chart_editor as dce
import dash_ag_grid as dag
import json
import dash_leaflet as dl
from utils import database
import pandas as pd

# # Importing Pirate Attacks and Key Ports Data Set #
piracy_data = database.get_pirate_attacks()
piracy_data.insert(0, "Index", piracy_data.index+1)

# Map Tiles #
satelite_map = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}'
satelite_attribution = 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'

openstreet_map = 'https://tile.openstreetmap.org/{z}/{x}/{y}.png'
openstreet_attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'

nat_geo_map = 'https://server.arcgisonline.com/ArcGIS/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}'
nat_geo_attribution = 'Tiles &copy; Esri &mdash; National Geographic, Esri, DeLorme, NAVTEQ, UNEP-WCMC, USGS, NASA, ESA, METI, NRCAN, GEBCO, NOAA, iPC'

dark_mode_map = 'https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png'
dark_mode_attribution = '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>'

relief_map = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Shaded_Relief/MapServer/tile/{z}/{y}/{x}'
relief_attribution = 'Tiles &copy; Esri &mdash; Source: Esri'

physical_map = 'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png'
physical_attribution = 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'

# GeoJSON Files Including Country Borders for Turkey and TPAO'S Abroad Operations #
with open(r"assets/geojson/Shipping_Lanes.geojson") as shipping:
  shipping_lanes_json = json.load(shipping)

with open(r"assets/geojson/EEZ_Boundaries_JSON.json") as eez:
  eez_boundaries_json = json.load(eez)

# App Layout #
def display_main_content:
  layout = html.Div ([ 
          dbc.Row([
              dbc.Col(
                  html.Div([
                      html.H4([
                         "Disclaimer"
                      ]),
  
                      html.P([
                         "This dashboard displays the piracy data at the NW Indian Ocean between 1993-2020.", 
                         html.Br(),
                         "The data is published in 2021, by researchers from the University of Canterbury, New Zealand.",
                         html.Br(),
                         "The developer does not accept any responsibility or liability regarding the accuracy and usage of the data provided in this dashboard."
                      ]),
  
                      html.Hr(),
  
                      html.H4([
                         "Reference"
                      ]),
  
                      html.P([
                         "Benden, P., Feng, A., Howell, C., & Dalla Riva G. V. (2021). Crime at Sea: A Global Database of Maritime Pirate Attacks (1993–2020). Journal of Open Humanities Data, 7: 19, pp. 1–6. DOI: https://doi.org/10.5334/johd.39",
                         html.Br(),
                         "The attack icons on the map view are from icons8.com",
                      ]),
  
                      html.Hr(),
  
                      html.H4([
                         "Chart Generation"
                      ]),
  
                      dbc.Button(
                          "Generate Graph",
                          id="generate_graphs_for_piracy_data",
                          n_clicks=0,
                          color="dark", 
                          style={
                              "margin-top":"2em"
                          }
                      ),
  
                      dbc.Offcanvas(
                          html.Div([
                              dce.DashChartEditor(dataSources=piracy_data.to_dict("list"), 
                                                  style={"border":"0.1px solid lightgray", "padding":"10px 10px", "margin-top":"2em"})
                          ]),
                          id="piracy_data_chart_editor",
                          scrollable=True,
                          title="Chart Generation Module for Piracy Data of NW Indian Ocean between 1993-2020",
                          is_open=False,
                          placement="top",
                          style={"height":"700px"}
                      ),
                  ], style={
                      "background-color":"#f8f9fa",
                      "padding": "2em 2em",
                      "border":"0.2px solid gray"
                  }
                  ), sm=6, md=6, lg=4
              ),   
          
              dbc.Col(
                  html.Div([
                      dl.Map(
                          [
                              dl.LayersControl([
                                  dl.BaseLayer(
                                          dl.TileLayer(url=openstreet_map,
                                              attribution=openstreet_attribution
                                          ),
                                          name="Open Street",                       
                                  ),
  
                                  dl.BaseLayer(
                                          dl.TileLayer(url=satelite_map,
                                              attribution=satelite_attribution
                                          ),
                                          name="Topographical Map",                        
                                  ),
  
                                  dl.BaseLayer(
                                          dl.TileLayer(url=nat_geo_map,
                                              attribution=nat_geo_attribution
                                          ),
                                          name="Nat Geo Map",
                                          checked="Nat Geo Map"                        
                                  ),
  
                                  dl.BaseLayer(
                                          dl.TileLayer(url=physical_map,
                                              attribution=physical_attribution
                                          ),
                                          name="Physical Map"                        
                                  ),
  
                                  dl.BaseLayer(
                                          dl.TileLayer(url=relief_map,
                                              attribution=relief_attribution
                                          ),
                                          name="Relief Map"                        
                                  ),
  
                                  dl.BaseLayer(
                                          dl.TileLayer(url=dark_mode_map,
                                              attribution=dark_mode_attribution
                                          ),
                                          name="Dark Mode"                        
                                  ),
  
                                  dl.Overlay(
                                      dl.LayerGroup(
                                          [
                                              dl.GeoJSON(data=eez_boundaries_json, 
                                                  format="geojson", 
                                                  style={"color":"white",
                                                          "weight":2
                                                  }
                                              )
                                          ]
                                      
                                      ),
                                      name="World EEZ Boundaries (Flanders Marine Institute (2023))",
                                      checked=True
                                  ),
  
                                  dl.Overlay(
                                      dl.LayerGroup(
                                          [
                                              dl.GeoJSON(
                                                  data=shipping_lanes_json, 
                                                  format="geojson", 
                                                  style={"color":"blue",
                                                          "dashArray":"8",
                                                          "weight":1
                                                  },
                                                  id="shipping_lanes"
                                              )
                                          ]
                                      
                                      ),
                                      name="World Shipping Lanes (Benden, P. (2022). Global Shipping Lanes, Data set)",
                                      checked=True
                                  ),
  
                                  dl.Overlay(
                                      dl.LayerGroup(
                                          [
                                              dl.Marker(
                                                  position=[row['lat'], row['lon']], 
                                                  icon=dict(
                                                      iconUrl=r"\assets\shipping_icons\piracy.png",
                                                      iconSize=[25, 25]
                                                  ),
                                                  children=[
                                                      dl.Popup(
                                                          content=f"<b>Date:</b> {row['date']}" 
                                                                  + "<br></br>" 
                                                                  + f"<b>Attack Type:</b> {row['attack_type']}"
                                                                  + "<br></br>" 
                                                                  + f"<b>Location:</b> {row['location_description']}" 
                                                                  + "<br></br>" 
                                                                  + f"<b>Vessel Name:</b> {row['vessel_name']}" 
                                                                  + "<br></br>" 
                                                                  + f"<b>Vessel Condition:</b> {row['vessel_status']}" 
                                                                  + "<extra></extra>"
                                                      )
                                                  ]
                                              ) for index, row in piracy_data.iterrows()
                                          ],
                                          id="piracy_markers"        
                                      ),
                                      name="Pirate Attacks (Benden, P., Feng, A., Howell, C., & Dalla Riva G. V. (2021))",
                                      checked=True,
                                  ),
                              ]),
                              
                              dl.FullScreenControl(),
  
                              dl.MeasureControl(position="topleft", 
                                              primaryLengthUnit="kilometers", 
                                              primaryAreaUnit="hectares",
                                              activeColor="#214097", 
                                              completedColor="#972158"
                              ),
  
                              dl.LocateControl(locateOptions={'enableHighAccuracy': True}),
  
                              dl.ScaleControl(position="bottomleft",
                                              maxWidth=300,
                                              metric=True,
                                              imperial=False),
  
                              dl.FeatureGroup([
                                  dl.EditControl(id="edit_control", position="topleft") 
                              ]),     
                          ], 
                          center=[5, 45],
                          zoom=5,
                          style={
                              "height": "75vh",
                              "padding":"10px 10px",
                              "font-size": "14px"
                          }
                      ),
  
                      html.Div(
                          html.Hr(), 
                          style={"padding":"20px 20px"},
                      ),
  
                      html.H2 ([html.I(className="bi bi-graph-up"), " Statistics"], 
                          style={"font-weight":"normal", 
                                  "font-size":"24px",
                                  "padding":"10px 10px"
                          },
                          className="text-center display-4"
                      ),
  
                      dbc.Tabs([
                          dbc.Tab(
                              label="Attacks by Years",
                              children=[
                                  html.Div([
                                      dcc.Graph (
                                        id="piracy_attacks_per_years_graph", 
                                        style={"width":"100%", "height":"100%"}
                                      )
                                  ], style={"border":"0.1px solid lightgray", "padding":"10px 10px"}),
                              ], 
                              style={"margin-top":"3em", "padding":"20px 20px"},
                              label_style={"color":"black"},
                              active_label_style={"color":"white", "background-color":"black"}
                          ),
  
                          dbc.Tab(
                              label="Attacks by Countries",
                              children=[
                                  html.Div([
                                      dcc.Graph (
                                        id="piracy_attacks_per_countries_graph", 
                                        style={"width":"100%", "height":"100%"}
                                      )
                                  ], style={"border":"0.1px solid lightgray", "padding":"10px 10px"}),
                              ],
                              style={"margin-top":"3em", "padding":"20px 20px"},
                              label_style={"color":"black"},
                              active_label_style={"color":"white", "background-color":"black"}
                          ),
  
                          dbc.Tab(
                              label="Attacks by Attack Types",
                              children=[
                                  html.Div([
                                      dcc.Graph (
                                        id="piracy_attacks_per_attack_types_graph", 
                                        style={"width":"100%", "height":"100%"}
                                      )
                                  ], style={"border":"0.1px solid lightgray", "padding":"10px 10px"}),
                              ],
                              style={"margin-top":"3em", "padding":"20px 20px"},
                              label_style={"color":"black"},
                              active_label_style={"color":"white", "background-color":"black"}
                          ),
                      ]),
                              
                      html.Div(
                          html.Hr(), 
                          style={"padding":"20px 20px"},
                      ),
  
                      html.H2 ([html.I(className="bi bi-table"), " Piracy Records between 1993-2020"], 
                          style={"font-weight":"normal", 
                                  "font-size":"24px",
                                  "padding":"10px 10px"
                          },
                          className="text-center display-4"
                      ),
  
                      html.Div ([
                          dcc.Download(id="download-dataframe-xlsx"),
  
                          html.Button("Export", 
                                      id="btn-excel-export", 
                                      className="btn btn-primary",
                                      style={"margin-bottom":"1em"}
                          ),
  
                          dag.AgGrid(
                              id="grid-excel-export",
                              rowData=piracy_data.to_dict("records"),
                              columnDefs=[{"field": i} for i in piracy_data.columns],
                              defaultColDef={"resizable": True, "filter": True, "sortable": True},
                          )
                      ], style={
                         "padding":"20px 20px"
                      })
                  ]), sm=6, md=6, lg=8
              )
          ], style={"padding":"20px 20px"})
  ], style={"margin-top":"3em"})

  return layout

# Figure Generation Canvas #    
@callback(
    Output("piracy_data_chart_editor", "is_open"),
    Input("generate_graphs_for_piracy_data", "n_clicks"),
    State("piracy_data_chart_editor", "is_open"),
)

def toggle_offcanvas_piracy_data_chart_editor(n1, is_open):
    if n1:
        return not is_open
    return is_open

# Display Attack Statistics as Graphs #
@callback(
    Output("piracy_attacks_per_years_graph", "figure"),
    [
        Input('btn-excel-export', 'n_clicks')
    ]
)
    
def display_piracy_attacks_per_years(date):
    # Data definition #
    # dataframe = database.fetch_piracy_data()
    dataframe = database.get_pirate_attacks()
    dataframe["Years"] = [i.year for i in dataframe["date"]]

    fig = database.display_attacks_per_years(dataframe)

    return fig

@callback(
    Output("piracy_attacks_per_countries_graph", "figure"),
    [
        Input('btn-excel-export', 'n_clicks')
    ]
)
    
def display_piracy_attacks_per_countries(date):
    # Data definition #
    # dataframe = database.fetch_piracy_data()
    dataframe = database.get_pirate_attacks()
    dataframe["Years"] = [i.year for i in dataframe["date"]]

    # fig = database.display_statistics_as_pie_chart(dataframe, "nearest_country")
    fig = database.display_attacks_by_countries(dataframe, "nearest_country")

    return fig

@callback(
    Output("piracy_attacks_per_attack_types_graph", "figure"),
    [
        Input('btn-excel-export', 'n_clicks')
    ]
)
    
def display_piracy_attacks_per_countries(date):
    # Data definition #
    # dataframe = database.fetch_piracy_data()
    dataframe = database.get_pirate_attacks()
    dataframe["Years"] = [i.year for i in dataframe["date"]]

    fig = database.display_attacks_by_attack_types(dataframe, "attack_type")

    return fig

# Exporting Piracy Data as Excel File #
@callback(
    Output('download-dataframe-xlsx', 'data'),
    Input('btn-excel-export', 'n_clicks'),
    State('grid-excel-export', "virtualRowData"),
    prevent_initial_call=True
)
    
def export_gantt_chart_data_to_excel(n, data):
    df = pd.DataFrame(data)
    if n:    
        return dcc.send_data_frame(df.to_excel, filename="Piracy_Data.xlsx", sheet_name="Sheet1")
