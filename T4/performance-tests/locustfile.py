from locust import HttpUser, task

class MyUser(HttpUser):
    @task
    def get_posts(self):
        self.client.get("/comments")
