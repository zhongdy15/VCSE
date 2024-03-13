import os
import time
gpu_id_list = [4,4,4,4]
for task in {'SimpleCrossingS9N1'}:
    for seed in {1,2,3,4}:
        cmd_line = f"CUDA_VISIBLE_DEVICES={gpu_id_list[seed]} python3 -m scripts.train --algo a2c --env MiniGrid-{task}-v0 --model {task}/MiniGrid-{task}-v0-sent-{seed} " \
                   f"--save-interval 100 --frames 1000000 --use_entropy_reward --seed {seed} --beta 0.005"
        print(cmd_line)
        os.system(cmd_line)
        time.sleep(5)
