def procesar_inventario(lista_productos):
    pedidos_urgentes = []
    valor_total_inventario = 0.0
    informe_productos = []

    for producto in lista_productos:
        nombre = producto["nombre"]
        cantidad = producto["cantidad"]
        precio = producto["precio"]
        
        # 1. Calcular valor total del inventario general
        valor_total_inventario += cantidad * precio
        
        # 2. Identificar productos con poco stock (< 5)
        if cantidad < 5:
            pedidos_urgentes.append(nombre)
            
        # 3. Aplicar etiqueta / Clasificación Premium (Si cuesta más de 100)
        tipo = "Premium" if precio > 100 else "Estándar"
        
        informe_productos.append({
            "nombre": nombre,
            "tipo": tipo,
            "subtotal": cantidad * precio
        })
        
    # Retornamos un diccionario con los datos estructurados para el informe
    return {
        "pedidos_urgentes": pedidos_urgentes,
        "valor_total_inventario": valor_total_inventario,
        "detalle_productos": informe_productos
    }

# --- EJEMPLO DE USO PRÁCTICO ---
# Esta lista contiene los datos correctos para las pruebas
inventario_almacen = [
    {"nombre": "Sensor Infrarrojo", "cantidad": 3, "precio": 45.0},
    {"nombre": "Placa de Control PLC", "cantidad": 10, "precio": 250.0},
    {"nombre": "Cableado de Cobre (m)", "cantidad": 12, "precio": 15.0},
    {"nombre": "Actuador Hidráulico", "cantidad": 2, "precio": 600.0}
]

# Ejecutamos la función pasando nuestro inventario
resultado = procesar_inventario(inventario_almacen)

# --- IMPRESIÓN DE RESULTADOS EN LA TERMINAL ---
print("\n" + "="*55)
print("       INFORME FINAL DE RENDIMIENTO DEL INVENTARIO")
print("="*55)

# Requerimiento 1: Productos con poco stock
print(f"1. PEDIDOS URGENTES (Stock < 5):\n   -> {resultado['pedidos_urgentes']}\n")

# Requerimiento 2: Valor total de la suma de todo el inventario
print(f"2. VALOR TOTAL DEL INVENTARIO:\n   -> Q{resultado['valor_total_inventario']:.2f}\n")

# Requerimiento 3: Clasificación de productos (Premium / Estándar)
print("3. CLASIFICACIÓN Y DESGLOSE DE PRODUCTOS:")
print("-" * 55)
for prod in resultado["detalle_productos"]:
    print(f" - {prod['nombre']:<22} | {prod['tipo']:<8} | Subtotal: Q{prod['subtotal']:>7.2f}")
print("-" * 55)