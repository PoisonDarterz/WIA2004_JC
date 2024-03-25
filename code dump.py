
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
            
            