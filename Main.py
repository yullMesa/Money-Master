import flet as ft
from sidebar import construir_sidebar
from Vistas.historia_view import obtener_historia_view
from Vistas.manejo_view import obtener_manejo_view
from Vistas.glosario_view import obtener_glosario_view

def main(page: ft.Page):
    # --- CONFIGURACIÓN UNIVERSAL ---
    page.title = "Money Master Pro"
    page.bgcolor = "#0B0E14"
    page.padding = 0
    
    # En lugar de WindowState (que falla), usamos el comando directo:
    page.window_maximized = True 

    area_contenido = ft.Column(expand=True, horizontal_alignment="center", scroll="auto")

    def actualizar_vista(nombre_vista):
        area_contenido.controls.clear()
        
        if nombre_vista == "historia":
         area_contenido.controls.append(obtener_historia_view(page))

        elif nombre_vista == "manejo":
            area_contenido.controls.append(obtener_manejo_view(page))
            
        elif nombre_vista == "glosario":
            area_contenido.controls.append(obtener_glosario_view(page))
        page.update()

    def entrar_al_sistema(e):
        page.controls.clear()
        layout = ft.Row(
            controls=[
                construir_sidebar(page, actualizar_vista), 
                ft.VerticalDivider(width=1, color="white10"),
                area_contenido
            ],
            expand=True
        )
        page.add(layout)
        actualizar_vista("historia")

    # Pantalla inicial simple para evitar errores de iconos
    # PANTALLA INICIAL PARA VERSIÓN 0.80.5
    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        ft.Text("MONEY MASTER", size=60, weight="bold", color="#00F2FF"),
                        ft.ElevatedButton(
                            "ENTRAR AL SISTEMA",
                            on_click=entrar_al_sistema,
                            width=250,
                            height=50
                        )
                    ],
                    alignment="center",
                    horizontal_alignment="center",
                )
            ],
            alignment="center", # Esto centra la columna horizontalmente
            vertical_alignment="center", # Esto centra la columna verticalmente
            expand=True # Esto hace que ocupe toda la pantalla
        )
    )

# El comando 'app' sigue siendo el más estable para escritorio
ft.app(target=main, assets_dir="assets")
