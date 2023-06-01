# 6.1 4K plateaus
from locust import LoadTestShape

class MyCustomShape(LoadTestShape):
    stages = [
        {"duration": 60, "users": 1, "spawn_rate": 1},
        {"duration": 660, "users": 5, "spawn_rate": 1},
        {"duration": 720, "users": 1, "spawn_rate": 1},        
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None