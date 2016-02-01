# DSS_py

DSS_py is a Distributed System Simulator. The python class file allows one to simulate distributed systems in one's own system. One can create a number of machines, assign them tasks in the form of functions and make them communicate between each other through messages.

## Get Started

1. Download the files and copy `class_file.py` and `config.txt` to the folder where you want to work.
2. Set the maximum number of machine instances you want to work with in `config.txt`.
3. Create a file name `functions.py` and keep the functions that you want to assign as tasks to the machines.
4. Create another file and start coding. Do include the line `from class_file import *` in your main code.

## Documentation

### Creating a New Instance

`machine_1 = machine()`

### Assigning a Task in the Form of a Function

`machine_1.execute_func("func_name", 1, 2)`

Where `func_name` is the name of the function, followed by the arguments that the function accepts.
Every function that is to be assigned as a task to the machine instance has to have their first parameter as the identity variable. One can name it whatever he/she wants. This identity variable has to be used while calling other functions such as `send()`, `recv()` and `get_machine_id()`. The function can have its regular variables (as sent through `execute_func()`) just after the identity variable.

### Sending a Message to another Machine Instance

`identity_variable.send("machine_1", "hello")`

Where `"machine_1"` is the machine ID of the destination machine and `"hello"` is the message.

`send()` returns 1 on success.

`send()` returns -1 when unsuccessful. This error will occur when you pass machine id that is not present.

### Receiving a Message from other Machine Instance

`identity_variable.recv()`

`recv()` is blocking, and will return only when some machine has sent a message that is buffered or some machine sends at that time.

`recv()` returns `message, sender_machine_id` on success.

`recv()` returns `-1, -1` when unsuccessful.

### Get the current machine ID

`identity_variable.get_machine_id()`

Returns the machine id of the present machine. It returns in the form of `"machine_1"`.
