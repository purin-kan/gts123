def calculate_average(scores):
    return sum(scores) / len(scores)

students = {}

while True:
    user_input = input("Input: ").split()
    
    if user_input[0] == 'done' and user_input[1] == '0':
        break
    
    if len(user_input[0]) != 4 or not user_input[0].isdigit():
        print("Invalid ID!")
        continue
    student_id = int(user_input[0])
    
    
    try:
        score = int(user_input[1])
    except ValueError:
        print("Invalid score!")
        continue
    
    if not 0 < score < 100:
        print("Invalid score!")
        continue
    
    
    if student_id not in students:
        students[student_id] = score
    else:
        print("The ID is already recorded!")
    

students = dict(sorted(students.items()))


print("List:")

if not students:
    print("> no score is recorded!")
    exit()

for student_id, score in sorted(students.items()):
    print(f"{student_id} {score}")
print(f"there are {len(students)} student(s). The average score is {calculate_average(students.values()):.2f} points.")
