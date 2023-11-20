import numpy as np

# def calculateGPA(id):
#     row = np.where(ids == id)[0][0]
#     numerator = 0
#     credits = [3, 2, 1, 3, 3, 3]
#     for i, credit in enumerate(credits):
#         numerator += data[row, i+1] * credit
        
#     return numerator / sum(credits)

def calculateGPA(id):
    row = np.where(ids == id)[0][0]
    credits = np.array([3, 2, 1, 3, 3, 3])
    grades = data[row, 1:]
    return np.average(grades, weights=credits)

data = np.loadtxt("Term1/Post midterm/lab10/data/grades.tsv", delimiter='\t', dtype=float)
ids = data[:, 0]

print("Student ID   GPA")
for id in ids:
    print("%d   %.2f" % (id, calculateGPA(id)))
