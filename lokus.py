from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(1)
    def index(self):
        with self.client.get("https://utecan.edu.mx/", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"No se pudo cargar la página de inicio: {response.status_code}")
    
    @task(2)
    def directorio(self):
        with self.client.get("https://utecan.edu.mx/directorio", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"No se pudo cargar la página de directorio: {response.status_code}")
    
    @task(3)
    def transparencia(self):
        with self.client.get("https://utecan.edu.mx/transparencia", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"No se pudo cargar la página de transparencia: {response.status_code}")
        
    @task(4)
    def financiera(self):
        with self.client.get("https://utecan.edu.mx/financiera", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"No se pudo cargar la página financiera: {response.status_code}") 
        
    @task(5)
    def universidad(self):
        with self.client.get("https://utecan.edu.mx/universidad", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"No se pudo cargar la página de universidad: {response.status_code}")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 2)
