import flet as ft

def construir_sidebar(page, cambiar_pantalla_func):
    return ft.Container(
        width=250,
        bgcolor="#151921",
        padding=20,
        content=ft.Column(
            controls=[
                ft.Text("MENÚ", size=15, weight="bold", color="white54"),
                ft.Divider(color="white10"),
                
                # Botones con la sintaxis más simple posible
                ft.TextButton(
                    content=ft.Text("📜 Historia del Dinero", color="white"),
                    on_click=lambda _: cambiar_pantalla_func("historia")
                ),
                
                ft.TextButton(
                    content=ft.Text("📊 Domina Tu Dinero", color="white"),
                    on_click=lambda _: cambiar_pantalla_func("manejo")
                ),

                ft.TextButton(
                content=ft.Text("📖 Glosario", color="white"),
                on_click=lambda _: cambiar_pantalla_func("glosario")
                ),
                ft.TextButton(
                content=ft.Text("🎯 Mis Metas", color="white"),
                on_click=lambda _: cambiar_pantalla_func("metas")
                ),
                ft.TextButton(
                content=ft.Text("📅 Registro", color="white"),
                on_click=lambda _: cambiar_pantalla_func("registro")
                ),
                
            ],
            spacing=15,
        ),
    )