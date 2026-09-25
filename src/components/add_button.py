import flet as ft

class AddButton(ft.IconButton) :
    def __init__(self):
        super().__init__()

        self.icon = ft.Icons.ADD
        self.on_click = self.handle_action

    def handle_action(self) :
        # print("Add Button Click")
        pass

