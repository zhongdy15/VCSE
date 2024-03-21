import os
import time
gpu_id_list = 6
time_flag = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
task_set = {"LavaGapS7", "Empty-16x16", "DoorKey-6x6", "DoorKey-8x8", "Unlock"}
task_set = {"SimpleCrossingS9N1"}


gpu_id_list = 6
task_set_0320 = {"MultiRoom-N6","Fetch-8x8-N3","GoToObject-8x8-N2","GoToDoor-8x8",
                 "PutNear-8x8-N3","LockedRoom","KeyCorridorS6R3","LavaCrossingS11N5",
                 "DistShift2","RedBlueDoors-8x8"}
task_set = {"DistShift2","RedBlueDoors-8x8"}

task_type = "MiniGrid"

gpu_id_list = 1
task_set = {"GoToLocal","GoToRedBall"}
task_type = "BabyAI"

for task in task_set:#{'SimpleCrossingS9N1'}:
    for seed in {1,2,3,4}:
        cmd_line = f"CUDA_VISIBLE_DEVICES={gpu_id_list} python3 -m scripts.train --algo a2c --env {task_type}-{task}-v0 --model {task+'_'+time_flag}/{task_type}-{task}-v0-nextsentksg-{seed} " \
                   f"--save-interval 100 --frames 2000000 --use_entropy_reward --use_nextstate_entropy_reward --use_ksg --seed {seed} --beta 0.005"
        print(cmd_line)
        os.system(cmd_line)
        time.sleep(5)
