import csv
import tkinter as tk
import time

def get_resource_instance(resource_manager, port_id):
    usb = resource_manager.list_resources()
    print('usb resources', usb)
    gauge = usb[port_id]
    inst = resource_manager.open_resource(gauge)

    return inst

def init_properties(inst, data_path, filename, config):
    inst.write('COM,0')
    inst.read()
    inst.write('\x05')

    with open(data_path + f"/data/{filename}.csv", mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(config["data_header"])

    return 0

def canvas_close(event, rm, root):
    time.sleep(1)
    rm.close()
    print("safely shut rm")
    time.sleep(1)
    root.destroy()
    print('safely destroyed root')
    
    return 0

def init_tkinter(rm):
    root = tk.Tk()
    frame = tk.Frame(root)

    button = tk.Button(frame, text='Close')
    button.grid(row=0, column=10, padx=5, sticky='e')
    button.bind('<Button-1>', lambda x: canvas_close(x, rm, root))

    canvas = tk.Canvas(frame, bg='#ffffff', width=800, height=400)
    canvas.grid(row=1, columnspan=11, rowspan=1)

    frame.pack()
    canvas.create_text(400, 200, text='', font=('Gothic', 100), tags='mytext')

    return canvas, root
