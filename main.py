import flet as ft

def main(page: ft.Page):
    
    
    page.theme_mode = ft.ThemeMode.LIGHT
    
    page.title = "Eventos"
    
    titulo=(ft.Text(
        value="Crear un evento",
        size=60,
        weight=ft.FontWeight.BOLD,
        italic=True,
        text_align=ft.TextAlign.CENTER,
        max_lines=2,
        overflow=ft.TextOverflow.ELLIPSIS
    ))
    
    nombre = ft.TextField(
        label="Nombre del evento",
        hint_text="Ingrese el nombre del evento",
        width=300,
        max_length=50,
    )
    
    if nombre.value == "":
        page.add(ft.Text(
            value="Por favor, ingrese un nombre para el evento.",
            color=ft.Colors.RED_400,
            size=12
        ))
    
    opcion=(ft.Dropdown(
        options=[
            ft.DropdownOption("Conferencia"),
            ft.DropdownOption("Taller"),
            ft.DropdownOption("Reunión"),
        ]
    ))
    
    modalidad=(ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Presencial", label="Presencial"),
            ft.Radio(value="Virtual", label="Virtual"),
        ])
    ))
    
    inscripcion=(ft.Checkbox(
        label="¿Requiere inscripción previa?"
    ))
    
    hora=(ft.Slider(
        min=0,
        max=8,
        divisions=8,
        value=1,
        label="Horas: {value}",
        width=300
    ))
    
    list = ft.ListView(
        expand=True,     
        spacing=10
    )
    
    def evento():
        page.add(ft.Text(
        value="Resumen del evento", color=ft.Colors.BLUE_400, size=30
        ))
        page.add(ft.Text(
            f"Evento: {nombre.value}, Tipo: {opcion.value}, Modalidad: {modalidad.value}, Requiere inscripción: {inscripcion.value}, Duración: {hora.value} horas"))
        list.controls.append(ft.Text(f"Evento: {nombre.value}, Tipo: {opcion.value}, Modalidad: {modalidad.value}, Requiere inscripción: {inscripcion.value}, Duración: {hora.value} horas"))
        page.update()
    
    def eventos():
        page.add(ft.Text(
        value="Lista de eventos", color=ft.Colors.BLUE_400, size=24
        ))
        for i in range(len(list.controls)):
            page.add(ft.Text(list.controls[i].value))
        page.update()
    
    boton=(ft.ElevatedButton
        ("Crear evento", 
        on_click=evento,
        bgcolor=ft.Colors.GREEN_400,
        color=ft.Colors.WHITE  
        ))
    
    page.add(
        ft.Column(
            controls=[
                titulo,
                nombre,
                ft.Text("Tipo de evento"),
                opcion,
                ft.Text("Modalidad"),
                modalidad,
                inscripcion,
                ft.Row([ft.Text("Horas"), hora]),
                boton
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )

    page.add(ft.Divider(height=10,thickness=10,color=ft.Colors.BLUE_400))
    
    
    page.add(ft.ElevatedButton
        ("Ver eventos ", 
        on_click=eventos,
        bgcolor=ft.Colors.GREEN_400,
        color=ft.Colors.WHITE  
        ))
    

ft.run(main)