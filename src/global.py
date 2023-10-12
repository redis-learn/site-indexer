import time

curr_time = 0

def reset():
    curr_time = int(time.time() * 1000000)

def get():
    return curr_time


