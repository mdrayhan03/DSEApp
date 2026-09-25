import flet as ft
from components.add_button import AddButton
from components.watchlist_component import WatchListComponent

class WatchListPage(ft.Column) :
    def __init__(self):
        super().__init__()
        watchlist_text = ft.Text(
            "Your Watchlist", 
            size=22, 
            weight=ft.FontWeight.BOLD
        )

        add_button = AddButton()

        header =  ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        watchlist_text,
                        add_button,
                    ],
                )

        watchlist_component = WatchListComponent()


        self.controls = [
            header,
            ft.Divider(),
            watchlist_component
        ]

