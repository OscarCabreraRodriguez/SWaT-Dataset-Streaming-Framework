import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
from flask import Flask


X = deque(maxlen=20)
X.append(1)
Y = deque(maxlen=20)
Y.append(1)


server = Flask(__name__)
app = dash.Dash(server=server) #type: ignore
app.layout = html.Div(
    [
        dcc.Graph(id="live-graph", animate=True),
        dcc.Interval(id="graph-update", interval=1000, n_intervals=0),
    ]
)


@app.callback(Output("live-graph", "figure"), [Input("graph-update", "n_intervals")])
def update_graph_scatter(n):

    X.append(X[-1] + 1)

    Y.append(Y[-1] + Y[-1] * random.uniform(-0.1, 0.1))

    data = plotly.graph_objs.Scatter(
        x=list(X), y=list(Y), name="Scatter", mode="lines+markers"
    )

    return {
        "data": [data],
        "layout": go.Layout(
            xaxis=dict(range=[min(X), max(X)]),
            yaxis=dict(range=[min(Y), max(Y)]),
        ),
    }
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

class Influx:
    def __init__(self) -> None:
        self.token = "91XonVTK0cXpXmwjoF32jKOeMKIkf2LPK4Vm5lURZJKR2mNP9pftxRxvcBu487wUa0hPoggNTImKDFpzzxDQsQ=="
        self.url = "http://influxdb:8086"
        self.org = "ost"
        self.client = influxdb_client.InfluxDBClient(
        url=self.url,
        token=self.token,
        org=self.org)

    def get_data(self):
        # Query script
        query_api = self.client.query_api()
        query = 'from(bucket:"my-bucket")\
        |> range(start: -10m)\
        |> filter(fn:(r) => r._measurement == "my_measurement")\
        |> filter(fn:(r) => r.location == "Prague")\
        |> filter(fn:(r) => r._field == "temperature")'
        result = query_api.query(org=self.org, query=query)
        results = []
        for table in result:
            for record in table.records:
                results.append((record.get_field(), record.get_value()))

        print(results)


if __name__ == "__main__":
    # app.run_server(debug=True)
    