people = {1: 'fred', 0: 'harry', 9: 'andy'}
print(sorted(people.keys()))
print(sorted(people.values()))
print(sorted(people.items()))
print(dict(sorted(people.items())))  # really???

person = people.get(1, None)
assert person == 'fred'

person = people.get(8, None)
assert person is None
