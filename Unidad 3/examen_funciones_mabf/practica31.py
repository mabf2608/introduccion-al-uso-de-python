#Miguel Ángel Bonilla Fernández 2º DAM

def convertir_acciones(compania: str, cantidad: int, unidad: str) -> float:
    companias_validas = ("NVDA", "SONY", "BMW")
    unidades_validas = ("euro", "dolar", "libra")

    compania = compania.upper()
    unidad = unidad.lower()

    if compania not in companias_validas:
        raise ValueError("Las compañías válidas son NVDA, SONY y BMW.")
    if unidad not in unidades_validas:
        raise ValueError("Las unidades válidas son euro, dolar y libra.")

    aux = 0.0

    if unidad == "euro":
        if compania == "NVDA":
            aux = 156.20 * cantidad
        elif compania == "SONY":
            aux = 24.16 * cantidad
        elif compania == "BMW":
            aux = 58.12 * cantidad
    elif unidad == "dolar":
        if compania == "NVDA":
            aux = (156.20 * 1.1) * cantidad
        elif compania == "SONY":
            aux = (24.16 * 1.1) * cantidad
        elif compania == "BMW":
            aux = (58.12 * 1.1) * cantidad
    elif unidad == "libra":
        if compania == "NVDA":
            aux = (156.20 * 0.83) * cantidad
        elif compania == "SONY":
            aux = (24.16 * 0.83) * cantidad
        elif compania == "BMW":
            aux = (58.12 * 0.83) * cantidad

    return round(aux, 2)

print(convertir_acciones("nvdA", 10, "EuRO"))
print(convertir_acciones("sOny", 5, "DOLAr"))
print(convertir_acciones("bMw", 20, "LiBRA"))