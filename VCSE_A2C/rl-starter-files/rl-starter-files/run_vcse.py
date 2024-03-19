import os
import time
gpu_id = 1
time_flag = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())

task_set = {"LavaGapS7", "Empty-16x16", "DoorKey-6x6", "DoorKey-8x8", "Unlock"}
task_set = {"DoorKey-8x8"}
for task in task_set:#{'SimpleCrossingS9N1'}:
    for seed in {1,2,3,4}:
        cmd_line = f"CUDA_VISIBLE_DEVICES={gpu_id} python3 -m scripts.train --algo a2c --env MiniGrid-{task}-v0 --model {task+'_'+time_flag}/MiniGrid-{task}-v0-vcse-{seed} " \
                   f"--save-interval 100 --frames 3000000 --use_entropy_reward --use_value_condition --seed {seed} --beta 0.005 --use_batch"
        print(cmd_line)
        os.system(cmd_line)
        time.sleep(5)
