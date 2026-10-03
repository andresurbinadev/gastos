
def total(gastos):
    for g in gastos:
        if g<0:
            raise ValueError("Monto negativo")
    resultado = round(sum(gastos),2)
    return resultado