import dash
from dash import dcc, html, Input, Output
import numpy as np
import plotly.express as px

# Initialize the Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Sine Function Visualization"),
    dcc.Slider(
        id='frequency-slider',
        min=1,
        max=10,
        step=0.5,
        value=5,
        marks={i: str(i) for i in range(1, 11)}
    ),
    dcc.Graph(id='sine-graph')
])

# Callback function to update the graph
@app.callback(
    Output('sine-graph', 'figure'),
    Input('frequency-slider', 'value')
)
def update_graph(frequency):
    x = np.linspace(0, 10, 100)
    y = np.sin(frequency * x)
    fig = px.line(x=x, y=y, title=f"Sine Function with Frequency: {frequency}")
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
