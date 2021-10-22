import numpy as np
import pandas as pd

import gym

import quantstats as qs
name_date = 'Date'
df = pd.read_csv('/home/nicholasward2/trading-bot/gym_trading/datasets/data/max_bitcoin_data.csv', parse_dates=True, index_col=name_date)
from stable_baselines import A2C

#df.head()
from stocks_env import StocksEnv
from stable_baselines import DQN
from stable_baselines.common.vec_env import DummyVecEnv

import matplotlib.pyplot as plt
from stable_baselines.deepq.policies import MlpPolicy


#df = gym_bot_trading.datasets.bitcoin_dataset.copy()

window_size = 10
start_index = window_size
end_index = len(df)

env_maker = lambda: gym.make(
    'stocks-v0',
    df = df,
    window_size = window_size,
    frame_bound = (start_index, end_index)
)

env = DummyVecEnv([env_maker])
policy_kwargs = dict(net_arch=[64, 'lstm', dict(vf=[128, 128, 128], pi=[64, 64])])
model = A2C('MlpLstmPolicy', env, verbose=1, policy_kwargs=policy_kwargs)
model.learn(total_timesteps=(1000000))


env = env_maker()
observation = env.reset()

while True:
    observation = observation[np.newaxis, ...]

    # action = env.action_space.sample()
    action, _states = model.predict(observation)
    observation, reward, done, info = env.step(action)

    # env.render()
    if done:
        print("info:", info)
        break


plt.figure(figsize=(16, 6))
env.render_all()
plt.show()


qs.extend_pandas()

net_worth = pd.Series(env.history['total_profit'], index=df.index[start_index+1:end_index])
returns = net_worth.pct_change().iloc[1:]

qs.reports.full(returns)
qs.reports.html(returns, output='a2c_quantstats.html')



