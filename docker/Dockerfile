FROM osrf/ros:melodic-desktop

RUN apt update

RUN apt install -y sudo\
                       wget\
                       lsb-release\
                       mesa-utils

RUN echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-latest.list \
         && wget http://packages.osrfoundation.org/gazebo.key -O - | apt-key add -

RUN apt update

RUN apt install -y ros-melodic-gazebo-ros-control \
                       ros-melodic-ros-controllers \
                       ros-melodic-gazebo-ros-pkgs \
                       ros-melodic-ros-control \ 
    && rm -rf /var/lib/apt/lists/*

# nvidia environment
# for 1
LABEL com.nvidia.volumes.needed="nvidia_driver"
ENV PATH /usr/local/nvidia/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/nvidia/lib:/usr/local/nvidia/lib64:${LD_LIBRARY_PATH}
# for 2
ENV NVIDIA_VISIBLE_DEVICES ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

#ros setting
WORKDIR /root

RUN /bin/bash -c "mkdir -p catkin_ws/src"

RUN cd catkin_ws/src && /bin/bash -c "source /opt/ros/melodic/setup.bash; catkin_init_workspace"

RUN cd catkin_ws && /bin/bash -c "source /opt/ros/melodic/setup.bash; catkin_make"

RUN cd /root && echo source /root/catkin_ws/devel/setup.bash >> .bashrc

ENV ROS_PACKAGE_PATH=/root/catkin_ws:$ROS_PACKAGE_PATH

ENV ROS_WORKSPACE=/root/catkin_ws

RUN ln -sf /usr/include/eigen3/Eigen /usr/include/Eigen

RUN apt update 
RUN apt install -y x11-apps

RUN apt clean \
    && rm -rf /var/lib/apt/lists/*
