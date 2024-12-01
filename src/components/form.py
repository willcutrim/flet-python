from flet import TextField


class InputText(TextField):
    def __init__(self, label, keyboard, icon):
        super().__init__()
        self.label = label
        self.keyboard = keyboard
        self.icon = icon
    
    def build(self):
        return TextField(
            label=self.label,
            multiline=False,
            keyboard_type=self.keyboard,
            icon=self.icon,
            expand=True
        )