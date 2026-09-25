import flet as ft

WATCHLIST = ["BEXIMCO", "CITYBANK", "ORIONPHARM"]

class WatchListComponent(ft.ListView) :
    def __init__(self):
        super().__init__()

        self.expand = 1
        self.spacing = 10
        self.item_extent = 50

        for ele in WATCHLIST :
            button = ft.FilledTonalButton(
                content=ft.Text(ele),
                icon= ft.Icons.SHOW_CHART,
                on_click=lambda e, item = ele : self.handle_action(item),
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=12),
                ),
            )

            self.controls.append(button)

    def handle_action(self, symobl) :
        print(f"Symbol: {symobl}")
        ft.context.page.navigate(f"stockview/{symobl}")

