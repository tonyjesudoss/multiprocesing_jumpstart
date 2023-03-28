from multiprocessing import Process, Value, Lock, Semaphore
import time
import signal
import sys


def add(variable, semaphore, j):
    
    target = 10

    with semaphore:
        for i in range(target):
            variable.value += 1
            time.sleep(0.01)
            #print(f"value of the variable in the add function: {variable.value}")
            print(f"process {j} is under process in add...")  

def subtract(variable, semaphore, i):

    target = 10

    with semaphore:
        for i in range(target):
            variable.value -= 1
            #print(f"value of the variable in the subtract function: {variable.value}")
            print(f"process {i} is under process in subtract...")


if __name__ == "__main__":
    
    variable = Value('i',0)
    #process_lock = Lock()
    process_semaphore = Semaphore(3)

    add_processes = [Process(target= add, args=(variable,process_semaphore, i)) for i in range(10)]
    #sub_processes = [Process(target= subtract, args=(variable,process_semaphore, i)) for i in range(10)]
    
    total_processes = add_processes #+ sub_processes


    for process in total_processes:
        process.start()
    
    for process in total_processes:
        process.join()

    print(f"value of the variable: {variable.value}")




