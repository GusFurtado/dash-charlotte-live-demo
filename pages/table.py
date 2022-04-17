from dash_charlotte.components.table import (
    Table,
    TableTextCol,
    TableButtonCol,
    TableCheckBoxCol,
    TableDropdownCol,
    TableInputCol
)
from dash_charlotte.themes import charlotte_light as cl

from dash import (
    register_page,
    html,
    callback,
    callback_context,
    Output,
    Input,
    ALL
)
import dash_bootstrap_components as dbc
import numpy as np
import pandas as pd



register_page(
    __name__,
    path = '/table',
    title = 'Dash Charlotte Table'
)



df = pd.DataFrame({
    'col1': [1,2,3,4],
    'col2': ['Banana', 'Apple', 'Orange', 'Grape'],
    'col3': np.random.random(4)
})



CELL_STYLE = {
    'padding': 10,
    'text-align': 'center'
}

HEADER_STYLE = {
    'padding': 10,
    'text-align': 'center',
    'background-color': str(cl.BLUE)
}

BODY_STYLE = {
    'background-color': 'white',
    'cursor': 'pointer'
}

FRUIT_FORMATTING = lambda td: html.B(
    children = td,
    style = {
        'color': {
            'Banana': str(cl.YELLOW),
            'Apple': str(cl.RED),
            'Orange': str(cl.ORANGE),
            'Grape': str(cl.PURPLE)
        }[td]
    }
)



col1 = TableDropdownCol(
    header = 'Dropdown',
    header_style = HEADER_STYLE,
    cell_style = {'padding': 5},
    dropdown_id = df.col1.apply(lambda x: {'table_dropdown': x}),
    dropdown_placeholder = 'Select...',
    dropdown_options = [
        {'label': 'Yes', 'value': 1},
        {'label': 'No', 'value': 0}
    ]
)

col2 = TableTextCol(
    header = 'Style Format',
    header_style = HEADER_STYLE,
    cell_style = CELL_STYLE,
    text = df.col2,
    text_formatting = FRUIT_FORMATTING
)

col3 = TableInputCol(
    header = 'Number Input',
    header_style = HEADER_STYLE,
    cell_style = {'padding': 5},
    input_id = df.col1.apply(lambda x: {'table_input': x}),
    input_value = df.index,
    input_type = 'number',
    input_min = 0,
    input_max = 9
)

col4 = TableTextCol(
    header = 'String Format',
    header_style = HEADER_STYLE,
    cell_style = CELL_STYLE,
    text = 10_000 * df.col3,
    text_formatting = 'R$ {:,.2f}'.format
)

col5 = TableButtonCol(
    header = 'Button',
    header_style = HEADER_STYLE,
    cell_style = {'text-align': 'center'},
    button_icon = 'fas fa-exclamation-triangle',
    button_text = df.col1.apply('Action {}!'.format),
    button_id = df.col1.apply(lambda x: {'table_button': x})
)

col6 = TableInputCol(
    header = 'Misc. Input',
    header_style = HEADER_STYLE,
    cell_style = {'padding': 5},
    input_id = df.col1.apply(lambda x: {'table_input2': x}),
    input_value = df.col2,
    input_type = ['text', 'email', 'password', 'url']
)

col7 = TableCheckBoxCol(
    header = '',
    header_style = HEADER_STYLE,
    cell_style = CELL_STYLE,
    checkbox_value = df.index % 2 == 1,
    checkbox_id = df.col1.apply(lambda x: {'table_checkbox': x})
)



layout = dbc.Container([
    html.Div(
        children = Table(
            columns = [col1, col2, col3, col4, col5, col6, col7],
            body_style = BODY_STYLE,
            bordered = True,
            dark = False,
            hover = True,
            responsive = True,
            striped = True,
            className = 'mb-0'
        ),
        className = 'shadow'
    ),
    dbc.Alert(
        id = 'table_alert',
        is_open = False,
        dismissable = True,
        color = 'primary',
        className = 'shadow mt-4'   
    )
])



@callback(
    Output('table_alert', 'children'),
    Output('table_alert', 'is_open'),
    Input({'table_button': ALL}, 'n_clicks'),
    prevent_initial_call = True)
def open_alert(_):
    cc = callback_context.triggered[0]['prop_id']
    return cc, True
