import imported
# only works if no __init__.py in this dir

def test_doit():
    assert imported.doit() == 999
