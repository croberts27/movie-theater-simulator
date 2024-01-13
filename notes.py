# PYTHON DICTIONARIES
# Made up of values and keys
# Key is what you search in the dict to get the value
# Key = "abby" value = 23
students = {"Abby":23, "Bob":27, "McCall":26, "Calvin":26, "Runey":5}

del students["Bob"]
a = list(students.keys())
print(list(students.values())[2:])

students = {"Abby": {"id": "ID0001", "age": 23, "grade": "A"},
            "Bob": {"id": "ID0002", "age": 60, "grade": "B"},
            "McCall": {"id": "ID0003", "age": 26, "grade": "A+"},
            "Calvin": {"id": "ID0004", "age": 25, "grade": "A-"},
            "Runey": {"id": "ID0005", "age": 5, "grade": "F"},
            }

print(students["McCall"]["grade"], students["McCall"]["id"])

