from ej4c1 import Person, Student


# Tests para las clases Person y Student
def test_describe_person():
    # Probamos la clase Person
    p = Person("John", 20)
    assert p.describe() == "John is 20 years old.", "describe does not return the correct value for input Person('John', 20). It should be 'John is 20 years old.'"
    assert p.name == "John", "name does not return the correct value for input Person('John', 20). It should be 'John'"
    assert p.age == 20, "age does not return the correct value for input Person('John', 20). It should be 20"


def test_describe_student():
    # Probamos la clase Student
    s = Student("Mary", 22, "Computer Science")
    assert s.describe() == "Mary is 22 years old. Studies Computer Science.", "describe does not return the correct value for input Student('Mary', 22, 'Computer Science'). It should be 'Mary is 22 years old. Studies Computer Science.'"
    assert s.major == "Computer Science", "major does not return the correct value for input Student('Mary', 22, 'Computer Science'). It should be 'Computer Science'"
    assert isinstance(s, Person), "Student is not a subclass of Person"
