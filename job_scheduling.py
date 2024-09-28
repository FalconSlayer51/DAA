from typing import List


class Job:
    def __init__(self,id:str,dead_line:int ,profit:int) -> None:
        self.id = id
        self.deadline = dead_line
        self.profit = profit
        
def job_scheduling(jobs: List[Job]):
    jobs.sort(key=lambda x: x.profit,reverse=True)
    
    deadline = max(job.deadline for job in jobs)
    
    schedule = [None] * deadline
    total_profit = 0
    
    for job in jobs:
        for slot in range(job.deadline-1,-1,-1):
            if schedule[slot] is None:
                schedule[slot] = job.id
                total_profit += job.profit
                break
                
    return schedule,total_profit
    
if __name__ == "__main__":
    jobs = [
        Job('Job1', 2, 100),
        Job('Job2', 1, 19),
        Job('Job3', 2, 27),
        Job('Job4', 1, 25),
        Job('Job5', 3, 15),
    ]
        
    scheduled_jobs, total_profit = job_scheduling(jobs)
        
    print("Scheduled Jobs:", scheduled_jobs)
    print("Total Profit:", total_profit)