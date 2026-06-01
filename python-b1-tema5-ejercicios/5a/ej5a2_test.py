import pytest
from ej5a2 import Animal, Dog, Cat, Duck


def test_dog_sound():
    dog = Dog()
    assert dog.make_sound() == "Woof", "Incorrect dog sound"


def test_cat_sound():
    cat = Cat()
    assert cat.make_sound() == "Meow", "Incorrect cat sound"


def test_duck_sound():
    duck = Duck()
    assert duck.make_sound() == "Quack", "Incorrect duck sound"


def test_animal_abstract_method():
    with pytest.raises(TypeError):
        Animal()  # Esto debe lanzar un error si Animal es realmente abstracta
