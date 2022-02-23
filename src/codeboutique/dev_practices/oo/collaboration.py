class Person:
    def __init__(self, full_name):
        self.full_name = full_name
        self.first_parent = None
        self.second_parent = None

    def record_parents(self, first_parent, second_parent):
        self.first_parent = first_parent
        self.second_parent = second_parent


fred = Person("Fred Bloggs")
assert isinstance(fred, Person)

fred.record_parents(Person("Fred Bloggs Senior"), Person("Freda Bloggs"))

assert fred.first_parent.full_name == "Fred Bloggs Senior"
assert fred.second_parent.full_name == "Freda Bloggs"
