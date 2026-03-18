import flet as ft
from calculos import calcular_mezcla_completa

def main(page: ft.Page):
    # --- CONFIGURACIÓN ESTABLE ---
    page.title = "jacobo Epoxy"
    page.scroll = "always"
    page.padding = 30
    page.window_width = 450
    page.window_height = 800
    
    # Paleta de Colores Pastel Segura (Hexadecimales)
    color_fondo = "#FFF0F5"       # Lavender Blush (Fondo principal muy claro)
    color_tarjeta = "#FFFFFF"     # Blanco puro para los contenedores
    color_texto = "#4A4A4A"       # Gris oscuro (más suave que el negro puro)
    color_titulo = "#D81B60"      # Rosa fuerte/Frambuesa para acentos
    color_boton = "#F48FB1"       # Rosa pastel vivo para el botón principal
    color_divisor = "#FFCDD2"     # Rosa muy pálido para líneas divisorias

    page.bgcolor = color_fondo

    # --- LÓGICA DE PROCESAMIENTO ---
    def procesar(e):
        res = calcular_mezcla_completa(
            i_l.value, i_an.value, i_al.value,
            i_ra.value, i_rb.value, i_pz.value,
            i_costo.value, i_peso.value, i_margen.value
        )
        if res:
            txt_res_peso.value = f"TOTAL A PREPARAR: {res['total']} g"
            txt_res_mezcla.value = f"Resina (A): {res['a']} g  |  Catalizador (B): {res['b']} g"
            txt_res_costo.value = f"Costo de Producción: ${res['costo']}"
            txt_res_venta.value = f"Venta Total Sugerida: ${res['v_total']}"
            txt_res_unidad.value = f"PRECIO POR UNIDAD: ${res['v_un']}"
            tarjeta_resultados.bgcolor = "#FFE4E1" # MistyRose: Cambia ligeramente de color al tener éxito
        else:
            txt_res_peso.value = "Error en los datos ingresados."
            txt_res_mezcla.value = "Verifica no haber dejado espacios en blanco."
            txt_res_costo.value = ""
            txt_res_venta.value = ""
            txt_res_unidad.value = ""
            tarjeta_resultados.bgcolor = color_tarjeta
        page.update()

    # --- COMPONENTES DE ENTRADA ---
    # Usamos campos simples sin prefix ni helper_text
    i_l = ft.TextField(label="Largo (cm)", value="5", color=color_texto)
    i_an = ft.TextField(label="Ancho (cm)", value="5", color=color_texto)
    i_al = ft.TextField(label="Altura (cm)", value="1", color=color_texto)
    i_pz = ft.TextField(label="Cantidad de Piezas a hacer", value="10", color=color_texto)
    
    i_ra = ft.TextField(label="Proporción A (Resina)", value="2", color=color_texto)
    i_rb = ft.TextField(label="Proporción B (Catalizador)", value="1", color=color_texto)
    
    i_costo = ft.TextField(label="Precio del Kit Total ($)", value="150000", color=color_texto)
    i_peso = ft.TextField(label="Peso del Kit Total (g)", value="1500", color=color_texto)
    i_margen = ft.TextField(label="Tu Margen de Ganancia", value="20", color=color_texto)

    # --- COMPONENTES DE RESULTADOS ---
    txt_res_peso = ft.Text("Los resultados aparecerán aquí", size=18, weight="bold", color=color_titulo)
    txt_res_mezcla = ft.Text("", size=15, color=color_texto)
    txt_res_costo = ft.Text("", size=15, color=color_texto)
    txt_res_venta = ft.Text("", size=15, color=color_texto)
    txt_res_unidad = ft.Text("", size=22, weight="bold", color=color_titulo)

    tarjeta_resultados = ft.Container(
        content=ft.Column([
            txt_res_peso,
            txt_res_mezcla,
            ft.Divider(color=color_divisor),
            txt_res_costo,
            txt_res_venta,
            txt_res_unidad
        ]),
        padding=20,
        bgcolor=color_tarjeta,
        border_radius=15
    )

    # --- CONSTRUCCIÓN DE LA VISTA ---
    page.add(
        ft.Text("Jacobo Epoxy", size=32, weight="bold", color=color_titulo),
        
        ft.Container(height=10),
        ft.Text("DIMENSIONES DEL MOLDE", weight="bold", color=color_texto),
        ft.Row([i_l, i_an, i_al]),
        ft.Row([i_ra, i_rb]),
        i_pz,
        
        ft.Container(height=15),
        ft.Text("FINANZAS DEL NEGOCIO", weight="bold", color=color_texto),
        ft.Row([i_costo, i_peso]),
        # Texto explicativo seguro fuera del TextField
        ft.Text("Ingresa el porcentaje deseado (Ej: 20 para el 20%, 50 para el 50%):", size=12, color=color_texto),
        i_margen,
        
        ft.Container(height=20),
        ft.ElevatedButton(
            "CALCULAR PROYECTO", 
            on_click=procesar, 
            bgcolor=color_boton, 
            color="#FFFFFF", # Texto blanco puro en el botón
            width=500, 
            height=55
        ),
        
        ft.Container(height=20),
        tarjeta_resultados,
        
        ft.Container(height=40) # Margen inferior
    )

if __name__ == "__main__":
    ft.app(target=main)