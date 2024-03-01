contacts = {
    "number": 4,
    "students": 
        [
            {"name": "Sarah James", "email": "saraj@fake.com"},
            {"name": "Sherlock Holmes", "email": "sherlockh@fakecom"},
            {"name": "James Moriarty", "email": "jamesm@fakecom"},
            {"name": "John Watson", "email": "johnw@fakecom"},
        ]
}

# Experiment with for loops

for i in contacts:
    print(i)

print("")
for key, value in contacts.items():
    print(key, value)

print("")
for student in contacts["students"]:
    print(student)
    print(student["name"])
    print(student["email"])

