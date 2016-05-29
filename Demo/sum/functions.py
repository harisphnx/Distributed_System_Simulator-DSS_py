
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
