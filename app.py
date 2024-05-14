from flask import Flask, render_template

import json
import numpy as np
import pandas as pd

import plotly
import plotly.graph_objects as go

def create_plot():
    df = plotly.data.stocks()
    data = [
        go.Scatter(
            x=df['date'],
            y=df['AMZN']
        )
    ]
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

app = Flask(__name__)

@app.route('/')
def index():
    scatter_plot = create_plot()
    return render_template('index.html', plot=scatter_plot)

if __name__ == '__main__':
    app.run()