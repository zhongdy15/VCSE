import os
import time
time_flag = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
gpu_id_list = [4,4,4,4]
task_set = {"LavaGapS7", "Empty-16x16", "DoorKey-6x6", "DoorKey-8x8", "Unlock"}
for task in task_set:#{'SimpleCrossingS9N1'}:
    for seed in {1,2,3,4}:
        cmd_line = f"CUDA_VISIBLE_DEVICES={gpu_id_list[seed-1]} python3 -m scripts.train --algo a2c --env MiniGrid-{task}-v0 --model {task+'_'+time_flag}/MiniGrid-{task}-v0-original-{seed} " \
                   f"--save-interval 100 --frames 1000000 --seed {seed} --use_batch"
        print(cmd_line)
        os.system(cmd_line)
        time.sleep(5)
