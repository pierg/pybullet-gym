import gym
import time
from stable_baselines3 import PPO

env = gym.make('CartPole-v0')
env.render()
env.reset()
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10_000)

obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    if (i % 100) == 0:
        print(f"Rendering...{i}")
        env.render()
    if done:
        obs = env.reset()

env.close()
