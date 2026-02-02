import flet as ft

def obtener_glosario_view(page):
    # 1. EL DICCIONARIO: Aquí es donde agregas más palabras
    terminos = [
        {"palabra": "INFLACIÓN", "def": "El dinero pierde valor y todo sube.", "ej": "Ej: Antes un dulce costaba $100, hoy cuesta $500."},
        {"palabra": "ACTIVOS", "def": "Cosas que ponen dinero en tu bolsillo.", "ej": "Ej: Un negocio o una inversión."},
        {"palabra": "PASIVOS", "def": "Cosas que sacan dinero de tu bolsillo.", "ej": "Ej: Deudas o gastos innecesarios."},
        # Para agregar otro, solo copia la línea de abajo y cambia los textos:
        {"palabra": "AHORRO", "def": "Dinero guardado para el futuro.", "ej": "Ej: Guardar el 10% de tu sueldo."},
        {"palabra": "INVERSIÓN", "def": "Usar dinero para ganar más dinero.", "ej": "Ej: Comprar acciones o bienes raíces."},
        {"palabra": "PRESUPUESTO", "def": "Planificar tus ingresos y gastos.", "ej": "Ej: Asignar dinero para comida, transporte, etc."},
        {"palabra": "DIVERSIFICACIÓN", "def": "No poner todos los huevos en la misma canasta.", "ej": "Ej: Invertir en diferentes tipos de activos."},
        {"palabra": "LIQUIDEZ", "def": "Qué tan rápido puedes convertir un activo en efectivo.", "ej": "Ej: El dinero en efectivo es muy líquido, una casa no tanto."},
        {"palabra": "RIESGO", "def": "La posibilidad de perder dinero en una inversión.", "ej": "Ej: Invertir en acciones puede ser riesgoso."},
        {"palabra": "RENTABILIDAD", "def": "La ganancia que obtienes de una inversión.", "ej": "Ej: Si inviertes $1000 y ganas $100, tu rentabilidad es del 10%."},
        {"palabra": "CRÉDITO", "def": "Dinero prestado que debes devolver con intereses.", "ej": "Ej: Usar una tarjeta de crédito para comprar ahora y pagar después."},
        {"palabra": "INTERÉS COMPUESTO", "def": "Ganar intereses sobre los intereses ya ganados.", "ej": "Ej: Invertir $1000 a una tasa del 5% anual, después de un año tienes $1050, el próximo año ganas interés sobre $1050."}
    ]

    # Variables para los textos de abajo
    lbl_def = ft.Text("Selecciona un término", size=20, color="white", weight="bold")
    lbl_ej = ft.Text("", size=16, color="#00F2FF", italic=True)

    def seleccionar(t):
        lbl_def.value = t["def"]
        lbl_ej.value = t["ej"]
        page.update()

    # 2. CREACIÓN DE BOTONES: No tocamos esto, se hace solo
    lista_botones = []
    for t in terminos:
        lista_botones.append(
            ft.Container(
                content=ft.Text(t["palabra"], color="black", weight="bold"),
                bgcolor="#00F2FF",
                padding=15,
                border_radius=8,
                on_click=lambda e, term=t: seleccionar(term),
            )
        )

    # 3. EL DISEÑO (Aquí está el truco del 'wrap' para que no se amontonen)
    return ft.Column(
        [
            ft.Text("DICCIONARIO FINANCIERO", size=30, weight="bold", color="white"),
            
            # El Row con wrap=True hace que los botones bajen solitos si no caben
            ft.Row(
                controls=lista_botones, 
                alignment="center", 
                spacing=15, 
                wrap=True  # <--- ESTO evita que se amontonen
            ),
            
            ft.Container(height=20),
            
            # Cuadro de resultados
            ft.Container(
                content=ft.Column([
                    lbl_def,
                    ft.Divider(color="white24"),
                    lbl_ej
                ], horizontal_alignment="center"),
                bgcolor="#1A1C23",
                padding=40,
                border_radius=15,
                width=600,
            )
        ],
        horizontal_alignment="center",
        spacing=20,
        scroll="auto" # Esto permite bajar si hay muchos términos
    )