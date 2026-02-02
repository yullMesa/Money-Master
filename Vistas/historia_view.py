import flet as ft

def obtener_historia_view(page):
    datos_historia = [
        {
            "titulo": "1. El Trueque Silencioso",
            "info": "Prehistoria: El intercambio directo de bienes era la base de la economía antes de existir el concepto de moneda.",
            "imagen": "Historia/Prehistoria.png" 
        },
        {
            "titulo": "2. La Mercancia como dinero",
            "info": "9000 a.C.: Elementos como la sal, el ganado y los granos se vuelven el primer estándar de valor aceptado.",
            "imagen": "Historia/Ganado.png"
        },
        {
            "titulo": "3. China y su impacto monetario",
            "info": "1200 a.C. (China): Aparecen las conchas de cauri (pequeños caracoles marinos). Fueron la moneda de mayor uso y duración en la historia, extendiéndose por África y Asia.",
            "imagen": "Historia/Concha.png"
        }
        ,
        {
            "titulo": "4. El nacimiento de la moneda metálica",
            "info": "1000 a.C. (China): Se empezaron a fabricar réplicas de las conchas de cauri en bronce. También hacían monedas con forma de cuchillos o herramientas.",
            "imagen": "Historia/MonedaMetal.png"
        },
        {
            "titulo": "5. Turquía y las primeras monedas oficiales",
            "info": "600 a.C. (Lidia, actual Turquía): El gran salto. Se acuñan las primeras monedas oficiales de una mezcla de oro y plata llamada electro. Al tener el sello de un rey, ya no tenías que pesar el metal cada vez; el sello garantizaba su valor.",
            "imagen": "Historia/turquia.png"
        },
        {
            "titulo": "6. Papel y bancos",
            "info": "Siglo VII - XI (China): Durante la dinastía Tang y Song, los mercaderes se cansaron de cargar monedas pesadas. Empezaron a dejar su metal con 'custodios' y a cambio recibían un recibo de papel. ¡Había nacido el billete!",
            "imagen": "Historia/China.png"
        },
        {
            "titulo": "7. Europa y el auge del papel moneda",
            "info": "Siglo VII - XI (China): Durante la dinastía Tang y Song, los mercaderes se cansaron de cargar monedas pesadas. Empezaron a dejar su metal con 'custodios' y a cambio recibían un recibo de papel. ¡Había nacido el billete!",
            "imagen": "Historia/China.png"
        }
    ]
    
    indice = [0]

    # --- ELEMENTOS VISUALES CON ESTILO ---
    img_hitos = ft.Image(
        src=datos_historia[0]["imagen"], 
        width=500, 
        height=300, 
        fit="contain",
        border_radius=15
    )
    
    lbl_titulo = ft.Text(
        datos_historia[0]["titulo"], 
        size=35, 
        weight="bold", 
        color="#00F2FF" # Cyan Neón
    )
    
    lbl_info = ft.Text(
        datos_historia[0]["info"], 
        size=18, 
        color="white", 
        text_align="center"
    )

    def cambiar_paso(direccion):
        nuevo_indice = indice[0] + direccion
        if 0 <= nuevo_indice < len(datos_historia):
            indice[0] = nuevo_indice
            img_hitos.src = datos_historia[indice[0]]["imagen"]
            lbl_titulo.value = datos_historia[indice[0]]["titulo"]
            lbl_info.value = datos_historia[indice[0]]["info"]
            page.update()

    # --- DISEÑO DE LA "TARJETA" ---
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("LÍNEA DE TIEMPO FINANCIERA", size=12, color="grey500", weight="bold"),
                ft.Divider(height=10, color="transparent"),
                img_hitos,
                lbl_titulo,
                ft.Container(
                    content=lbl_info, 
                    width=600, 
                    padding=20,
                    bgcolor="#1A1C23", # Un gris muy oscuro para resaltar el texto
                    border_radius=10
                ),
                ft.Divider(height=20, color="transparent"),
                ft.Row(
                    [
                        ft.ElevatedButton(
                            "  ← ANTERIOR  ", 
                            on_click=lambda _: cambiar_paso(-1),
                            bgcolor="grey800",
                            color="white"
                        ),
                        ft.ElevatedButton(
                            "  SIGUIENTE →  ", 
                            on_click=lambda _: cambiar_paso(1),
                            bgcolor="#00F2FF",
                            color="black"
                        ),
                    ],
                    alignment="center",
                    spacing=30
                )
            ],
            horizontal_alignment="center",
            spacing=10
        ),
        padding=40,
        expand=True
    )