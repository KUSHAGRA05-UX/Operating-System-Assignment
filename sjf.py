def sjf(processes, burst_time):
    n = len(processes)
    
    # Combine and sort by burst time
    data = list(zip(processes, burst_time))
    data.sort(key=lambda x: x[1])
    
    processes_sorted = [x[0] for x in data]
    burst_sorted = [x[1] for x in data]
    
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    # Calculate waiting time
    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + burst_sorted[i-1]
    
    # Calculate turnaround time
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_sorted[i]
    
    # Display results
    print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes_sorted[i]}\t\t{burst_sorted[i]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    
    print("\nAverage Waiting Time =", sum(waiting_time)/n)
    print("Average Turnaround Time =", sum(turnaround_time)/n)


# Example
processes = [1, 2, 3, 4]
burst_time = [5, 3, 8, 6]

sjf(processes, burst_time)