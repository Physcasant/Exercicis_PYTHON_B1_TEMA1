from ej4c4 import Dog, Cat, Parrot


def test_talk_animals():
    perro = Dog("Fido")
    gato = Cat("Felix")
    loro = Parrot("Polly")

    assert perro.talk() == "¡Guau!", "Dog.talk() does not return the correct value for input 'Fido'. It should be '¡Guau!'"
    assert gato.talk() == "¡Meow!", "Cat.talk() does not return the correct value for input 'Felix'. It should be '¡Meow!'"
    assert loro.talk() == "¡Whistle!", "Parrot.talk() does not return the correct value for input 'Polly'. It should be '¡Whistle!'"
    assert perro.name == "Fido", "Dog.name does not return the correct value for input 'Fido'. It should be 'Fido'"
    assert gato.name == "Felix", "Cat.name does not return the correct value for input 'Felix'. It should be 'Felix'"
    assert loro.name == "Polly", "Parrot.name does not return the correct value for input 'Polly'. It should be 'Polly'"
