class Process:
    def __init__(self, pid, arrival_time, burst_time, memory_req):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.memory_req = memory_req
        self.remaining_time = burst_time  # For SJF/SRTF scheduling
        self.start_time = 0  # Start time of execution
        self.completion_time = 0  # Completion time after execution

    def __str__(self):
        return f"Process {self.pid} (Arrival: {self.arrival_time}, Burst: {self.burst_time}, Memory: {self.memory_req})"


