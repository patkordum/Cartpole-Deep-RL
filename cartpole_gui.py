import gymnasium as gym
from stable_baselines3 import DQN

# Load trained model
model_path = "dqn_cartpole_model.zip"
model = DQN.load(model_path)

# Create environment with GUI rendering
env = gym.make("CartPole-v1", render_mode="human")

# Run the agent for several episodes
episodes = 500
for ep in range(episodes):
    obs, _ = env.reset()
    done = False
    total_reward = 0
    while not done:
        # Predict action from model
        action, _ = model.predict(obs, deterministic=True)
        obs, reward, done, truncated, _ = env.step(action)
        total_reward += reward
        #print(action, obs)
    print(f"Episode {ep + 1}: Total reward = {total_reward}")

env.close()
