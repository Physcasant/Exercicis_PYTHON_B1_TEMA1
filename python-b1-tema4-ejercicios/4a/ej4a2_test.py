from ej4a2 import count_fruits


def test_count_fruits():
    fruits = [
        "apple",
        "banana",
        "orange",
        "apple",
        "kiwi",
        "banana",
        "kiwi",
        "kiwi",
        "kiwi",
    ]
    assert count_fruits(fruits) == {"apple": 2, "banana": 2, "orange": 1, "kiwi": 4}, "count_fruits does not return the correct value for input ['apple', 'banana', 'orange', 'apple', 'kiwi', 'banana', 'kiwi', 'kiwi', 'kiwi']. It should be {'apple': 2, 'banana': 2, 'orange': 1, 'kiwi': 4}"

    fruits = []
    assert count_fruits(fruits) == {}, "count_fruits does not return the correct value for input []. It should be {}, that is, empty"

    fruits = ["apple", "apple", "apple", "apple"]
    assert count_fruits(fruits) == {"apple": 4}, "count_fruits does not return the correct value for input ['apple', 'apple', 'apple', 'apple']. It should be {'apple': 4}"

    fruits = ["apple", "banana", "kiwi"]
    assert count_fruits(fruits) == {"apple": 1, "banana": 1, "kiwi": 1}, "count_fruits does not return the correct value for input ['apple', 'banana', 'kiwi']. It should be {'apple': 1, 'banana': 1, 'kiwi': 1}"
