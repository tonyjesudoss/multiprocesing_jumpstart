from multiprocessing import Process, Value, Lock, Semaphore, Condition, Barrier
import time
import signal
import sys


def add(variable, condition, barrier, j):
    
    target = 10


    #print(f"line position {line_position}")

    #time.sleep(1)

    print(f"before the barrier in process {j}")
    barrier.wait()
    print("after the barrier wait")
    
    with condition:

        condition.wait()
    
    time.sleep(0.01)
    print(f"condition signal received in process {j}")
    #return



if __name__ == "__main__":    
    variable = Value('i',0)
    primitive = Condition()
    process_barrier = Barrier(10)

    add_processes = [Process(target= add, args=(variable, primitive, process_barrier, i)) for i in range(10)]

    
    total_processes = add_processes 


    

    for process in total_processes:
        process.start()
    
    #time.sleep(1)
    #process_barrier.wait()
    #print("passed the barrier in the main process")
    #print(f"position in the main process: {position}")
    #for i in range(10):
    time.sleep(1)

    with primitive:
        print("notifying all the processes with condition")
        primitive.notify_all()
        #time.sleep(1)
    
    
    for process in total_processes:
        process.join()

    print(f"value of the variable: {variable.value}")




