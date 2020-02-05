
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(children = [
  html.H1("Using callbacks"),
  dcc.Input(id="textbox-changed", type="text"),
  html.H2(id="id-changes")
])

@app.callback(
  Output(component_id="id-changes",component_property="children"),
  [Input(component_id="textbox-changed", component_property="value")]
)
def change_h2_on_input_change(value):
    return value

app.run_server(debug=True)