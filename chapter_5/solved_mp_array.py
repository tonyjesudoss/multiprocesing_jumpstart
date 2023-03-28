import multiprocessing
from multiprocessing import Queue
from multiprocessing import Pipe
from multiprocessing import Array
from random import random
import time
from time import sleep
import queue

def worker(id, mp_arr):

    value = id + 10
    print(f"inserting: {value} at the index {id}")
    mp_arr[id] = value
    print(f"array after insertion: {mp_arr[:]}")


if __name__ == "__main__":
    #process_queue = Queue()
    #receiver, sender = Pipe()
    mp_array = Array('i', 5)
    
    worker_processes = [multiprocessing.Process(target=worker, args=(i, mp_array)) for i in range(5)]

    for process in worker_processes:
        process.start()


    
    for process in worker_processes:
        process.join()
    
    
    print("values of the finished array:", mp_array[:])

    
    
