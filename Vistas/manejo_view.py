import flet as ft

def obtener_manejo_view(page):
    # Lista de consejos clave
    consejos = [
        {
            "icon": "💰",
            "titulo": "La Regla 50/30/20",
            "desc": "Divide tus ingresos: 50% Necesidades, 30% Gustos y 20% Ahorro. Es el cimiento de la paz financiera."
        },
        {
            "icon": "🛡️",
            "titulo": "Fondo de Emergencia",
            "desc": "Guarda de 3 a 6 meses de tus gastos básicos. Este es tu escudo contra imprevistos y deudas."
        },
        {
            "icon": "📈",
            "titulo": "Inversión Temprana",
            "desc": "No ahorres lo que te sobra después de gastar; gasta lo que te sobra después de invertir."
        },
        {
            "icon": "🛑",
            "titulo": "Evita Deuda Mala",
            "desc": "Si algo no te genera dinero o no es una necesidad vital, no lo compres con crédito."
        }
    ]

    # Función para crear cada tarjeta de consejo
    def crear_tarjeta(consejo):
        return ft.Container(
            content=ft.Column([
                ft.Text(consejo["icon"], size=40),
                ft.Text(consejo["titulo"], size=22, weight="bold", color="#00F2FF"),
                ft.Text(consejo["desc"], size=14, color="white70", text_align="center"),
            ], horizontal_alignment="center", spacing=10),
            bgcolor="#1A1C23",
            padding=20,
            border_radius=15,
            width=280,
            height=220,
            border=ft.border.all(1, "white10")
        )

    # Diseño final de la vista
    return ft.Container(
        content=ft.Column([
            ft.Text("DOMINA TU DINERO", size=30, weight="bold", color="white"),
            ft.Text("Principios básicos para una vida financiera saludable", size=16, color="grey400"),
            ft.Divider(height=30, color="transparent"),
            
            # Grid de tarjetas
            ft.Row([
                crear_tarjeta(consejos[0]),
                crear_tarjeta(consejos[1]),
            ], alignment="center", spacing=20),
            
            ft.Row([
                crear_tarjeta(consejos[2]),
                crear_tarjeta(consejos[3]),
            ], alignment="center", spacing=20),
            
        ], horizontal_alignment="center", spacing=10),
        padding=40,
        expand=True
    )