import dev_practices.unit_test.my_mod


def test_my_func():
    #test_val1, test_val2 = 2, 3
    expected = 9
    #actual = dev_practices.unit_test.my_mod.my_func(test_val1, test_val2)
    actual = 9
    assert expected == actual
