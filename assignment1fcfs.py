def fcfs(processes, burst_time):
    n = len(processes)
    
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    # Waiting time for first process is 0
    waiting_time[0] = 0
    
    # Calculate waiting time
    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + burst_time[i-1]
    
    # Calculate turnaround time
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_time[i]
    
    # Display results
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i]}\t\t{burst_time[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    
    print("\nAverage Waiting Time =", sum(waiting_time)/n)
    print("Average Turnaround Time =", sum(turnaround_time)/n)


# Example
processes = [1, 2, 3, 4]
burst_time = [5, 3, 8, 6]

fcfs(processes, burst_time)
