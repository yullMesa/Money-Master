import flet as ft

def obtener_metas_view(page):
    # Campos de entrada (Sin prefix_text para evitar errores)
    txt_meta = ft.TextField(label="¿Qué quieres lograr? (Ej: Moto)", width=300, color="white")
    txt_valor = ft.TextField(label="¿Cuánto cuesta? (Sin puntos ni comas)", width=300, color="white")
    txt_tiempo = ft.TextField(label="¿En cuántos meses lo quieres?", width=300, color="white")
    
    # Etiquetas de resultado
    lbl_resultado = ft.Text("Tu plan de ahorro aparecerá aquí", size=18, color="#00F2FF", weight="bold")
    lbl_diario = ft.Text("", size=16, color="white")

    def calcular_meta(e):
        try:
            # Limpiamos el valor por si el usuario pone símbolos
            valor_limpio = txt_valor.value.replace("$", "").replace(".", "").replace(",", "")
            total = float(valor_limpio)
            meses = float(txt_tiempo.value)
            
            cuota_mensual = total / meses
            cuota_diaria = cuota_mensual / 30
            
            # Usamos formato simple para evitar errores de f-strings complejos
            lbl_resultado.value = "Cuota mensual: $" + "{:,.0f}".format(cuota_mensual)
            lbl_diario.value = "Eso son $" + "{:,.0f}".format(cuota_diaria) + " por día. ¡Tú puedes!"
            page.update()
        except:
            lbl_resultado.value = "Error: Ingresa solo números"
            page.update()

    return ft.Column(
        [
            ft.Text("SIMULADOR DE METAS", size=30, weight="bold", color="white"),
            ft.Text("Convierte tus sueños en un plan real", size=16, color="grey"),
            ft.Container(height=10),
            
            # Formulario en una tarjeta oscura
            ft.Container(
                content=ft.Column([
                    txt_meta,
                    txt_valor,
                    txt_tiempo,
                    ft.Container(height=10),
                    # Usamos un botón con 'content' en lugar de 'text' por si acaso
                    ft.ElevatedButton(
                        content=ft.Text("CALCULAR MI PLAN", color="black", weight="bold"),
                        bgcolor="#00F2FF",
                        on_click=calcular_meta,
                        width=300
                    )
                ], horizontal_alignment="center"),
                padding=30,
                bgcolor="#1A1C23",
                border_radius=15
            ),
            
            # Panel de Resultados
            ft.Container(
                content=ft.Column([
                    lbl_resultado,
                    lbl_diario
                ], horizontal_alignment="center"),
                padding=20,
                width=500
            )
        ],
        horizontal_alignment="center",
        spacing=20,
        scroll="auto"
    )