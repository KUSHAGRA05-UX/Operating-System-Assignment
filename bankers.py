def is_safe(processes, available, max_demand, allocation):
    n = len(processes)
    m = len(available)

    # Calculate Need matrix
    need = [[max_demand[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]

    finish = [False] * n
    safe_sequence = []
    work = available.copy()

    while len(safe_sequence) < n:
        allocated = False
        for i in range(n):
            if not finish[i]:
                # Check if need <= work
                if all(need[i][j] <= work[j] for j in range(m)):
                    # Allocate resources
                    for j in range(m):
                        work[j] += allocation[i][j]

                    safe_sequence.append(processes[i])
                    finish[i] = True
                    allocated = True

        if not allocated:
            return False, []

    return True, safe_sequence


# Example Input
processes = ["P0", "P1", "P2", "P3", "P4"]

available = [3, 3, 2]

max_demand = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]

allocation = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

# Run Algorithm
safe, sequence = is_safe(processes, available, max_demand, allocation)

if safe:
    print("System is in SAFE state")
    print("Safe sequence:", " -> ".join(sequence))
else:
    print("System is NOT in safe state")