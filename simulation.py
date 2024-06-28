# simulation.py

from scheduler import Scheduler
from process import Process  # Assuming Process class is defined in process.py

def main():
    # Create some example processes (replace with your actual process creation logic)
    processes = [
        Process(1, 0, 10, 100),  # Process ID, arrival time, burst time, memory requirement
        Process(2, 2, 5, 50),
        Process(3, 4, 8, 70),
        # Add more processes as needed
    ]

    # Instantiate Scheduler
    scheduler = Scheduler(processes)

    # Simulate FCFS scheduling
    scheduler.simulate("FCFS")

    # Calculate metrics
    avg_waiting_time, avg_turnaround_time, cpu_utilization = scheduler.calculate_metrics()

    # Print metrics
    print(f"Average Waiting Time: {avg_waiting_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")
    print(f"CPU Utilization: {cpu_utilization}")

if __name__ == "__main__":
    main()

