def add_student(name, score):
    if name not in students:
        students[name] = score
    else:
        print("Duplicate name!")


students = {}

while True:
    
    user_input = input("Enter student name and score: ").split()

    if user_input[0] == "end":
        if not(students):
            print("List:\n> empty list!")
            break
        
        print("List:")
        
        students = dict(sorted(students.items(), key=lambda x:x[1], reverse=True))
        
        for name, score in students.items():
            print(f"{name}    {score}")
        break
        

    if not 0 <= int(user_input[1]) <= 100:
        print("Invalid score!")
        continue

    add_student(user_input[0], user_input[1])
