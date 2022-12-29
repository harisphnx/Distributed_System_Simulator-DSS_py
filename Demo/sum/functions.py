import dss

# Add a method to the machine class that allows machine instances to send and receive data
def send_data(self, destination_id, data):
    '''
    Send data to the machine with machine_id destination_id.
    '''
    self.send(destination_id, 'data|' + data)

def recv_data(self):
    '''
    Receive data from another machine instance.
    '''
    message, sender = self.recv(is_blocking=True)
    if message.startswith('data|'):
        return message[5:], sender
    else:
        return None, None

dss.Machine.send_data = send_data
dss.Machine.recv_data = recv_data

# Add a method to the machine class that allows machine instances to communicate with a central server
def send_to_server(self, data):
    '''
    Send data to the central server.
    '''
    self.send('server', 'data|' + data)

def recv_from_server(self):
    '''
    Receive data from the central server.
    '''
    message, sender = self.recv(is_blocking=True)
    if message.startswith('data|'):
        return message[5:], sender
    else:
        return None, None

dss.Machine.send_to_server = send_to_server
dss.Machine.recv_from_server = recv_from_server

# Update machine1 and machine2 functions to use the new methods
def machine1(id_var):
    print("machine instance started with id:", id_var.get_machine_id())

    # id_var.get_machine_id() is used to get the machine id

    for i in range(10):
        id_var.send("machine_2", str(i), 1)

    message, sender = id_var.recv(1)

    print(id_var.get_machine_id(), " got sum =", message, " from", sender)

def machine2(id_var):
    print("machine instance started with id:", id_var.get_machine_id())

    # id_var.get_machine_id() is used to get the machine id

    total = 0
    for i in range(10):
        message, sender = id_var.recv(1)
        total += int(message)
    id_var.send("machine_1", str(total), 1)
