# Burst 
from locust import LoadTestShape
import random
class MyCustomShape(LoadTestShape):
    stages = [
        {"duration": 60, "users": [1,2], "spawn_rate": 1},
    
    ]
    counter = -1
    users = 0
    
    def tick(self):
        run_time = self.get_run_time()
        divider = round(run_time / 60)
        if divider != self.counter:
            self.counter = divider
            self.users = random.randrange(self.stages[0]['users'][0], self.stages[0]['users'][1])
            print(self.users)
        
        
        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (self.users, stage["spawn_rate"])
                return tick_data

        return None