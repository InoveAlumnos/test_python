#!/usr/bin/env python
'''
Test is even [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba la función is_even
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


from number import is_even

def test_is_even():
    """ Test si el número 4 es determinado par"""
    number = 4
    assert is_even(number) == True, '4 debería haber sido determinado par'
