import gym  # open ai gym
import pybulletgym  # register PyBullet enviroments with open ai gym
from stable_baselines3 import PPO
import time


env = gym.make('HumanoidPyBulletEnv-v0')
env.render() # call this before env.reset, if you want a window showing the environment
env.reset()  # should return a state vector if everything worked


for i in range(10000):
    env.step(env.action_space.sample())
    print(i)
    time.sleep(0.1)
    env.render()
    print(f"rendered {i}")
