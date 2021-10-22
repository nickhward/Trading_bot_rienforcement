# Trading_bot_rienforcement
System:
- Ubuntu 16.04
- GPU (GeForce GTX 1080 Ti)


Instructions:

In order to run the code:

Make sure to clone the stable baselines repository (this is a repo that holds popular reinforcement learning algorithms, such as DeepQ, HER, A2C, etc):
```
cd
git clone https://github.com/hill-a/stable-baselines.git
```

First clone the Github Repository using terminal commands.

```
git clone https://github.com/nickhward/Trading_bot_rienforcement.git
```

Run the setup script to install required dependencies.
```
cd ~/Trading_bot_rienforcement
pip3 install -e .
```


To run the reinforcement learning agent type the command in the same directory as `pip3 install -e.'
```
python3 bot_training.py
```

You should see initial values like such running over and over until it reaches 1000000 timesteps:

![image](https://user-images.githubusercontent.com/78880630/138394972-58f1b4cb-6bef-4cd1-8584-4de2dcea3dbc.png)

And a graph that looks similar to this when it is finished running through the timesteps:
![image](https://user-images.githubusercontent.com/78880630/138395802-e65ecd75-fb67-4f90-9a0f-be69f14d9ea1.png)


