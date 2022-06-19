from dash import Dash, page_container
import dash_bootstrap_components as dbc

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
    use_pages = True,
    external_stylesheets = [
        dbc.themes.BOOTSTRAP,
        themes.BOOTSTRAP,
        themes.BOXICONS,
        themes.BUTTONS,
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
    children = page_container,
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
