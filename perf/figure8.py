# 7 Manual scale up
from locust import LoadTestShape

class MyCustomShape(LoadTestShape):
    stages = [
        {"duration": 1200, "users": 15, "spawn_rate": 1},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None