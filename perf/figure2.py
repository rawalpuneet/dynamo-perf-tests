# Burst 
from locust import LoadTestShape
import random
class MyCustomShape(LoadTestShape):
    stages = [        
        {"duration": 60, "users": 20, "spawn_rate": 1, "type":"constant"},
        {"duration": 10*60, "users": [5,11], "spawn_rate": 1, "type":"range"},
        {"duration": 11*60, "users": 20, "spawn_rate": 1, "type":"constant"},
        {"duration": 20*60, "users": [5,11], "spawn_rate": 1, "type":"range"},
        {"duration": 21*60, "users": 20, "spawn_rate": 1, "type":"constant"},
        {"duration": 50*60, "users": [5,11], "spawn_rate": 1, "type":"range"},
        {"duration": 51*60, "users": 20, "spawn_rate": 1, "type":"constant"},
        
    
    ]
    counter = -1
    users = 0
    
    def tick(self):
        run_time = self.get_run_time()        
        
        
        for stage in self.stages:
            if run_time < stage["duration"] and stage['type'] == "range":
                divider = round(run_time / 60)               
                if divider != self.counter:
                    self.counter = divider
                    self.users = random.randrange(stage['users'][0], stage['users'][1])
                    print("Starting users type: "+ stage['type']+" for "+str(self.users) + " users.")

                tick_data = (self.users, stage["spawn_rate"])
                return tick_data
            elif run_time < stage["duration"] and stage['type'] == "constant":
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None