from dash import Dash
import dash_bootstrap_components as dbc
import dash_labs as dl

from dash_charlotte import themes
from dash_charlotte.components import (
    Dashboard,
    Drawer,
    DrawerSingleItem,
    DrawerMultiItem,
    DrawerSubItem,
    DrawerFooter,
    Navbar
)



app = Dash(
    name = __name__,
    title = 'Dash Charlotte',
    plugins = [dl.plugins.pages],
    external_stylesheets = [
        dbc.themes.BOOTSTRAP,
        themes.BOOTSTRAP,
        themes.BOXICONS,
        themes.FONTAWESOME,
        themes.CHARLOTTE_DARK
    ]
)



nav_links = [
    DrawerSingleItem(
        name = 'Login',
        icon = 'bx bx-log-in',
        href = '/login'
    ),
    DrawerMultiItem(
        name = 'Analytics',
        icon = 'bx bx-line-chart',
        href = '/page2',
        submenu = [
            DrawerSubItem(
                name = 'Page 1',
                href = '/page1'
            ),
            DrawerSubItem(
                name = 'Page 2',
                href = '/page2'
            )
        ]
    ),
    DrawerSingleItem(
        name = 'Icons',
        icon = 'bx bx-grid-alt',
        href = '/icons'
    ),
    DrawerSingleItem(
        name = 'Box',
        icon = 'bx bx-box',
        href = '/box'
    ),
    DrawerSingleItem(
        name = 'Table',
        icon = 'bx bx-table',
        href = '/table'
    ),
    DrawerFooter(
        title = 'Footer',
        subtitle = 'Footer Subtitle'
    )
]



app.layout = Dashboard(
    children = dl.plugins.page_container,
    navbar = Navbar(
        title = 'Navbar'
    ),
    drawer = Drawer(
        menu = nav_links,
        logo_name = 'Charlotte',
        logo_icon = 'fas fa-rocket'
    )
)


server = app.server
if __name__ == '__main__':
    app.run_server(
        host = '0.0.0.0',
        port = 1000
    )
