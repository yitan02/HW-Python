import time
def calculate_time(func):
    def wrapper():
       """"
      Compute the time it takes for the function to run.

      This function takes the current time as the starting time. Then, the 
      function runs and end time is calculated by calling time.time() again.
      Prints the total time taken to run by subtracting end time with start 
      time.
    
      Parameter
      _________
      func : function
          A function that contains code that will be called on.
    
      Returns
      _______
      int
        The time taken where end time subtracts start time
    
      Example
      _______
      >>> calculate_time(func):
      # start_time = 00:00:01
      # end_time = 00:00:02
      2
      >>> calculator_time(func):
      # start_time = 00:00:10
      # end_time = 00:00:05
      5
      """

       start_time = time.time()
       func()
       end_time = time.time()
       print(f'Total time {end_time-start_time}')
    return wrapper 
