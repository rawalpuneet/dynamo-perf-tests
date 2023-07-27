from locust import HttpUser, task, between
import time,json, pandas

headers = {"x-api-key":"OT5PlILuzR83sgCJQ3zJD2SuFJPMMwRB5VoI8qOk"}

class putItem(HttpUser):
    wait_time = between(0.100, 0.300)
    @task
    def hello_world(self):
        payload = {"size":"10"}
        self.client.put("/load", headers=headers, data=json.dumps(payload) )
        #time.sleep(0.200)