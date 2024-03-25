#Program to simulate non-preemptive CPU sceduling algorithms
#TurnAround Time and Waiting Time

class CPU_Scheduler:
    # Constructor to initialize the process_ids and burst_time
    def __init__(self, process_ids, burst_time):
        self.process_ids = process_ids
        self.burst_time = burst_time
        self.n = len(burst_time)
        self.waiting_time = [0] * self.n
        self.turnaround_time = [0] * self.n

    # Function to calculate waiting time and turnaround time for FCFS
    def fcfs(self):
        self.waiting_time[0] = 0
        self.turnaround_time[0] = self.burst_time[0]
        # Calculate waiting time and turnaround time for subsequent processes
        for i in range(1, self.n):
            self.waiting_time[i] = self.waiting_time[i-1] + self.burst_time[i-1]
            self.turnaround_time[i] = self.waiting_time[i] + self.burst_time[i] 

    # Function to print the result
    def print_result(self):
        avg_waiting_time = sum(self.waiting_time) / self.n
        avg_turnaround_time = sum(self.turnaround_time) / self.n

        print("Process ID\t Burst Time\t Waiting Time\t Turnaround Time")
        for i in range(self.n):
            print(f"{self.process_ids[i]}\t\t{self.burst_time[i]}\t\t{self.waiting_time[i]}\t\t{self.turnaround_time[i]}")

        print("\nAverage Waiting Time:", avg_waiting_time)
        print("Average Turnaround Time:", avg_turnaround_time)

# Main function
def main ():
    # initialize process_ids and burst_time
    process_ids = [1, 2, 3, 4, 5] 
    burst_time = [10, 5, 8, 2, 5]
    # Create an object of CPU_Scheduler class
    fcfs = CPU_Scheduler(process_ids, burst_time)
    fcfs.fcfs()
    # Print the results.
    fcfs.print_result()

if __name__ == "__main__":
    main()
