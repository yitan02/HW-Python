import time
def calculate_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        time_taken = end_time-start_time
        print("Hello.")
    return wrapper 
