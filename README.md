## Summer School 2024 Workshop 4

We will present how wearable robotics, and specifically exoskeletons, are typically controlled to provide assistance in various activities of daily living (such as overground walking, ramps, stairs, sit-to-stand). In particular, a state machine-based controller will be introduced and students will tune a state machine. We will also present how machine learning (ML) techniques are changing wearable robots control, and students will use data, and a neural network to complete a ML task for wearable robotic locomotion control, and tested in realtime.
Hosted by: Shirley Ryan AbilityLab (SRAlab) – Dr. José L. Pons’ lab: Lorenzo Vianello;  Hospital Los Madroños – Alberto Cantón Gonzalez
Tentative contributions by: Technaid
Relevant populations: stroke, spinal cord injury, amputation
Techniques involved: MATLAB, ROS C++, Gazebo, Python

** WS4 Day 1 **: Finite State Machine Tuning for the X2 exoskeleton
– Introduction to controllers designed to provide assistance to lower-limb exoskeletons in everyday life
– Presentation of the X2 lower limb exoskeleton
– Introduction of planned activities, review of FSM impedance control, and description of control task
– Hands-on tuning of parameters in a simulation
– Hands-on testing and tuning impedance controller on the X2 exoskeleton

** WS4 Day 2 **: Machine Learning for Wearable Robots Control
– Introduction to ML techniques for the control of wearable robots (prosthetic and exoskeletons) designed to provide assistance to lower-limb exoskeletons in everyday life
– Review of ML techniques for regression of locomotion characteristics (gait phase, locomotion mode)
– Hands-on tuning of parameters in a simulation
– Hands-on testing and tuning impedance controller on the X2 exoskeleton

# Dependencies
Before starting the workshop be sure to install the following libraries for python

```bash
pip install jupyter pandas matplotlib numpy tensorflow==2.16 scipy scikit-learn
```

clone the git repository:
```bash
git clone https://github.com/LorenzoVianello95/SSNR24.git
```

# Data:

Download materials from and export in /data folder: 
```bash
https://drive.google.com/drive/folders/14UZmdo3Le2SGO_6KnsqW4aNOsZHobWc4
```