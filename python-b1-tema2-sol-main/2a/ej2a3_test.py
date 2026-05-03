from ej2a3 import add_student_by_reference, add_student_by_value, main

list_students = ["Alice", "Bob", "Juan"]
new_student_by_value = "Maria"
new_student_by_reference = "Sofia"


def test_add_student_by_value():
    assert add_student_by_value(list_students, new_student_by_value) == [
        "Alice",
        "Bob",
        "Juan",
        "Maria",
    ], "add_student_by_value does not return the correct value for input ['Alice', 'Bob', 'Juan'], 'Maria'. It should be ['Alice', 'Bob', 'Juan', 'Maria']"
    assert add_student_by_value(list_students, "Victor") == [
        "Alice",
        "Bob",
        "Juan",
        "Victor",
    ], "add_student_by_value does not return the correct value for input ['Alice', 'Bob', 'Juan'], 'Victor'. It should be ['Alice', 'Bob', 'Juan', 'Victor']"


def test_add_student_by_reference():
    add_student_by_reference(list_students, new_student_by_reference)
    assert list_students == ["Alice", "Bob", "Juan", "Sofia"], "add_student_by_reference does not return the correct value for input ['Alice', 'Bob', 'Juan'], 'Sofia'. It should be ['Alice', 'Bob', 'Juan', 'Sofia']"
    add_student_by_reference(list_students, "Victor")
    assert list_students == ["Alice", "Bob", "Juan", "Sofia", "Victor"], "add_student_by_reference does not return the correct value for input ['Alice', 'Bob', 'Juan', 'Sofia'], 'Victor'. It should be ['Alice', 'Bob', 'Juan', 'Sofia', 'Victor']"


def test_main():
    assert main(list_students, new_student_by_value, new_student_by_reference) == [
        "Alice",
        "Bob",
        "Juan",
        "Sofia",
        "Victor",
        "Sofia",
    ], "main does not return the correct value for input ['Alice', 'Bob', 'Juan'], 'Maria', 'Sofia'. It should be ['Alice', 'Bob', 'Juan', 'Sofia', 'Victor', 'Sofia']"
    assert main(list_students, new_student_by_value, "Carlos") == [
        "Alice",
        "Bob",
        "Juan",
        "Sofia",
        "Victor",
        "Sofia",
        "Carlos",
    ], "main does not return the correct value for input ['Alice', 'Bob', 'Juan'], 'Maria', 'Carlos'. It should be ['Alice', 'Bob', 'Juan', 'Sofia', 'Victor', 'Sofia', 'Carlos']"
