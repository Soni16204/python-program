#Given the dictionary student = {'name': 'John', 'age': 22, 'course': 'Computer Science'}, print all the keys and values.
student = {'name': 'John', 'age': 22, 'course': 'Computer Science'}
for key,values in student.items():
    print(f"{key}: {values}")