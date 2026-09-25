import flet as ft
from flet_webview import WebView

@ft.component
def StockViewPage():
    params = ft.use_route_params()
    
    symbol = params.get("symbol", "")
    url = f"https://www.dse.com.bd/company/{symbol}"
    
    # print(f"Rendering WebView for Symbol: {symbol}")

    return ft.Container(
        expand=True,
        content=ft.Column(
            controls=[
                # Navigation Header Bar
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            tooltip="Back to Watchlist",
                            on_click=lambda _: ft.context.page.navigate("/"),
                        ),
                        ft.Text(f"Stock: {symbol}", size=18, weight=ft.FontWeight.BOLD),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Divider(height=1),
                
                # WebView re-renders automatically when symbol changes
                WebView(
                    url=url,
                    expand=True,
                    # javascript_enabled=True,
                    # user_agent="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
                ),
                # ft.IFrame(
                #     url=url,
                #     expand=True,
                # ),
            ],
            expand=True,
            spacing=0,
        )
    )