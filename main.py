import flet as ft
from datetime import datetime

def main(page: ft.Page):
    
    page.theme_mode = ft.ThemeMode.LIGHT
    
    page.title = "Eventos"
    
    titulo=(ft.Text(
        value="Crear un evento",
        size=40,
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
    
    lista = ft.ListView(
        expand=True,
        spacing=10,
        padding=20,
        divider_thickness=2,
        visible=False
    )
    
    resumen = ft.Text(size=20, color=ft.Colors.BLUE_400)
    
    def evento():
        if not nombre.value:
            resumen.value = "El nombre del evento es obligatorio"
            resumen.color = ft.Colors.RED_400
            page.update()
            lista.visible = False
            return
        else:
            resumen.value = ft.Text(
                value="Resumen del evento", color=ft.Colors.BLUE_400, size=30
            )
            resumen.value = f"Resumen del evento:\n Nombre: {nombre.value}, Tipo: {opcion.value}, Modalidad: {modalidad.value}, Requiere inscripción: {inscripcion.value}, Duración: {hora.value} horas, Fecha: {fecha.value.strftime('%Y-%m-%d')}"
            lista.controls.append(ft.Text(f"Evento: {nombre.value}, Tipo: {opcion.value}, Modalidad: {modalidad.value}, Requiere inscripción: {inscripcion.value}, Duración: {hora.value} horas, Fecha: {fecha.value.strftime('%Y-%m-%d')}", color=ft.Colors.GREEN_400))
            opcion.value = None
            modalidad.value = None
            inscripcion.value = False
            hora.value = 1
            fecha.value = datetime.now()
            nombre.value = ""
            page.update()
    
    boton=(ft.ElevatedButton
        ("Crear evento", 
        on_click=evento,
        bgcolor=ft.Colors.GREEN_400,
        color=ft.Colors.WHITE  
        ))
    
    
    def eventos():
        if not lista.controls:
            lista.value ="No hay eventos creados"
            lista.color = ft.Colors.RED_400
            page.update()
            return
        else:
            lista.visible = True
            lista.color = ft.Colors.BLUE_400
            page.update()
        
    resumen.on_change=evento
    lista.on_change=evento
    
    ver = ft.ElevatedButton(
        "Ver eventos",
        on_click=eventos,
        bgcolor=ft.Colors.BLUE_400,
        color=ft.Colors.WHITE
    )
    
    fecha = ft.DatePicker(
        first_date=datetime(2020, 1, 1),
        last_date=datetime(2030, 12, 31),
        value=datetime.now(),
    )
    
    
    def abrir_fecha(e):
        fecha.open = True
        page.update()

    page.overlay.append(fecha)
    
    selfecha = ft.ElevatedButton(
        "Seleccionar fecha",
        on_click=lambda e: abrir_fecha(e),
        bgcolor=ft.Colors.BLUE_400,
        color=ft.Colors.WHITE
    )
    
    
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
                ft.Row([ft.Text("Fecha del evento"), selfecha]),
                boton,
                ver
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )

    page.add(ft.Divider(height=10,thickness=10,color=ft.Colors.BLUE_400))
    
    page.add(ft.Row(resumen))
    
    page.add(ft.Row(lista))
    
    
    

ft.run(main)