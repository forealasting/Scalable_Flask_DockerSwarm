from locust import HttpUser, task, constant_pacing
import random
import subprocess
from locust.stats import stats_printer, stats_history
from locust.env import Environment
from locust.log import setup_logging


ip = "192.168.99.104"  # app_web

url = "http://" + ip + ":1111/ping"

class OneM2MUser(HttpUser):

    wait_time = constant_pacing(1 / 10)  # 每秒生成10個請求
    @task
    def on_start(self):

        # 執行POST請求
        response = self.client.post(url)

        if response.status_code == 200:
            print("POST successful")
        else:
            print("POST failed")

        @task
        def index(self):
            self.client.get("/")
            self.client.get("/static/assets.js")

        @task
        def about(self):
            self.client.get("/about/")