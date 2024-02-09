# Teb with RTabmap

RTabmap is RGB-D SLAM approach based on a global loop closure detector with real-time constraints. This package can be used to generate a 3D point clouds of the environment and/or to create a 2D occupancy grid map for navigation.

Teb is used as path planning method after Mabbing with Rtab then we provide the robot goal to reach in this Mab to move it without manual control

## Dependencies

- Install Rtabmap package by the following command

```bash
sudo apt update

sudo apt install ros-noetic-rtabmap-ros
```

- Setup kinect v1 by following [This](https://www.notion.so/Kinect-v1-Setup-61abfd432e50402a824913e9962a4da5?pvs=21)

## Implementation details

The model used the odomatry from dead_reckoning script and Scan msg from the lidar and RGB image, Depth img, Camera info from kinect V1 

the model updates and correct himself by comparing previous frames to the current frame 

- You can give them mab and use it to localize the robot only by this parameter

```bash
<arg name="localization"      default="false"/> <!-- True make it continue from previes map-->
```

## Launching

```bash
roslaunch shato_bringup bringup_full.launch
#to launch odom, Rplidar and kinect V1

roslaunch mia_rtabmap teb_rtab.launch
#To launch Rtab with tep
```

## Problems

- The Lidar and Kinect devices intermittently experience shutdowns or disconnections during usage, particularly when connected via wired connections so it decrease the smoothing of the movement as it will require to launch the file again
- The local costmab in teb was not updated and when we add the robot avoide the obstacles successfully
- Most of the problems came from adjusting the parameters of Rtab like adjusting the update rate to be 10Hz and synchronising the data from the lidar and kinect to be at the same rate
