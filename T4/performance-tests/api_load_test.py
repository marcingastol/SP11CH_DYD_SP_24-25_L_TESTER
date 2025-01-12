import time
import requests

url = "https://jsonplaceholder.typicode.com/posts"

def send_request():
    """
    ta funkcja wysyla pojedyncze zapytanie do naszego API
    i bedzie zwracala kod statusu (200,400,500 itp)
    """

    response = requests.get(url)
    return response.status_code

print("Rozpoczynamy prosty test, bedziemy wysylac 10 zapytan do API")

start_time = time.time()

# w petli wysylamy 10 zapytan
for i in range(10):
    status = send_request()
    print(f"Zapytanie numer {i + 1}: status: {status}")

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Suma czasu dla 10 zapytan: {elapsed_time} sekund")