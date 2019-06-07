import solution

nValues = [40, 250, 260, 230, 60]
solutions = [[0, 0, 2], [2, 1, 0], [2, 0, 3], [1, 1, 4], [0, 0, 3]]
for i in range(len(nValues)):
    print(solution.withdraw(nValues[i]) == solutions[i])