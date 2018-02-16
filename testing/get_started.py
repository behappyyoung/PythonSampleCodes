import plotly
from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go

import numpy as np
import pandas as pd

init_notebook_mode()
iplot({
    'data': [{
        'x': [1, 2, 3],
        'y': [3, 1, 2],
        'type': 'scatter',
        'mode': 'lines' # 'markers' | 'lines+markers'
    }],
    'layout': {
        'title': 'Plotly Graph',
        'xaxis': {
            'title': 'Time'
        },
        'yaxis': {
            'title': 'Voltage'
        }
    }
})

