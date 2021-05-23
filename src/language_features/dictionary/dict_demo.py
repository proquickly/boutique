
my_customers = [
    ('01',
     'XYZ abc',
     42.09,
     ),
    ('02',
     'TR deep',
     90.01
     )
]


my_other_customers = [
    {'ID': '01',
     'Name': 'XYZ abc',
     'Credit': 42.09
     },
    {'ID': '02',
     'Name': 'TR deep',
     'Credit': 90.01
     }
]

mydict = {'ID': '01',
     'Name': 'XYZ abc',
     'Credit': 42.09
}

assert mydict['Credit'] == 42.09



for customer in my_other_customers:
    print(customer['Name'])

for customer in my_other_customers:
    print(customer.get('Name'))

for customer in my_other_customers:
    customer['Credit'] *= 1.5

for customer in my_other_customers:
    print(customer.values())

for customer in my_other_customers:
    for key, value in customer.items():
        print(key, value)


my_dict = {"Name": "Andy", "Job": "Tutor"}

dict_to_list = []

for key, value in my_dict.items():
    dict_to_list.append((key, value))

assert dict_to_list == [("Name", "Andy"), ("Job", "Tutor")]


people = [
    {"Name": "Andy", "Job": "Tutor"},
    {"Name": "Fred", "Job": "Analyst"},
    {"Name": "Pam", "Job": "Nurse"},
]

assert people[1]["Name"] == "Fred"


# dictionary keys must be unique; show what happens when they are not
my_dict = {
    "Name": "Andy",
    "Job": "Tutor",
    "Job": "Analyst",
    "Preferred_name": "Andy",
}

assert my_dict == {"Name": "Andy", "Job": "Analyst", "Preferred_name": "Andy"}

# transpose keys and values
my_new_dict = {}
for key, value in my_dict.items():
    my_new_dict[value] = key

assert my_new_dict == {"Analyst": "Job", "Andy": "Preferred_name"}

people = [
    {"Name": "Andy", "Job": "Tutor"},
    {"Name": "Fred", "Job": "Analyst"},
    {"Name": "Pam", "Job": "Nurse"},
]

better_people = {
    1: {"Name": "Andy", "Job": "Tutor"},
    2: {"Name": "Fred", "Job": "Analyst"},
    3: {"Name": "Pam", "Job": "Nurse"},
}

better_people2 = {
    'Andy': {"Name": "Andy", "Job": "Tutor"},
    'Fred': {"Name": "Fred", "Job": "Analyst"},
    3: {"Name": "Pam", "Job": "Nurse"},
}

assert better_people[2] == {"Name": "Fred", "Job": "Analyst"}
assert better_people[2]["Name"] == "Fred"
