#!/bin/bash

IMAGE_NAME=sq2_ccv_simulator

xhost + 

SCRIPT_DIR=$(cd $(dirname $0); pwd)

nvidia-docker run -it --rm \
  --privileged \
  --runtime=nvidia \
  --env=QT_X11_NO_MITSHM=1 \
  --env="DISPLAY" \
  --volume="/etc/group:/etc/group:ro" \
  --volume="/etc/passwd:/etc/passwd:ro" \
  --volume="/etc/shadow:/etc/shadow:ro" \
  --volume="/etc/sudoers.d:/etc/sudoers.d:ro" \
  --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
  --net="host" \
  --volume="$SCRIPT_DIR/:/root/catkin_ws/src/sq2_ccv_description/" \
  $IMAGE_NAME
