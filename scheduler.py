from collections import deque

class Scheduler:
    def __init__(self, processes):
        self.processes = processes

    def fcfs_schedule(self):
        """ First-Come, First-Served (FCFS) scheduling """
        current_time = 0
        for process in self.processes:
            process.start_time = max(current_time, process.arrival_time)
            process.completion_time = process.start_time + process.burst_time
            current_time = process.completion_time

    def sjf_schedule(self):
        """ Shortest Job First (SJF) scheduling """
        self.processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
        current_time = 0
        for process in self.processes:
            process.start_time = max(current_time, process.arrival_time)
            process.completion_time = process.start_time + process.burst_time
            current_time = process.completion_time

    def rr_schedule(self, quantum):
        """ Round Robin (RR) scheduling """
        ready_queue = deque(self.processes)
        current_time = 0
        while ready_queue:
            process = ready_queue.popleft()
            process.start_time = max(current_time, process.arrival_time)
            if process.remaining_time > quantum:
                current_time += quantum
                process.remaining_time -= quantum
                ready_queue.append(process)
            else:
                current_time += process.remaining_time
                process.completion_time = current_time

    def simulate(self, scheduling_algorithm, quantum=5):
        """ Simulate the scheduling algorithm """
        if scheduling_algorithm == "FCFS":
            self.fcfs_schedule()
        elif scheduling_algorithm == "SJF":
            self.sjf_schedule()
        elif scheduling_algorithm == "RR":
            self.rr_schedule(quantum)

    def calculate_metrics(self):
        """ Calculate performance metrics """
        total_waiting_time = 0
        total_turnaround_time = 0
        total_burst_time = 0
        total_completion_time = max(p.completion_time for p in self.processes)
        for process in self.processes:
            waiting_time = process.start_time - process.arrival_time
            turnaround_time = process.completion_time - process.arrival_time
            total_waiting_time += waiting_time
            total_turnaround_time += turnaround_time
            total_burst_time += process.burst_time

        avg_waiting_time = total_waiting_time / len(self.processes)
        avg_turnaround_time = total_turnaround_time / len(self.processes)
        cpu_utilization = (total_burst_time / total_completion_time) * 100

        return avg_waiting_time, avg_turnaround_time, cpu_utilization
