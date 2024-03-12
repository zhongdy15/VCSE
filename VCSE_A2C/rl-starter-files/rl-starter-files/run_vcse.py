import os
import time

for task in {'SimpleCrossingS9N1'}:
    for seed in {1,2,3,4}:
        cmd_line = f"python3 -m scripts.train --algo a2c --env MiniGrid-{task}-v0 --model {task}/MiniGrid-{task}-v0-vcse-{seed} " \
                   f"--save-interval 100 --frames 10000 --use_entropy_reward --use_value_condition --seed {seed} --beta 0.005 --use_batch &"
        print(cmd_line)
        os.system(cmd_line)
        time.sleep(5)
