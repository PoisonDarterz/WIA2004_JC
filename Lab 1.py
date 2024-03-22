#Program to simulate non-preemptive CPU sceduling algorithms
#TurnAround Time and Waiting Time

class CPU_Scheduler:
    def __init__(self, process_ids, burst_time):
        self.process_ids = process_ids
        self.burst_time = burst_time
        self.n = len(burst_time)
        self.waiting_time = [0] * self.n
        self.turnaround_time = [0] * self.n


    def fcfs(self):
        self.waiting_time[0] = 0
        self.turnaround_time[0] = self.burst_time[0]

        for i in range(1, self.n):
            self.waiting_time[i] = self.waiting_time[i-1] + self.burst_time[i-1]
            self.turnaround_time[i] = self.waiting_time[i] + self.burst_time[i] 


    def sjf(self):
        sorted_burst_times = sorted((burst_time, index) for index, burst_time in enumerate(self.burst_time))
        
        # Calculating waiting time and turnaround time for SJF
        for i in range(self.n):
            index = sorted_burst_times[i][1]
            if i == 0:
                self.waiting_time[index] = 0
                self.turnaround_time[index] = self.burst_time[index]
            else:
                prev_index = sorted_burst_times[i - 1][1]
                self.waiting_time[index] = self.turnaround_time[prev_index]
                self.turnaround_time[index] = self.waiting_time[index] + self.burst_time[index]

    def print_result(self):
        avg_waiting_time = sum(self.waiting_time) / self.n
        avg_turnaround_time = sum(self.turnaround_time) / self.n

        print("Process ID\t Burst Time\t Waiting Time\t Turnaround Time")
        for i in range(self.n):
            print(f"{self.process_ids[i]}\t\t{self.burst_time[i]}\t\t{self.waiting_time[i]}\t\t{self.turnaround_time[i]}")

        print("\nAverage Waiting Time:", avg_waiting_time)
        print("Average Turnaround Time:", avg_turnaround_time)


def main ():
    process_ids = [1, 2, 3] 
    burst_time = [10, 5, 8]

    fcfs = CPU_Scheduler(process_ids, burst_time)
    fcfs.fcfs()

    sjf = CPU_Scheduler(process_ids, burst_time)
    sjf.sjf()

    fcfs.print_result()
    sjf.print_result()

if __name__ == "__main__":
    main()
