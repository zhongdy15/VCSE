#!/bin/bash
# envs=("Hopper-v4" "Walker2d-v4" "HalfCheetah-v4" "Ant-v4" "Humanoid-v4" "Reacher-v4")
# envs=("dm_control/cartpole-balance_sparse-v0" "dm_control/finger-turn_easy-v0" "dm_control/finger-turn_hard-v0" "dm_control/reacher-easy-v0" "dm_control/reacher-hard-v0")
# tasks=("Hopper Stand" "Walker Walk Sparse" "Walker Walk" "Cheetah Run Sparse" "Cartpole Swingup Sparse" "Pendulum Swingup")
envs=("cartpole_swingup_sparse" "reacher_easy" "reacher_hard" "finger_turn_easy" "finger_turn_hard")


seeds=(1 2 3)
exp_name="SE"

# 循环创建 tmux 窗口并运行 Python 程序
for env in "${envs[@]}"
do
    # # 创建一个新的 tmux 窗口并命名为 "python$i"
    tmux new-window -n "$exp_name-$env" || tmux select-window -t "$exp_name-$env"
    # tmux select-window -t "$exp_name-$env"

    # 在新窗口中运行 Python 程序，这里假设你的 Python 程序为 example.py
    for seed in "${seeds[@]}"
    do
        tmux send-keys -t "$exp_name-$env" "conda activate rl" C-m
        tmux send-keys -t "$exp_name-$env" "CUDA_VISIBLE_DEVICES=7 python train.py task=$env seed=$seed agent.do_vcse=False agent.do_nse=False" C-m
    done

done

# 切换到第一个窗口（可选）
tmux select-window -t "$exp_name-$env"

# 进入 tmux 会话（可选）
tmux attach-session -d