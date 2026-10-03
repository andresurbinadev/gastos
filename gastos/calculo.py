
def total(gastos):
    for g in gastos:
        if g<0:
            raise ValueError("Monto negativo")
    resultado = round(sum(gastos),2)
    return resultado

def promedio(gastos):
    if len(gastos) == 0:
        raise ValueError("No se puede calcular el promedio de una lista vacía")
    resultado = round(total(gastos)/len(gastos),2)
    return resultado