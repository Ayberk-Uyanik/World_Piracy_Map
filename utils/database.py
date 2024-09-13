# Importing necessary libraries #
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine

## SQL Database Connection Using SQLAlchemy ##
def fetch_piracy_data():
    # Connection string
    engine = create_engine('mssql+pyodbc://@' + 'ANK19393\MSSQLSERVER2022' + '/' + 'sectoral' + '?trusted_connection=yes&driver=SQL+Server')

    # SQL query to fetch all data from a table
    query = 'SELECT * FROM world_pirate_attacks;'

    # Execute the query and fetch the data into a DataFrame
    df = pd.read_sql(query, engine)
    # df_sorted = df.sort_values(by=["Dates"])

    # Display the DataFrame
    return df

# Import Pirate Attacks #
def get_pirate_attacks():
    piracy_data = pd.read_excel (r"assets/database/maritime_data.xlsx", sheet_name="pirate_attacks_somalia")

    return piracy_data

# Generating Chart for Attack Counts per Year #
def display_attacks_per_years(dataframe):
    # Dataframe Filtering #
    attacks_year_labels = dataframe["Years"].unique()
    attacks_year_counts = dataframe["Years"].value_counts()

    df_dict = {
        "X": attacks_year_labels,
        "Y": attacks_year_counts.loc[attacks_year_labels]
    }

    df = pd.DataFrame.from_dict(df_dict)
    df = df.sort_values(by="Y", ascending=True)

    # Figure Initiation #
    fig = go.Figure ()

    # Figure Data Selection #
    fig.add_trace(go.Bar(x=df["X"], 
                        y=df["Y"], 
                        name="Attacks per Year", 
                        marker=dict(color="teal", opacity=1), 
                        hovertemplate="Attack Year: %{x}<br>" +
                                    "Number of Attacks: %{y}<br>" + 
                                    "<extra></extra>", 
                        )
    )

    # Figure Layout #
    fig.update_layout (title="Pirate Attacks between 1993-2012", 
                title_x=0.5, 
                template="plotly_white",
                showlegend=False,
                # width=1200,
                # height=800
    )
    
    # X-Axis Styles #
    fig.update_xaxes(title=dict(text="Years"), 
                    color="black", 
                    tickangle=90
    )

    # Y Axis Styles #
    fig.update_yaxes(title=dict(text="Number of Attacks"), 
                    color="black", 
                    range=[0, 250]
    )

    return fig

# Generating Charts for Attacks per Countries as Pie Charts #
def display_statistics_as_pie_chart(dataframe, parameter):
    # Dataframe Filtering #
    attack_labels = dataframe[f"{parameter}"].unique()
    attack_labels = np.delete(attack_labels, 0)

    attack_counts = dataframe[f"{parameter}"].value_counts().loc[attack_labels]

    # Figure Initiation #
    fig = go.Figure ()

    # Figure Data Selection #
    fig.add_trace(go.Pie(labels=attack_labels, 
                        values=attack_counts, 
                        hole=0.5, 
                        marker=dict(colors=px.colors.sequential.Bluyl_r), 
                        text=attack_labels,
                        customdata=attack_counts,
                        hovertemplate="parameter: %{text}<br>" +
                                    "Count: %{customdata}<br>" + 
                                    "<extra></extra>",
                        )
    )

    # Figure Layout #
    fig.update_layout (title=f"Statistics Based on {parameter}", title_x=0.5)

    return fig

# Generating Charts for Attacks per Countries as Horizontal Bar Chart #
def display_attacks_by_countries (dataframe, parameter):
    # Figure constants #
    dataframe = dataframe[[f"{parameter}"]]
    dataframe = dataframe.dropna(axis=0, inplace=False)

    attack_labels = dataframe[f"{parameter}"].unique()
    attack_counts = dataframe[f"{parameter}"].value_counts().loc[attack_labels]

    # Figure Initiation #
    fig = go.Figure ()

    # Figure Data Selection #
    fig.add_trace(go.Bar(x=attack_counts, 
                        y=attack_labels,
                        orientation="h", 
                        name="Pirate Attacks", 
                        marker=dict(color="teal", opacity=1),
                        text=attack_counts, 
                        textposition="outside", 
                        hovertemplate="Country: %{y}<br>" +
                                    "Number of Attacks: %{x}<br>" + 
                                    "<extra></extra>", 
                    )               
    )

    # Figure Layout #
    fig.update_layout (title="Pirate Attacks by Country", 
                    title_x=0.5, 
                    template="plotly_white",
                    showlegend=False,
                    # width=1400,
                    # height=850,
                    yaxis={'categoryorder':'total descending'},
                    # bargap=0.45,
                    bargroupgap=0.35
    )
    
    # X-Axis Styles #
    fig.update_xaxes(
        title=dict(text="Number of Attacks"), 
        range=[0, 600]
    )

    # Y Axis Styles #
    fig.update_yaxes(
        title=dict(
            text="Countries"   
        ),
        autorange="reversed"
    )

    return fig

def display_attacks_by_attack_types (dataframe, parameter):
    # Figure constants #
    attack_labels = dataframe[f"{parameter}"].unique()
    attack_labels = np.delete(attack_labels, 0)

    attack_counts = dataframe[f"{parameter}"].value_counts().loc[attack_labels]

    # Figure Initiation #
    fig = go.Figure ()

    # Figure Data Selection #
    fig.add_trace(go.Bar(x=attack_counts, 
                        y=attack_labels,
                        orientation="h", 
                        name="Pirate Attacks", 
                        marker=dict(color="teal", opacity=1),
                        text=attack_counts, 
                        textposition="outside", 
                        hovertemplate="Type of Attack: %{y}<br>" +
                                    "Number of Attacks: %{x}<br>" + 
                                    "<extra></extra>", 
                    )               
    )

    # Figure Layout #
    fig.update_layout (title="Pirate Attacks by Attack Types", 
                    title_x=0.5, 
                    template="plotly_white",
                    showlegend=False,
                    # width=1400,
                    # height=850,
                    yaxis={'categoryorder':'total descending'},
                    # bargap=0.45,
                    bargroupgap=0.35
    )
    
    # X-Axis Styles #
    fig.update_xaxes(
        title=dict(text="Number of Attacks"), 
        range=[0, 900]
    )

    # Y Axis Styles #
    fig.update_yaxes(
        title=dict(
            text="Attack Types"   
        ),
        autorange="reversed"
    )

    return fig