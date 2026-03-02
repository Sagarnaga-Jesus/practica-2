import flet as ft

def main(page: ft.Page):
    
    page.add(ft.Text(
        value="Crear un evento",
        size=60,
        weight=ft.FontWeight.BOLD,
        italic=True,
        text_align=ft.TextAlign.CENTER,
        max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS
    ))
    
    page.add(ft.TextField(
        label="Nombre del evento",
        hint_text="Ingrese el nombre del evento",
        width=300,
        max_length=50,
    ))
    
    page.add(ft.Dropdown(
        options=[
            ft.DropdownOption("Conferencia"),
            ft.DropdownOption("Taller"),
            ft.DropdownOption("Reunión"),
        ]
    ))
    
    page.add(ft.Checkbox(
        label="¿Requiere inscripción previa?"
    ))
    
    page.add(ft.Slider(
        min=1,
        max=8,
        divisions=8,
        value=1,
        label="Horas: {value}",
        height=25
))

ft.run(main)