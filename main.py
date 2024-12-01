import flet as ft
from src.state_machine.state import App

def main(page: ft.Page):
    App(page)
    
ft.app(main)