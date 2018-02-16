import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html # includes all (510!) html tags and their properties
import dash_table_experiments as dt
from pandas_datareader import data as web # widget library: dropdowns, graphs, sliders, tabs, etc
import datetime

app = dash.Dash()

# app.layout describes what the app looks like
app.layout = html.Div([
    html.H1('Hello Dash'),

    html.Div(
        children="Dash: A web application framework for Python.",
        style={
            'borderBottom': 'thin lightgrey solid'
        }
    ),

    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Coke', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value='COKE'
    ),

    dcc.Graph(
        id='hello-dash-graph',
        style={'height': '70vh'}
    ),

])


@app.callback(Output('hello-dash-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
        selected_dropdown_value, data_source='google',
        start=datetime.datetime(2017, 1, 1),
        end=datetime.datetime.now())

    # a declarative description of the graph
    return {
        'data': [{
            'x': df.index,
            'y': df.Close,
            'line': {
                'width': 2,
                'shape': 'spline'
            }
        }],
        'layout': {
            'margin': {
                'l': 40,
                'r': 10,
                't': 20,
                'b': 30
            }
        }
    }


if __name__ == '__main__':
    app.run_server(debug=True)  # debug=True will reload the app when you make changes to the code

