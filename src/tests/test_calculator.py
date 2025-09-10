"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from src.calculator import Calculator

def test_app():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

def test_addition():
    my_calculator = Calculator()
    assert my_calculator.addition(2, 3) == 5
    assert my_calculator.addition(-1, 1) == 0
    assert my_calculator.addition(0, 0) == 0

def test_subtraction():
    my_calculator = Calculator()
    assert my_calculator.subtraction(5, 3) == 2
    assert my_calculator.subtraction(0, 0) == 0
    assert my_calculator.subtraction(-1, -1) == 0

def test_multiplication():
    my_calculator = Calculator()
    assert my_calculator.multiplication(2, 3) == 6
    assert my_calculator.multiplication(-1, 1) == -1
    assert my_calculator.multiplication(0, 100) == 0

def test_division():
    my_calculator = Calculator()
    assert my_calculator.division(6, 3) == 2
    assert my_calculator.division(-4, 2) == -2
    assert my_calculator.division(5, 0) == "Erreur : division par zéro"
