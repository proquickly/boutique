from cerberus import Validator
v = Validator({'name': {'type': 'string'}})
assert v.validate({'name': 'andy miles'})
