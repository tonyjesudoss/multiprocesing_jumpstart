from multiprocessing import Process
import time

def add(num):
    number = 1
    
    for i in range(num):
        number = number + 1

    #print("number in the add function :", number)

def subtract(num):
    number = 1
    
    for i in range(num):
        number = number - 1

    #print("number in the subtract function :", number)



if __name__ == "__main__":
    number = 1000000000
    
    start = time.time()
    
    add_process = Process(target= add, args=(number,))
    sub_process = Process(target= subtract, args=(number,))
    
    add_process.start()
    sub_process.start()

    add_process.join()
    sub_process.join()    
    
    end = time.time()

    print(f"Iteration count: {number}")
    print(f"time taken for the operation: {end - start} s")
