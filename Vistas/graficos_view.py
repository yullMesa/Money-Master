import flet as ft
from database import obtener_movimientos

def obtener_graficos_view(page):
    datos = obtener_movimientos()
    
    if not datos:
        return ft.Column([ft.Text("Registra datos para ver el análisis")], alignment="center")

    datos_grafica = list(reversed(datos))
    
    # Buscamos el valor más alto para escalar las barras (ej: 3200)
    max_valor = max(max(d["ingreso"], d["gasto"]) for d in datos)
    altura_maxima = 250 # Píxeles de alto para la barra más grande

    filas_barras = []
    
    for d in datos_grafica:
        # Calculamos la altura proporcional de cada barra
        alto_in = (d["ingreso"] / max_valor) * altura_maxima
        alto_out = (d["gasto"] / max_valor) * altura_maxima
        
        filas_barras.append(
            ft.Column([
                ft.Row([
                    # Barra de Ingreso
                    ft.Container(
                        width=15, height=alto_in, bgcolor="green", 
                        border_radius=ft.border_radius.only(top_left=5, top_right=5),
                        tooltip=f"Ingreso: ${d['ingreso']}"
                    ),
                    # Barra de Gasto
                    ft.Container(
                        width=15, height=alto_out, bgcolor="red", 
                        border_radius=ft.border_radius.only(top_left=5, top_right=5),
                        tooltip=f"Gasto: ${d['gasto']}"
                    ),
                ], alignment="end", spacing=2),
                ft.Text(d["fecha"][-2:], size=10, color="grey") # Solo el mes
            ], horizontal_alignment="center", alignment="end")
        )

    return ft.Column(
        [
            ft.Container(height=20),
            ft.Text("ANÁLISIS DE FLUJO", size=30, weight="bold", color="#00F2FF"),
            
            # Tarjeta de Resumen con tus datos reales de SQL
            ft.Container(
                content=ft.Row([
                    ft.Column([ft.Text("GANADO", size=10), ft.Text("$26,000", color="green", weight="bold")], horizontal_alignment="center"),
                    ft.VerticalDivider(),
                    ft.Column([ft.Text("GASTADO", size=10), ft.Text("$21,950", color="red", weight="bold")], horizontal_alignment="center"),
                    ft.VerticalDivider(),
                    ft.Column([ft.Text("BALANCE", size=10), ft.Text("$4,050", color="#00F2FF", weight="bold")], horizontal_alignment="center"),
                ], alignment="space_around"),
                bgcolor="#1A1C23", padding=20, border_radius=15, width=600
            ),
            
            ft.Container(height=30),
            
            # El Gráfico Manual (Imposible que falle)
            ft.Container(
                content=ft.Row(filas_barras, alignment="center", spacing=20, vertical_alignment="end"),
                bgcolor="#14151a", padding=30, border_radius=15, height=350, width=650
            ),
            
            ft.Row([
                ft.Row([ft.Container(width=12, height=12, bgcolor="green",), ft.Text("Ingresos",color="white")]),
                ft.Container(width=30),
                ft.Row([ft.Container(width=12, height=12, bgcolor="red"), ft.Text("Gastos", color="white")]),
            ], alignment="center")
        ],
        horizontal_alignment="center",
        scroll="auto"
    )