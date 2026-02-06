import flet as ft
from sidebar import construir_sidebar
from Vistas.historia_view import obtener_historia_view
from Vistas.manejo_view import obtener_manejo_view
from Vistas.glosario_view import obtener_glosario_view
from Vistas.metas_view import obtener_metas_view
from Vistas.inicio_view import obtener_inicio_view
import time

import sidebar
from Vistas.registro_view import obtener_registro_view
from database import inicializar_db
from Vistas.graficos_view import obtener_graficos_view

def main(page: ft.Page):
    # --- CONFIGURACIÓN UNIVERSAL ---
    inicializar_db()
    page.title = "Money Master Pro"
    page.bgcolor = "#0B0E14"
    page.padding = 0
    
    # En lugar de WindowState (que falla), usamos el comando directo:
    page.window_maximized = True 

    # Agregamos expand=True para que no se colapse el contenido
    area_contenido = ft.Column(expand=True, horizontal_alignment="center", scroll="auto")

    def actualizar_vista(nombre_vista):
        print(f"DEBUG: Cambiando a vista: {nombre_vista}")  # ← DEBUG
        area_contenido.controls.clear()
        
        if nombre_vista == "historia":
            area_contenido.controls.append(obtener_historia_view(page))
        elif nombre_vista == "manejo":
            area_contenido.controls.append(obtener_manejo_view(page))
        elif nombre_vista == "glosario":
            area_contenido.controls.append(obtener_glosario_view(page))
        elif nombre_vista == "metas":
            area_contenido.controls.append(obtener_metas_view(page))
        elif nombre_vista == "inicio":
            area_contenido.controls.append(obtener_inicio_view(page))
        elif nombre_vista == "registro":
            area_contenido.controls.append(obtener_registro_view(page))
        elif nombre_vista == "graficos":
            area_contenido.controls.append(obtener_graficos_view(page))
        
        # IMPORTANTE: Solo usamos page.update(). 
        # Borra la línea que dice area_contenido.update()
        page.update()

    def entrar_al_sistema(e):
        page.controls.clear()
        
        # Creamos el layout
        layout = ft.Row(
            controls=[
                construir_sidebar(page, actualizar_vista),
                ft.VerticalDivider(width=1, color="white10"),
                area_contenido,
            ],
            expand=True
        )
        
        page.add(layout)
        page.update()
        
        # Ahora cargamos la vista de inicio usando actualizar_vista
        actualizar_vista("inicio")

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
