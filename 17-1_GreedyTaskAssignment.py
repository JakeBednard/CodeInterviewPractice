def make_assignments(tasks):
    tasks.sort()
    assignments = []
    for i in range(0, int(len(tasks)/2)):
        assignments.append((tasks[i], tasks[len(tasks)-i-1]))

    if len(tasks) % 2 == 1:
        assignments[-1] = assignments[-1] + (tasks[int(len(tasks)/2+1)],)

    return assignments

print(make_assignments([5,2,1,6,4,4,3]))