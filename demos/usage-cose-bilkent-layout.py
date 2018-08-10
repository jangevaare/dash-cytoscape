import my_dash_component
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import json

app = dash.Dash(__name__)
server = app.server

app.scripts.append_script({
    'external_url': 'https://cdn.rawgit.com/cytoscape/cytoscape.js-cose-bilkent/d810281d/cytoscape-cose-bilkent.js'
})

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

# Load Data
with open(f'cose-bilkent-layout/data.json', 'r') as f:
    elements = json.loads(f.read())

# App
app.layout = html.Div([
    my_dash_component.Cytoscape(
        id='cytoscape',
        elements=elements,
        layout={
            'name': 'cose-bilkent',
            'animate': False
        },
        stylesheet=[{
            'selector': 'node',
            'style': {
                'background-color': '#ad1a66'
            }
        }, {
            'selector': 'edge',
            'style': {
                'width': 3,
                'line-color': '#ad1a66'
            }
        }],

        style={
            'width': '100%',
            'height': '100%',
            'position': 'absolute',
            'left': 0,
            'top': 0,
            'z-index': 999
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
