from ej5a1 import Student


def test_estudiante():
    estudiante = Student("Juan", 25, 8.0)
    assert (
        estudiante.describe() == "Name: Juan, Age: 25, Average: 8.0"
    ), "Incorrect student description"
    estudiante.grade(9.0)
    assert estudiante.average == 8.5, "Incorrect average after grading"
    assert (
        estudiante.describe() == "Name: Juan, Age: 25, Average: 8.5"
    ), "Incorrect student description after grading"
