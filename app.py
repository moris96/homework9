import dash
from dash.dependencies import Input, Output
from dash import html
from dash import dcc
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


# first tab = 3d line chart
df = px.data.gapminder().query("continent=='Europe'")
fig1 = px.line_3d(df, x="gdpPercap", y="pop", z="year", color='country')

# second tab = Helix equation (3d scatter plot)
t = np.linspace(0, 10, 50)
x, y, z = np.cos(t), np.sin(t), t

fig2 = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z,
                                   mode='markers')])


# third tab = 3d mesh plot
pts = np.loadtxt(np.DataSource().open('https://raw.githubusercontent.com/plotly/datasets/master/mesh_dataset.txt'))
x, y, z = pts.T

fig3 = go.Figure(data=[go.Mesh3d(x=x, y=y, z=z, color='lightpink', opacity=0.50)])



# layout stuff bro
myheading1 = 'Cool python stuff with plotly & dash'
tabtitle = "python stuff"
sourceurl = 'https://plotly.com/python/3d-charts/'
githublink = 'https://git.generalassemb.ly/moris96/homework-9'
image1 = 'nagini.jpg'

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle
app.config['suppress_callback_exceptions'] = True

app.layout = html.Div([
    html.H1(myheading1, style={'text-align': 'center'}),
    html.Img(src=app.get_asset_url(image1)),
    dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph', children=[
        dcc.Tab(label='Plotly 3d example 1', value='tab-1-example-graph'),
        dcc.Tab(label='Plotly 3d example 2', value='tab-2-example-graph'),
        dcc.Tab(label='Plotly 3d example 3', value='tab-3-example-graph'),
    ]),
    html.Div(id='tabs-content-example-graph'),
    html.Div([
        html.A('Code on Github', href=githublink),
        html.Br(),
        html.A("Data Source", href=sourceurl),
])
])



@app.callback(Output('tabs-content-example-graph', 'children'),
              Input('tabs-example-graph', 'value'))
def render_content(tab):
    if tab == 'tab-1-example-graph':
        return html.Div([
            html.H3('3D Line Chart'),
            dcc.Graph(figure=fig1)
        ])
    elif tab == 'tab-2-example-graph':
        return html.Div([
            html.H3('3D Scatterplot: Helix Equation (A helix, sometimes also called a coil, is a curve for which the tangent makes a constant angle with a fixed line... and it looks cool)'),
            dcc.Graph(figure=fig2)
        ])
    elif tab == 'tab-3-example-graph':
        return html.Div([
            html.H3('3D Mesh Plot'),
            dcc.Graph(figure=fig3)
        ])
if __name__ == '__main__':
    app.run_server(debug=True)