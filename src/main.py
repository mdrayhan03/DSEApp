import flet as ft
from pages.watchlist import WatchListPage
from pages.stock_view import StockViewPage

@ft.component
def App():
    # Wrap the Router inside SafeArea
    return ft.SafeArea(
        expand=True,
        content=ft.Router([
            # Index route matches "/"
            ft.Route(index=True, component=WatchListPage),
            
            # Dynamic parameter route matches "/stockview/:symbol"
            ft.Route(path="stockview/:symbol", component=StockViewPage),
        ]),
    )

def main(page: ft.Page) :
    # Set window dimensions (typical mobile screen ratio)
    page.window.width = 390
    page.window.height = 844
    
    # Prevent resizing (optional, keeps fixed phone aspect ratio)
    page.window.resizable = False
    
    # app title
    page.title = "DSE App"

    # using light theme
    page.theme_mode = ft.ThemeMode.LIGHT

    # not using any top padding
    page.padding = 5

    page.render(App)

if __name__ == "__main__" :
    ft.run(main)