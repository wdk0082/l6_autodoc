from autodoc.base_people import People

def test_people_init():
    p = People("John", 30)
    assert p.name == "John"
    assert p.age == 30

def test_change_name():
    p = People("John", 30)
    p.change_name("Jane")
    assert p.name == "Jane"

def test_update_age():
    p = People("John", 30)
    p.update_age()
    assert p.age == 31

def test_get_info():
    p = People("John", 30)
    info = p.get_info()
    assert info == ("John", 30)
