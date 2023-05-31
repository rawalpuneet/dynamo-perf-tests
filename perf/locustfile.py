from locust import HttpUser, task
import time,json, pandas

headers = {"x-api-key":"bOn4rsRLP68DFAkeuJYq6asVVsxw9bEd1XnKvjNQ"}
csv_payload = pandas.read_csv('data/file300.csv')

class putItem(HttpUser):
    @task
    def hello_world(self):
        payload = {}
        payload['TTL'] = str(time.time() + 60 * 10)
        payload['json'] = csv_payload.to_csv(index=False).replace("\n","")
        self.client.post("/v1/load", headers=headers, data=json.dumps(payload) )