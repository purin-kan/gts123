names = []
programs = []
gpas = []

while True:
    user_input = input("Input: ").split()
    
    if user_input[0] == "done":
        break
        
    if user_input[1] not in ['ce', 'che', 'ec', 'ie', 'me']:
        print("ERROR")
        continue
    
    if not 0 <= float(user_input[2]) <= 4:
        print("ERROR")
        continue
    
    names.append(user_input[0])
    programs.append(user_input[1])
    gpas.append(float(user_input[2]))
        
print("---SUMMARY----")
print("ce = %d" % programs.count("ce"))
print("che = %d" % programs.count("che"))
print("ec = %d" % programs.count("ec"))
print("ie = %d" % programs.count("ie"))
print("me = %d" % programs.count("me"))


students = list(zip(names, programs, gpas))

students_sorted_by_gpa = sorted(students, key=lambda student: student[2], reverse=True)
print(students_sorted_by_gpa)

print("---LIST----")
if not students_sorted_by_gpa:
    print("The list is empty")
else:
    for student in students_sorted_by_gpa:
        print("%s %s %.2f" % student)
