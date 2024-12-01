from flet import Container, Column, Text, colors, padding, border_radius, Row, IconButton, icons
from src.colors.colors import COLORS

class CardInformativo(Column):
    def __init__(self, titulo, descricao, remover_card):
        super().__init__()
        self.titulo = titulo
        self.descricao = descricao
        self.remover_card = remover_card

    def build(self):
        return Container(
                content=Column(
                    [
                        Row(
                            [
                                Text(self.titulo, size=20, weight='bold', color=COLORS["accent"]),
                                IconButton(icon=icons.CLOSE, on_click=self.remover_card, icon_color=COLORS["error"]),
                            ],
                            alignment='spaceBetween',
                        ),
                        Text(self.descricao, size=14, color=COLORS["text_primary"])
                    ],
                    spacing=10,
                ),
                padding=padding.all(15),
                border_radius=border_radius.all(10),
                bgcolor=COLORS["card_background"],
            )
        