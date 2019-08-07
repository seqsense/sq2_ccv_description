ARG FROM_IMAGE=ubuntu:18.04
FROM $FROM_IMAGE


RUN apt-get update
#RUN apt-get upgrade

RUN echo "alias r12='r1;r2'" >> ~/.bashrc
RUN echo "alias r2='source /opt/ros/crystal/setup.bash'" >> ~/.bashrc
RUN echo "alias r1='source /opt/ros/melodic/setup.bash'" >> ~/.bashrc
RUN echo "alias rs='source install/setup.bash && source install/local_setup.bash'" >> ~/.bashrc
RUN echo "alias rl='source install/local_setup.bash'" >> ~/.bashrc
RUN echo "alias gbrc='gedit ~/.bashrc'" >> ~/.bashrc
RUN echo "alias vbrc='vim ~/.bashrc'" >> ~/.bashrc
RUN echo "alias sbrc='source ~/.bashrc'" >> ~/.bashrc
RUN echo "alias agu='apt-get update'" >> ~/.bashrc
#RUN echo "alias agp='apt-get upgrade'" >> ~/.bashrc
RUN echo "alias rip='export ROS_IP=172.16.7.11'" >> ~/.bashrc

RUN apt install -y sudo\
                       wget\
                       lsb-release\
                       mesa-utils

RUN apt install -y    libignition-math4 \
    && rm -rf /var/lib/apt/lists/*

ENV DEBAIN_FRONTEND=noninteractive 


#RUN source ~/.bashrc
RUN /bin/bash -c "source ~/.bashrc"
RUN apt-get install apt-utils -y
RUN cd home && mkdir -p repo/git/yolo && mkdir -p repo/git/ros && cd repo/git/ros/
RUN apt update

RUN apt install curl gnupg2 lsb-release -y

RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/ros-latest.list'
RUN apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
RUN apt-key del 421C365BD9FF1F717815A3895523BAEEB01FA116
RUN apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
RUN apt-get update
#RUN agp
RUN apt-get install -y tzdata
RUN apt install ros-melodic-desktop-full -y
RUN apt search ros-melodic
RUN rosdep init
RUN rosdep update
RUN apt install python-rosinstall python-rosinstall-generator python-wstool build-essential -y
RUN apt-get install ros-melodic-catkin -y
RUN apt-get install ros-melodic-ros* -y
RUN apt-get install ros-melodic-std* -y
RUN apt-get install ros-melodic-rviz* -y
RUN apt-get install ros-melodic-rqt* -y


RUN echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-latest.list \
         && wget http://packages.osrfoundation.org/gazebo.key -O - | apt-key add -


# nvidia environment
# for 1
LABEL com.nvidia.volumes.needed="nvidia_driver"
ENV PATH /usr/local/nvidia/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}
# for 2
ENV NVIDIA_VISIBLE_DEVICES ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics


RUN curl http://repo.ros2.org/repos.key | apt-key add -
RUN sh -c 'echo "deb [arch=amd64,arm64] http://packages.ros.org/ros2/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list'
ARG CHOOSE_ROS_DISTRO=crystal
RUN apt-get update
RUN apt-get install -y tzdata
RUN apt install ros-$CHOOSE_ROS_DISTRO-desktop -y
RUN apt install python3-argcomplete -y
ENV DEBIAN_FRONTEND teletype
RUN apt-get update -y && apt-get install -y --no-install-recommends apt-utils
RUN yes accept | apt-get install ros-crystal-ros* select true | debconf-set-selections
RUN apt-get install ros-crystal-rviz* -y
RUN apt-get install ros-crystal-rqt* -y
RUN apt-get install ros-crystal-camera* -y
RUN apt-get install ros-crystal-cv-bridge* -y
RUN apt-get install ros-crystal-ros1* -y
RUN apt-get install ros-crystal-ros2* -y
RUN apt-get install ros-crystal-rosbag2* -y


RUN apt install python3-colcon-common-extensions -y

RUN apt-get install vim -y

RUN apt install python3-pip -y
RUN apt install python-pip -y
RUN pip3 install opencv-python
RUN pip install opencv-python

COPY requirements.txt /tmp/requirements.txt
ARG GITHUB_USER
ARG GITHUB_TOKEN
RUN touch /root/.netrc && \
    echo machine github.com >> /root/.netrc && \
    echo login $GITHUB_USER >> /root/.netrc && \
    echo password $GITHUB_TOKEN >> /root/.netrc && \
    pip install -r /tmp/requirements.txt && \
    pip3 install -r /tmp/requirements.txt && \
    rm /root/.netrc

#RUN curl https://s3-ap-northeast-1.amazonaws.com/dev-sq-image-processing/keras-yolo3/yolo.h5 -o /app/model_data/yolo.h5




















# FROM osrf/ros:melodic-desktop

# RUN apt update

# RUN apt install -y sudo\
#                        wget\
#                        lsb-release\
#                        mesa-utils

# RUN echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-latest.list \
#          && wget http://packages.osrfoundation.org/gazebo.key -O - | apt-key add -

# RUN apt update

# RUN apt install -y ros-melodic-gazebo-ros-control \
#                        ros-melodic-ros-controllers \
#                        ros-melodic-gazebo-ros-pkgs \
#                        ros-melodic-ros-control \ 
# 					   libignition-math4 \
#     && rm -rf /var/lib/apt/lists/*

# # nvidia environment
# # for 1
# LABEL com.nvidia.volumes.needed="nvidia_driver"
# ENV PATH /usr/local/nvidia/bin:${PATH}
# ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}
# # for 2
# ENV NVIDIA_VISIBLE_DEVICES ${NVIDIA_VISIBLE_DEVICES:-all}
# ENV NVIDIA_DRIVER_CAPABILITIES ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

# #ros setting
# WORKDIR /root

# RUN /bin/bash -c "mkdir -p catkin_ws/src"

# RUN cd catkin_ws/src && /bin/bash -c "source /opt/ros/melodic/setup.bash; catkin_init_workspace"

# RUN cd catkin_ws && /bin/bash -c "source /opt/ros/melodic/setup.bash; catkin_make"

# RUN cd /root && echo source /root/catkin_ws/devel/setup.bash >> .bashrc

# ENV ROS_PACKAGE_PATH=/root/catkin_ws:$ROS_PACKAGE_PATH

# ENV ROS_WORKSPACE=/root/catkin_ws

# RUN ln -sf /usr/include/eigen3/Eigen /usr/include/Eigen

# RUN apt update \
#     && apt install vim -y

# RUN apt clean \
#     && rm -rf /var/lib/apt/lists/*








