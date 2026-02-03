import flet as ft
import datetime
import json
import os

ARCHIVO_DATOS = "historial_financiero.json"

def guardar_en_disco(datos):
    # Lógica de autolimpieza: máximo 12 archivos/registros
    if len(datos) > 12:
        datos = datos[-12:]
    with open(ARCHIVO_DATOS, "w") as f:
        json.dump(datos, f)

def cargar_de_disco():
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "r") as f:
            return json.load(f)
    return []

def obtener_registro_view(page):
    lista_meses_ui = ft.Column(spacing=10, width=600)
    panel_analisis = ft.Container(padding=20, border_radius=15, width=600)

    # 1. CAMPOS DE TEXTO DIRECTOS (Para que el usuario suba la info)
    txt_fecha = ft.TextField(label="1. Fecha (Año-Mes)", value=datetime.datetime.now().strftime("%Y-%m"), width=140)
    txt_ingreso = ft.TextField(label="2. Ingreso ($)", width=140)
    txt_gasto = ft.TextField(label="3. Gasto ($)", width=140)

    def actualizar_interfaz():
        lista_meses_ui.controls.clear()
        datos = cargar_de_disco()
        
        if not datos:
            panel_analisis.content = ft.Text("ESPERANDO DATOS...", color="white", weight="bold")
            panel_analisis.bgcolor = "#333333"
        else:
            total_in = sum(float(m["ingreso"]) for m in datos)
            total_out = sum(float(m["gasto"]) for m in datos)
            saldo = total_in - total_out
            
            # Diagnóstico de salud financiera
            if saldo < 0:
                msg = f"ESTADO: CRÍTICO 🚨\nSaldo total: -${abs(saldo)}"
                bg = "#FF4444"
            else:
                msg = f"ESTADO: SALUDABLE ✅\nSaldo total: +${saldo}"
                bg = "#00F2FF"

            panel_analisis.bgcolor = bg
            panel_analisis.content = ft.Text(msg, color="black", weight="bold", size=20, text_align="center")

            for m in reversed(datos):
                diff = float(m["ingreso"]) - float(m["gasto"])
                color_txt = "red" if diff < 0 else "green"
                lista_meses_ui.controls.append(
                    ft.Container(
                        content=ft.Row([
                            ft.Text(m["fecha"], weight="bold", width=100),
                            ft.Text(f"IN: ${m['ingreso']}", color="green", expand=True),
                            ft.Text(f"OUT: ${m['gasto']}", color="red", expand=True),
                            ft.Text(f"${diff}", color=color_txt, weight="bold")
                        ]),
                        bgcolor="#1A1C23", padding=15, border_radius=10
                    )
                )
        page.update()

    # 2. BOTÓN DE GUARDADO (El cuarto elemento)
    def ejecutar_guardado(e):
        if txt_ingreso.value and txt_gasto.value:
            actuales = cargar_de_disco()
            actuales.append({
                "fecha": txt_fecha.value,
                "ingreso": txt_ingreso.value,
                "gasto": txt_gasto.value
            })
            guardar_en_disco(actuales)
            # Limpiar campos para nueva entrada
            txt_ingreso.value = ""
            txt_gasto.value = ""
            actualizar_interfaz()

    btn_guardar = ft.ElevatedButton(
        "4. GUARDAR Y ANALIZAR", 
        icon="check",
        on_click=ejecutar_guardado,
        style=ft.ButtonStyle(color="black", bgcolor="#FFFFFF")
    )

    actualizar_interfaz()

    # DISEÑO FINAL: Formulario arriba, lista abajo
    return ft.Column(
        [
            ft.Container(height=20),
            ft.Text("CONSULTORIO FINANCIERO", size=30, weight="bold", color="#00F2FF"),
            panel_analisis,
            ft.Container(height=20),
            
            # Fila con los 4 elementos que pediste
            ft.Row([
                txt_fecha,
                txt_ingreso,
                txt_gasto,
                btn_guardar
            ], alignment="center", spacing=10),
            
            ft.Text("Se mantienen los últimos 12 registros en el archivo local", size=10, color="grey"),
            ft.Container(height=20),
            lista_meses_ui
        ],
        horizontal_alignment="center", scroll="auto"
    )