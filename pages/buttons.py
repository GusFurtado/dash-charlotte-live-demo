from dash_charlotte.components import Button, Footer

from dash import register_page
import dash_bootstrap_components as dbc



register_page(
    module = __name__,
    path = '/buttons',
    title = 'Dash Charlotte Buttons'
)




COLORS = [
    'red',
    'orange',
    'yellow',
    'green',
    'cyan',
    'blue',
    'purple',
    'pink'
]



def row_of_buttons(color:str) -> Button:
    return dbc.Row(
        children = [
            dbc.Col(
                Button(
                    f'{color.title()} Button',
                    type = t,
                    color = color,
                    className = 'me-2'
                ),
                width = 'auto'
            ) for t in ['shadow', 'arrow']
        ],
        className = 'mt-3',
        justify = 'center'
    )



layout = [row_of_buttons(color) for color in COLORS] \
    + [Footer(right_text='Dash Charlotte')]
