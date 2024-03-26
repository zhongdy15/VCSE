import os
import time
time_flag = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
task_set = {"LavaGapS7", "Empty-16x16", "DoorKey-6x6", "DoorKey-8x8", "Unlock"}
task_set = {"DoorKey-8x8"}

gpu_id_list = 5
task_set_0320 = {"MultiRoom-N6","Fetch-8x8-N3","GoToObject-8x8-N2","GoToDoor-8x8",
                 "PutNear-8x8-N3","LockedRoom","KeyCorridorS6R3","LavaCrossingS11N5",
                 "DistShift2","RedBlueDoors-8x8"}
task_set = {"DistShift2","RedBlueDoors-8x8"}

task_type = "MiniGrid"

gpu_id_list = 4
task_set = {"PutNextLocal","PickupLoc"}
task_type = "BabyAI"

for task in task_set:#{'SimpleCrossingS9N1'}:
    for seed in {1,2,3,4}:
        cmd_line = f"CUDA_VISIBLE_DEVICES={gpu_id_list} python3 -m scripts.train --algo a2c --env {task_type}-{task}-v0 --model {task+'_'+time_flag}/{task_type}-{task}-v0-original-{seed} " \
                   f"--save-interval 100 --frames 2000000 --seed {seed} --use_batch"
        print(cmd_line)
        os.system(cmd_line)
        time.sleep(5)
