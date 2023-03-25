
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
    add_start = time.time()
    number = 1000000000
    add(number)
    add_end = time.time()
    sub_start = time.time()
    subtract(number)
    sub_end = time.time()

    #print(f"time taken for add operation : {add_end - add_start} s")
    #print(f"time taken for subtract operation : {sub_end - sub_start} s")
    print(f"Iteration count {number}")
    print(f"time taken for the operation : {sub_end - add_start}")
