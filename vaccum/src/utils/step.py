from datetime import datetime
from zoneinfo import ZoneInfo
from time import time
import threading
from .writer import write_buffer_data, plot_recent_graph
from .manager import canvas_close
from .manager import get_resource_instance, init_properties, init_tkinter


    
class Loop():
    def __init__(self, config, rm):
        self.config = config
        self.port =  config["usb_port_id"]
        self.interval = config["interval"]
        self.total = config["total_time_s"]
        if self.total ==None:
            pass
        else:
            self.total = self.total * 1000
        self.data_path = config["save_dir"] + "/vaccum"
        self.filename = config["filename"]
        self.export_interval = config["data_export_interval"]

        self.inst = get_resource_instance(rm, self.port)
        _ = init_properties(self.inst, self.data_path, self.filename, config)
        
        self.start_time = time()
        self.time_passed = 0
        self.count = 0
        self.save_first = True
        # self.inv_interval = max(1, int(1. / self.interval))
        self.buffer = []


    
    def tkinter_step(self, canvas, root, rm):
        if (self.total == None) or (self.total > self.time_passed):
            try:
                self.count += 1
                s = self.single_taking()
                if self.count % self.interval == 0:
                    if s:
                        self.buffer.append(s)
                    if len(self.buffer) > self.export_interval:
                        if self.save_first:
                            self.save_first = False
                        else:
                            pass
                            # self.write_thread.join()
                        write_buffer_data(self.buffer, self.data_path, self.filename)
                        self.buffer = []
                        plot_recent_graph(self.data_path, self.filename, self.count, self.config)
                        # self.write_thread = threading.Thread(target=write_buffer_data, args=(self.buffer, self.data_path, self.filename))
                        # self.write_thread.start()
                        
                if s != None:
                    canvas.itemconfig('mytext', text=s[self.config["desired_column_index"]])
            except:
                pass
            root.after(1, self.tkinter_step, canvas, root, rm)
        else:
            print('closing')
            canvas_close(None, rm, root)

            exit()

            return 0

    def single_taking(self):
        s = self.inst.read()
        if (s=='\x15\r\n') or (s=='0001\r\n') or (s=='\x06\r\n') or (s=='0000\r\n'):
            return None
        else:
            datetime_str = datetime.now(ZoneInfo('Asia/Tokyo')).isoformat()
            self.time_passed = time() - self.start_time
            s = [datetime_str, self.time_passed] + s[:-2].split(',') #-2 removes \n
            return s