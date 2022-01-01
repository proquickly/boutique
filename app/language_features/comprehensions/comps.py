names = [name.capitalize() for name in ("andy", "sue", "pete")]
assert names == ["Andy", "Sue", "Pete"]

some_names = [name for name in names if name[0] != "S"]
assert some_names == ["Andy", "Pete"]

some_names.append(sum([num for num in range(0, 20, 4)]))
assert some_names == ["Andy", "Pete", 40]

names_with_id = {key + 1: value for key, value in enumerate(["Andy", "Sue", "Pete"])}

assert names_with_id == {1: "Andy", 2: "Sue", 3: "Pete"}

numbers = list(range(10)) + list(range(20))
assert numbers == [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
]

two_multiples = {number for number in numbers if number % 2 == 0}
assert two_multiples == {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
