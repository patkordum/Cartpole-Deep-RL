import gymnasium as gym
from stable_baselines3 import DQN  # Deep Q-Network agent
import os

# Train or load the model
model_path = "dqn_cartpole_model"

# Create the CartPole environment
env = gym.make("CartPole-v1")

# Check if a trained model exists, otherwise train a new one
if os.path.exists(model_path + ".zip"):
    print("Loading existing model...")
    model = DQN.load(model_path, env=env)
else:
    print("Training new DQN model...")
    # DQN uses a neural network to approximate Q-values
    model = DQN("MlpPolicy", env, verbose=1)  # MLP = Multi-Layer Perceptron
    model.learn(total_timesteps=500_000)      # Train for 100,000 time steps
    model.save(model_path)
    print(f"Model saved to {model_path}.zip")

# Run a few test episodes to see how the agent performs
episodes = 200
for ep in range(episodes):
    obs, _ = env.reset()
    done = False
    total_reward = 0
    while not done:
        # Choose action based on trained model (no exploration)
        action, _states = model.predict(obs, deterministic=True)
        obs, reward, done, truncated, info = env.step(action)
        total_reward += reward
        env.render()  # Show animation in terminal (if supported)

    print(f"Episode {ep + 1}: Total reward = {total_reward}")

env.close()
