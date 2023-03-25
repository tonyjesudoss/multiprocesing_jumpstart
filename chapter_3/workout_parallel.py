from multiprocessing import Process
import time
import signal
import sys

def add(num):
    number = 1
    
    for i in range(num):
        number = number + 1


def signal_terminate(sig_num, frame):
    print("terminate signal called.")
    print("calling sys exit")
    sys.exit(0)

if __name__ == "__main__":
    number = 1000000000
    
    signal.signal(signal.SIGTERM, signal_terminate)

    add_process = [Process(target= add, args=(number,)) for _ in range(5)]
    
    for process in add_process:
        process.start()
    
    time.sleep(2)

    for process in add_process:
        process.terminate()


    for process in add_process:
        if process.is_alive():
            print(f"process {process} is still alive")


