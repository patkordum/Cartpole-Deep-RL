import gymnasium as gym
from stable_baselines3 import DQN

# Load the environment with GUI rendering
env = gym.make("CartPole-v1", render_mode="human")

# Load the trained model from file
model = DQN.load("dqn_cartpole_model", env=env)

# Run the agent for 1 episode
obs, _ = env.reset()
done = False
total_reward = 0

while not done:
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, done, truncated, _ = env.step(action)
    total_reward += reward

print(f"Episode reward: {total_reward}")
env.close()
