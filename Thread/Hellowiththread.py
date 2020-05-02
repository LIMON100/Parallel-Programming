from threading import Thread
from time import sleep

class bokk(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.messege = "Python Parallel programming started.\n"
        
    
    def print_messege(self):
        print(self.messege)
        
        
    def run(self):
        print("Thread Starting")
        
        x = 0
        while(x < 10):
            self.print_messege()
            sleep(2)
            x = x + 1
        
        print("Thread Ended..\n")
        
print("Process Start..\n")

b = bokk()

b.start()

print("Process Ended..\n")