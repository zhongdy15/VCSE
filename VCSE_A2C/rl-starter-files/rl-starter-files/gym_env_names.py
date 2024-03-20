import gym
import gym_minigrid

# 获取所有注册的gym环境名称
env_ids = [env_spec.id for env_spec in gym.envs.registry.all()]
minigrid_envs = [env_id for env_id in env_ids if 'MiniGrid' in env_id]
# 打印环境名称列表
with open('minigrid_envs.txt', 'w') as f:
    for env_name in minigrid_envs:
        f.write(env_name + '\n')

print("已将所有包含 'minigrid' 的环境名称保存到 minigrid_envs.txt 文件中.")
