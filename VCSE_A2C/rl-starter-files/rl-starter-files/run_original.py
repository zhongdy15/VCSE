import os
import time
gpu_id_list = [3,3,3,3]
for task in {'SimpleCrossingS9N1'}:
    for seed in {1,2,3,4}:
        cmd_line = f"CUDA_VISIBLE_DEVICES={gpu_id_list[seed]} python3 -m scripts.train --algo a2c --env MiniGrid-{task}-v0 --model {task}/MiniGrid-{task}-v0-original-{seed} " \
                   f"--save-interval 100 --frames 1000000 --seed {seed} --use_batch"
        print(cmd_line)
        os.system(cmd_line)
        time.sleep(5)
