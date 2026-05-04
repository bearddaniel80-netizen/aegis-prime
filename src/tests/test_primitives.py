
def test_literal():
    assert 'l' in "Hello World"

def test_bool():
    assert True == True

def test_number():
    assert 1 == 1

def test_literal_error():
    assert 'z' in "Hello World"

def test_bool_error():
    assert True == False

def test_number_error():
    assert 2 == 1

def test_number_signature_error():
    assert 2 == 1

def test_number_exception():
    start = 0
    end = 1
    assert start > end