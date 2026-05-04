
def test_dict():
    target = {'a':1, 'b':2, 'c':3}
    assert 2 in target

def test_list():
    target = [1,2,3]
    assert 2 in target

def test_tuple():
    target = (1,2)
    assert 2 in target