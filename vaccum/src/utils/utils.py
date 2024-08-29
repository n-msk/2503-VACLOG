import os
import json
from datetime import datetime
from zoneinfo import ZoneInfo

def load_config():
    with open("./src/configs/runtime_config.json", "r") as f:
        config = json.load(f)
    exp = config["EXPERIMENT"]
    chp = config["CHECKPOINT"]

    save_dir = f"./data/experiments/{exp}/checkpoints/{chp}"
    config["save_dir"] = save_dir
    exp_st_time = datetime.now(ZoneInfo("Asia/Tokyo"))
    config["time_started"] = exp_st_time.isoformat()

    date = exp_st_time.strftime('%Y%m%d_%H%M%S')
    name = 'VacuumLog_' + date
    config["filename"] = name

    return config
    

def setup_dir(save_dir):
    is_exists_ok = True
    os.makedirs(f"{save_dir}", exist_ok=is_exists_ok)
    os.makedirs(f"{save_dir}/vaccum", exist_ok=is_exists_ok)
    os.makedirs(f"{save_dir}/vaccum/data", exist_ok=is_exists_ok)
    os.makedirs(f"{save_dir}/vaccum/plot", exist_ok=is_exists_ok)

    return 0

def setup_storage(config):
    save_dir = config["save_dir"]
    setup_dir(save_dir)
    with open(f"{save_dir}/vaccum/data/runtime_config.json", mode="w") as f:
        json.dump(config, f)

    return save_dir
