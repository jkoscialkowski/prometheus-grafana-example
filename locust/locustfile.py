from locust import HttpUser, task

class LoadTestUser(HttpUser):
    @task
    def send_request(self):
        self.client.get("/")
