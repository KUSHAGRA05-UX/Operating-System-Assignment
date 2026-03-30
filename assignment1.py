
# CPU Scheduling Lab Program
# Tasks: Process Creation, FCFS, SJF, Priority, Round Robin


class Process:
    def __init__(self, pid, at, bt, pr=0):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.pr = pr


# ===============================
# TASK 1: PROCESS CREATION
# ===============================

print("\n" + "="*50)
print("TASK 1: PROCESS CREATION")
print("="*50)

processes = []

n = int(input("Enter number of processes: "))

for i in range(n):

    print(f"\nProcess {i+1}")

    pid = int(input("Enter Process ID: "))
    at = int(input("Enter Arrival Time: "))
    bt = int(input("Enter Burst Time: "))
    pr = int(input("Enter Priority: "))

    processes.append(Process(pid, at, bt, pr))


print("\nPROCESS TABLE")
print("PID\tAT\tBT\tPR")

for p in processes:
    print(p.pid, "\t", p.at, "\t", p.bt, "\t", p.pr)



# ===============================
# TASK 2: FCFS SCHEDULING
# ===============================

print("\n" + "="*50)
print("TASK 2: FCFS SCHEDULING")
print("="*50)

fcfs = sorted(processes, key=lambda x: x.at)

time = 0

print("PID\tAT\tBT\tCT\tTAT\tWT")

for p in fcfs:

    if time < p.at:
        time = p.at

    ct = time + p.bt
    tat = ct - p.at
    wt = tat - p.bt

    print(p.pid, "\t", p.at, "\t", p.bt, "\t", ct, "\t", tat, "\t", wt)

    time = ct



# ===============================
# TASK 3: SJF SCHEDULING
# ===============================

print("\n" + "="*50)
print("TASK 3: SJF SCHEDULING")
print("="*50)

time = 0
completed = []
remaining = processes.copy()

print("PID\tAT\tBT\tCT\tTAT\tWT")

while remaining:

    available = [p for p in remaining if p.at <= time]

    if not available:
        time += 1
        continue

    p = min(available, key=lambda x: x.bt)

    ct = time + p.bt
    tat = ct - p.at
    wt = tat - p.bt

    print(p.pid, "\t", p.at, "\t", p.bt, "\t", ct, "\t", tat, "\t", wt)

    time = ct
    remaining.remove(p)


