import numpy as np

def sumOfSales(branch):
    row = np.where(branch_numbers == branch)[0]
    return np.sum(data[row, 1:])

data = np.loadtxt("Term1/Post midterm/lab10/data/sales.tsv", delimiter='\t', dtype=float)
branch_numbers = data[:, 0]

# total_sales = []
# for branch in branch_numbers:
#     total_sales.append(sumOfSales(branch))
total_sales = [sumOfSales(branch) for branch in branch_numbers]

sorted_indices = np.argsort(total_sales)[::-1]
    
print("Branch   Total Sales")
for i in sorted_indices:
    print("%d        %d" % (branch_numbers[i], total_sales[i]))
