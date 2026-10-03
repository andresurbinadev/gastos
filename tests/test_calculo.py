import pytest
from gastos.calculo import total

def test_suma_simple():
    assert total([10.5, 4.5]) == 15.0

def test_lista_vacia():
    assert total([]) == 0

def test_decimales():
    assert total([0.1, 0.2]) == 0.3

def test_rechaza_negativos():
    with pytest.raises(ValueError):
        total([10, -3])