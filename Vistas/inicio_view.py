import flet as ft
import random

def obtener_inicio_view(page):
    # Definimos la frase directamente para evitar errores de random por ahora
    frases = [
        "El dinero es un excelente esclavo, pero un pésimo amo.",
        "Cuida de los pequeños gastos; un pequeño agujero hunde un barco.",
        "No ahorres lo que te sobra después de gastar, gasta lo que te sobra después de ahorrar.",
        "La mejor inversión que puedes hacer es en ti mismo.",
        "El precio es lo que pagas, el valor es lo que recibes.",
        "Nunca dependas de una sola fuente de ingresos.",
        "Si compras cosas que no necesitas, pronto tendrás que vender cosas que necesitas.",
        "La riqueza no consiste en tener grandes posesiones, sino en tener pocas necesidades.",
        "El camino a la riqueza depende de dos palabras: trabajo y ahorro.",
        "No pongas todos los huevos en la misma cesta.",
        "La libertad financiera consiste en vivir con tus propios términos.",
        "El interés compuesto es la octava maravilla del mundo.",
        "Regla número 1: Nunca pierdas dinero. Regla número 2: Nunca olvides la regla número 1.",
        "Compra solo lo que estarías feliz de tener si el mercado cerrara durante 10 años."
    ]

    frase_dia = random.choice(frases)

    # Agregando un Container simple
    return ft.Column(
        [
            ft.Container(height=40),  # Solo espaciado
            ft.Text("MONEY MASTER", size=45, weight="bold", color="white"),
            ft.Text("Tu guía hacia la libertad financiera", size=18, color="grey"),
            ft.Container(height=30),  # Espaciado
            ft.Container(
                content=ft.Text(frase_dia, size=18, color="white", italic=True, text_align="center"),
                bgcolor="#1A1C23",
                padding=20,
                border_radius=10
            ),
            ft.Container(height=30),  # Espaciado
            ft.Text("Usa el menú lateral para navegar", color="grey700", size=14),
        ],
        horizontal_alignment="center",
        spacing=10,
        scroll="auto"
    )