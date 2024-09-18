

# 1. Creación de la Función calcular_descuento

def calcular_descuento(monto_total, porcentaje_descuento=30):
    """
    :param monto_total: El monto total de la compra
    :param porcentaje_descuento: El porcentaje de descuento a aplicar (por defecto es 30%)v
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    monto_final = monto_total - descuento
    return descuento, monto_final


# 2. Llamada a la Función y Resultados


  # Primera llamada con el valor predeterminado del porcentaje (30%)
monto_total = 150
print(monto_total)
descuento, monto_final = calcular_descuento(monto_total)
print(f"Compra de {monto_total} con descuento del 30%: Descuento = {descuento}, Importe Total = {monto_final}")

# Segunda llamada con un porcentaje de descuento 25%
porcentaje_descuento = 25
descuento, monto_final = calcular_descuento(monto_total, porcentaje_descuento)
print(f"Compra de {monto_total} con descuento del {porcentaje_descuento}%: Descuento = {descuento}, Importe Total = {monto_final}")