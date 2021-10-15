import time
def calculate_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f'Total time {end_time-start_time}')
    return wrapper 
