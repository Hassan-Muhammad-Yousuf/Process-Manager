from process import Process
from scheduler import Scheduler
from memory import MemoryManager
import simulation
import matplotlib.pyplot as plt
import pandas as pd
from config import MEMORY_BLOCKS

def get_user_input():
    num_processes = int(input("Enter the number of processes: "))
    
    arrival_times = []
    while len(arrival_times) != num_processes:
        try:
            arrival_times = list(map(int, input(f"Enter {num_processes} arrival times (comma-separated): ").split(',')))
        except ValueError:
            print(f"Please enter {num_processes} integers separated by commas.")

    burst_times = []
    while len(burst_times) != num_processes:
        try:
            burst_times = list(map(int, input(f"Enter {num_processes} burst times (comma-separated): ").split(',')))
        except ValueError:
            print(f"Please enter {num_processes} integers separated by commas.")

    memory_requirements = []
    while len(memory_requirements) != num_processes:
        try:
            memory_requirements = list(map(int, input(f"Enter {num_processes} memory requirements (comma-separated): ").split(',')))
        except ValueError:
            print(f"Please enter {num_processes} integers separated by commas.")

    print("\nChoose a scheduling algorithm:")
    print("1. First-Come, First-Served (FCFS)")
    print("2. Shortest Job First (SJF)")
    print("3. Round Robin (RR)")
    scheduling_choice = int(input("Enter your choice (1/2/3): "))

    print("\nChoose a memory management technique:")
    print("1. First-Fit")
    print("2. Best-Fit")
    memory_choice = int(input("Enter your choice (1/2): "))

    return num_processes, arrival_times, burst_times, memory_requirements, scheduling_choice, memory_choice

def print_table(processes):
    data = {
        "Process ID": [p.pid for p in processes],
        "Arrival Time": [p.arrival_time for p in processes],
        "Burst Time": [p.burst_time for p in processes],
        "Start Time": [p.start_time for p in processes],
        "Completion Time": [p.completion_time for p in processes],
        "Waiting Time": [p.start_time - p.arrival_time for p in processes],
        "Turnaround Time": [p.completion_time - p.arrival_time for p in processes]
    }
    df = pd.DataFrame(data)
    print(df)

def plot_gantt_chart(processes):
    fig, gnt = plt.subplots(figsize=(10, 5))
    gnt.set_title('Gantt Chart of Process Scheduling')
    gnt.set_xlabel('Time')
    gnt.set_ylabel('Process ID')

    yticks = [10 * (i + 1) for i in range(len(processes))]
    gnt.set_yticks(yticks)
    gnt.set_yticklabels([f"P{p.pid}" for p in processes])

    for i, process in enumerate(processes):
        gnt.broken_barh([(process.start_time, process.burst_time)], (yticks[i] - 5, 9), facecolors=('tab:blue'))
        gnt.text(process.start_time + process.burst_time / 2, yticks[i], f"P{process.pid}", ha='center', va='center', color='white')

    plt.show()

def plot_metrics(avg_waiting_time, avg_turnaround_time, cpu_utilization):
    metrics = {
        'Average Waiting Time': avg_waiting_time,
        'Average Turnaround Time': avg_turnaround_time,
        'CPU Utilization': cpu_utilization
    }
    
    df = pd.DataFrame(metrics, index=[0])
    df.plot(kind='bar', figsize=(10, 5))
    plt.title('Performance Metrics')
    plt.xticks(rotation=0)
    plt.show()

def main():
    print("Welcome to Process Scheduler and Memory Manager Simulation!\n")
    
    num_processes, arrival_times, burst_times, memory_requirements, scheduling_choice, memory_choice = get_user_input()

    # Validate lengths of input lists
    if len(arrival_times) != num_processes or len(burst_times) != num_processes or len(memory_requirements) != num_processes:
        print(f"Error: Number of processes ({num_processes}) does not match the length of input lists.")
        return

    processes = []
    for i in range(num_processes):
        process = Process(i + 1, arrival_times[i], burst_times[i], memory_requirements[i])
        processes.append(process)

    scheduler = Scheduler(processes)
    memory_manager = MemoryManager(MEMORY_BLOCKS.copy())

    if scheduling_choice == 1:
        scheduler.simulate("FCFS")
    elif scheduling_choice == 2:
        scheduler.simulate("SJF")
    elif scheduling_choice == 3:
        quantum = int(input("Enter the time quantum for Round Robin: "))
        scheduler.simulate("RR", quantum)

    if memory_choice == 1:
        for process in processes:
            if not memory_manager.first_fit(process.memory_req):
                print(f"Memory allocation failed for Process {process.pid} using First-Fit.")
    elif memory_choice == 2:
        for process in processes:
            if not memory_manager.best_fit(process.memory_req):
                print(f"Memory allocation failed for Process {process.pid} using Best-Fit.")

    print("\nRunning simulation...\n")
    avg_waiting_time, avg_turnaround_time, cpu_utilization = scheduler.calculate_metrics()

    print("\nSimulation Results:")
    print("-------------------")
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"CPU Utilization: {cpu_utilization:.2f}")
    # Print memory utilization if implemented

    print("\nProcess Information:")
    print_table(processes)
    plot_gantt_chart(processes)
    plot_metrics(avg_waiting_time, avg_turnaround_time, cpu_utilization)

if __name__ == "__main__":
    main()
