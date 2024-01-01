def set_comp():
    return {(integer, integer ** 2)
        for integer in range(1, 100001)
        if integer ** 2 % 3 == 0
    }


def min_max_set(a_set):
    lowest = lowest_possible = float('inf') * -1
    highest = highest_possible = float('inf')
    for set_member in a_set:
        if lowest == lowest_possible or set_member < lowest:
            lowest = set_member
        if highest == highest_possible or set_member > highest:
            highest = set_member
    return lowest, highest


def unique_elems(values):
    if len(values) == len(set(values)):
        return True
    return False


def set_stuff():
    scenario0 = [1, 5, 4, 3, 1, 6]
    unique = set(scenario0)
    assert sorted(list(unique)) == [1, 3, 4, 5, 6]

    scenario1 = set_comp()
    assert (3, 9) in scenario1
    assert (99999, 99999 ** 2) in scenario1
    assert(10, 100) not in scenario1
    assert(0, 0) not in scenario1

    scenario2 = min_max_set({5, 7, 1, 8, 5, 9, 2})
    assert scenario2 == (1, 9)

    scenario3 = unique_elems([3, 4, 5, 2, 5, 1])
    assert scenario3 is False
    scenario3 = unique_elems([3, 4, 5, 2, 7, 1])
    assert scenario3 is True


if __name__ == "__main__":
    set_stuff()
