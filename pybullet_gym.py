import gym  # open ai gym
import pybulletgym  # register PyBullet enviroments with open ai gym
from stable_baselines3 import PPO

env = gym.make('HumanoidPyBulletEnv-v0')
env.render() # call this before env.reset, if you want a window showing the environment
env.reset()  # should return a state vector if everything worked

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10_000)

obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    env.render()
    if done:
        obs = env.reset()

env.close()
