import gym  # open ai gym
from gym.envs.registration import register
from stable_baselines3 import PPO

# Quadrotors with Plus(+)-configuration
register(
    id='QuadrotorPlusHoverEnv-v0',
    entry_point='gym_multirotor.envs.mujoco.quadrotor_plus_hover:QuadrotorPlusHoverEnv'
)

register(
    id='TiltrotorPlus8DofHoverEnv-v0',
    entry_point='gym_multirotor.envs.mujoco.tiltrotor_plus_hover:TiltrotorPlus8DofHoverEnv'
)

# Quadrotor with X-configuration
register(
    id='QuadrotorXHoverEnv-v0',
    entry_point='gym_multirotor.envs.mujoco.quadrotor_x_hover:QuadrotorXHoverEnv'
)

env = gym.make('QuadrotorPlusHoverEnv-v0')
env.render()  # call this before env.reset, if you want a window showing the environment
env.reset()  # should return a state vector if everything worked


for i in range(10000):
    env.step(env.action_space.sample())
    print(i)
    time.sleep(0.5)
    env.render()
    print(f"rendered {i}")
