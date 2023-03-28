import multiprocessing
from multiprocessing import Queue
from multiprocessing import Pipe
from multiprocessing import Array
from random import random
import time
from time import sleep
import queue

def worker(id, sender):
    
    value = id
    print(f"sleeping in the process {id}")
    sleep(value)

    print(f"adding value: {value} to the pipe")
    sender.send(value)

    if id == 4:
        value = None
        print(f"adding value: {value} to the pipe")
        sender.send(value)


def listener(receiver):

    sum = 0 
    while True:
        try:
            #number = process_queue.get()
            number = receiver.recv()

            if number == None:
                print("none received so breaking the listener")
                break
            
            sum += number

            print(f"number received at the listener: {number}")
            
        except queue.Empty:
            print("encountered empty queue , going to sleep now")
            time.sleep(0.01)
    return sum

if __name__ == "__main__":
    #process_queue = Queue()
    receiver, sender = Pipe()
    worker_processes = [multiprocessing.Process(target=worker, args=(i, sender)) for i in range(5)]

    for process in worker_processes:
        process.start()

    added_number = listener(receiver)

    print("added number received:", added_number)

    for process in worker_processes:
        process.join()
    
    print("Done with all the procedures. Exiting the program")

    
    
