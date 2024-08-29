import pyvisa
from .utils.utils import setup_storage, load_config
from .utils.step import Loop
from .utils.manager import init_tkinter
import json
import time



def loop_vaccum_taking():
    config = load_config()
    setup_storage(config)

    rm = pyvisa.ResourceManager()
    canvas, root = init_tkinter(rm)
    
    try:
        loop = Loop(config, rm)
        loop.tkinter_step(canvas, root, rm)
        root.mainloop()
    finally:
        print('closing completed')

    return 0


        