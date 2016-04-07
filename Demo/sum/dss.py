from functions import *
import multiprocessing
import time
import sys
# for compatibility with Python 2.7 and 3
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

# Checking whether by mistake the user is running dss directly
if __name__ == "__main__":
    print("dss.py should not be called directly")
    print("Read the README file for further details")
    exit(1)

config = ConfigParser()
config.read("config.ini")
max_instances = int(config.get("default", "max_number_of_instances"))

class machine():
    'Class for the instance of a machine'
    
    q = [multiprocessing.Queue() for i in range(max_instances + 1)]
    # q[0] is unused
    count = multiprocessing.Value('i', 1)

    def __init__(self):
        self.mac_id = machine.count.value
        machine.count.value += 1

    def execute_func(self, func_name, *user_args):
        list_of_args = [self]
        for arg in user_args:
            list_of_args.append(arg)
        arguments = tuple(list_of_args)

        try:
            if(func_name in globals()):
                multiprocessing.Process(target = globals().get(func_name), args = arguments).start()
            else:
                raise NameError("name '" + func_name + "'is not defined")
        except:
            e = sys.exc_info()
            print("Exception in execute_func() of", self.get_machine_id(), ":", e[0], e[1]) 

    def send(self, destination_id, message):
        # send message to the machine with machine_id destination_id

        try:
            mac_id = int(destination_id[8:])
        except:
            e = sys.exc_info()
            print("Exception in send() of", self.get_machine_id(), ":", e[0], e[1])
            return -1
        if(mac_id >= machine.count.value or mac_id <= 0):
            return -1

        # message is of the format "hello|2". Meaning message is "hello" from machine with id 2
        # However, the message received is processed and then returned back to the user
        message += '|' + str(self.get_id())

        machine.q[mac_id].put(message)
        return 1

    def recv(self):
        mac_id = self.get_id()
        if(mac_id >= machine.count.value or mac_id <= 0):
            return -1, -1

        message =  machine.q[mac_id].get().split('|')

        # message received is returned with the format "hello" message from "machine_2"
        return message[0], 'machine_' + message[1]

    def get_id(self):
        return self.mac_id

    def get_machine_id(self):
        return "machine_" + str(self.get_id()) 
