import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

df = pd.read_csv("example-3/bike-accidents.csv")

app = dash.Dash(__name__)

districts = [{"label": district, "value": district} for district in  df["DISTRITO"].unique()]

app.layout = html.Div(children = [
    html.H1("Bicimad accidents by district and time of day"),
    dcc.Dropdown(
        id="district",
        options=districts,
        multi=True,
        value=districts[0]["value"]
    ),
    dcc.Graph(
        id="accidents-graph",
        figure={
            "data": [],
            "layout": {
                "title": "accidents"
            }
        }
    )
])

xs = list(sorted(df["HORA"].unique()))

@app.callback(
    Output(component_id="accidents-graph",component_property="figure"),
    [Input(component_id="district", component_property="value")]
)
def change_h2_on_input_change(districts):

    ys = []

    for district in districts:
        count = df[df["DISTRITO"] == district]["HORA"].count()
        row = {'x': list(range(0, 50)), 'y': [count], 'type': 'bar', 'name': district}
        ys.append(row)


    print(ys)

    return {
        "data": ys,
        "layout": {
            "title": "Stock prices"
        }
    }

app.run_server(debug=True)
