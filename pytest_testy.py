import pytest_funkcje
pytest_funkcje.dodawanie()

from pytest_funkcje import *
import pytest

def test_dodawanie1():
    assert dodawanie(a:3, b:5) == 8
    assert dodawanie(a:3, b:2) == 8

def test_dodawanie2():
    assert dodawanie(a:1, b:1) == 2

def test_mnozenie():
    assert mnozenie(a:10, b:5) == 50
    assert mnozenie(a:10, b:'mama') == None

def test_fissbuzz():
    assert fissbuz(1) == 1
    assert fissbuzz(2) == 2
    assert fissbuzz(3) == 'fiss'

def test_fissbuzz_advanced():
    assert fissbuzz(0) == None
    assert fissbuzz(-5) == None





