import os
import time
gpu_id = 1
time_flag = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
for task in {'SimpleCrossingS9N1'}:
    for seed in {1,2,3,4}:
        cmd_line = f"CUDA_VISIBLE_DEVICES={gpu_id} python3 -m scripts.train --algo a2c --env MiniGrid-{task}-v0 --model {task}/MiniGrid-{task}-v0-vcse-{seed} " \
                   f"--save-interval 100 --frames 1000000 --use_entropy_reward --use_value_condition --seed {seed} --beta 0.005 --use_batch"
        print(cmd_line)
        os.system(cmd_line)
        time.sleep(5)
