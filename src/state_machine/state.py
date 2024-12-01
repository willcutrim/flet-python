from flet import (
    ThemeMode, Page, AppBar, Text, IconButton, icons, Row,
    Column, KeyboardType, FloatingActionButton, colors, SnackBar
)
from src.components.card_informativo import CardInformativo
from src.components.form import InputText
from src.colors.colors import COLORS


class State:
    def __init__(self, update_ui_callback):
        self.cards = []
        self.update_ui_callback = update_ui_callback

    def add_card(self, titulo, descricao):
        """Adiciona um cartão ao estado."""
        card = {
            "titulo": titulo,
            "descricao": descricao,
        }
        self.cards.append(card)
        self.update_ui()

    def remove_card(self, index):
        """Remove um cartão do estado."""
        if 0 <= index < len(self.cards):
            self.cards.pop(index)
            self.update_ui()

    def update_ui(self):
        """Chama o callback para atualizar a interface."""
        if self.update_ui_callback:
            self.update_ui_callback()


class App:
    def __init__(self, page: Page):
        self.page = page
        self.page.title = "Página principal"
        self.page.theme_mode = ThemeMode.DARK

        # Inicializar estado com callback para atualizar a interface
        self.state = State(self.atualizar_ui)

        self.titulo = InputText("Título", KeyboardType.TEXT, icons.TITLE)
        self.descricao = InputText("Descrição", KeyboardType.TEXT, icons.DESCRIPTION)

        # Configurar a UI
        self.configurar_appbar()
        self.configurar_floating_action_button()
        self.construir_ui()

        self.page.snack_bar = SnackBar(
            content=Text("", color=colors.WHITE),
            bgcolor=colors.RED,
            action="Fechar",
        )

    def alerta(self, titulo, cor_texto, cor_alerta):
        self.page.snack_bar.content = Text(titulo, color=cor_texto)
        self.page.snack_bar.bgcolor = cor_alerta
        self.page.snack_bar.open = True
        self.page.update()

    def configurar_appbar(self):
        def mudar_tema(_):
            self.page.theme_mode = ThemeMode.LIGHT if self.page.theme_mode == ThemeMode.DARK else ThemeMode.DARK
            self.page.update()

        self.page.appbar = AppBar(
            title=Text("Appbar"),
            elevation=10,
            actions=[
                IconButton(
                    icon=icons.DARK_MODE_OUTLINED,
                    on_click=mudar_tema,
                )
            ],
        )

    def configurar_floating_action_button(self):
        self.page.floating_action_button = FloatingActionButton(
            icon=icons.ADD,
            bgcolor=COLORS["button"],
            on_click=self.adicionar_cartao,
        )


    def adicionar_cartao(self, _):
        if not self.titulo.value or not self.descricao.value:
            self.alerta(
                'Os campos "título" e "descrição" são orbigatórios!', 
                cor_texto=COLORS['text_primary'],
                cor_alerta=COLORS['error']
            ) 
            return

        self.state.add_card(self.titulo.value, self.descricao.value)

        self.alerta(
            'Cartão adicionado com sucesso!', 
            cor_texto=COLORS['text_primary'],
            cor_alerta=COLORS['button']
        ) 

        self.titulo.value = ""
        self.descricao.value = ""
        self.page.update()

    def remover_cartao(self, index):
        # Remove o cartão no índice fornecido
        self.state.remove_card(index)

    def atualizar_ui(self):
        """Atualiza a interface com base no estado atual."""
        cards_ui = []
        for index, card in enumerate(self.state.cards):
            card_component = CardInformativo(
                titulo=card["titulo"],
                descricao=card["descricao"],
                remover_card=lambda _, idx=index: self.remover_cartao(idx),
            )
            cards_ui.append(card_component.build())

        # Reconstrói os controles da página
        self.page.controls = [
            Row([self.titulo, self.descricao]),
            Column(cards_ui),
        ]
        self.page.update()

    def construir_ui(self):
        """Cria a interface inicial."""
        self.page.bgcolor = COLORS["background"]  # Fundo escuro
        self.page.add(
            Row(
                [self.titulo, self.descricao],
            )
        )

