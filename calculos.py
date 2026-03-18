def calcular_mezcla_completa(largo, ancho, altura, ra, rb, piezas, costo_kit, peso_kit, porcentaje_ganancia):
    try:
        # Volumen y peso base (Densidad 1.1)
        vol_un = float(largo) * float(ancho) * float(altura)
        gramos_un = vol_un * 1.1
        total_g = gramos_un * int(piezas)
        
        # Proporciones A y B
        t_partes = float(ra) + float(rb)
        g_a = (total_g * float(ra)) / t_partes
        g_b = (total_g * float(rb)) / t_partes
        
        # Finanzas: Cálculo de costo
        c_por_g = float(costo_kit) / float(peso_kit)
        c_obra = total_g * c_por_g
        
        # Finanzas: Precio de venta basado en el % de ganancia deseado
        margen_decimal = float(porcentaje_ganancia) / 100
        if margen_decimal >= 1: 
            margen_decimal = 0.99 # Evitar que la app colapse si pone 100% o más por error
            
        v_total = c_obra / (1 - margen_decimal)
        
        return {
            "total": round(total_g, 1),
            "a": round(g_a, 1),
            "b": round(g_b, 1),
            "unidad": round(gramos_un, 1),
            "costo": round(c_obra, 2),
            "v_total": round(v_total, 2),
            "v_un": round(v_total / int(piezas), 2)
        }
    except Exception:
        return None