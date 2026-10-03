import pytest
from gastos.calculo import total,promedio

def test_suma_simple():
    assert total([10.5, 4.5]) == 15.0

def test_lista_vacia():
    assert total([]) == 0

def test_decimales():
    assert total([0.1, 0.2]) == 0.3

def test_rechaza_negativos():
    with pytest.raises(ValueError):
        total([10, -3])

def test_promedio_simple():
    assert promedio([10, 20]) == 15

def test_rechaza_negativos_promedio():
    with pytest.raises(ValueError):
        promedio([10, -20])

def test_decimales_promedio():
    assert promedio([10, 10, 10.01]) == 10

def test_lista_vacia_promedio():
    with pytest.raises(ValueError):
        promedio([])