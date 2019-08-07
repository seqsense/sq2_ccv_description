#!/bin/bash

IMAGE_NAME=sq2_future_vision_simulator

xhost + 

SCRIPT_DIR=$(cd $(dirname $0); pwd)

nvidia-docker run -it --rm \
  --privileged \
  --runtime=nvidia \
  --env=QT_X11_NO_MITSHM=1 \
  --env="DISPLAY" \
  # --volume="$PWD/:/home/repo/"
  --volume="/etc/group:/etc/group:ro" \
  --volume="/etc/passwd:/etc/passwd:ro" \
  --volume="/etc/shadow:/etc/shadow:ro" \
  --volume="/etc/sudoers.d:/etc/sudoers.d:ro" \
  --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
  --net="host" \
  --volume="$SCRIPT_DIR/:/home/repo/future_vision/src/sq2_future_vision_description/" \
  --volume="$SCRIPT_DIR/../diff_drive_steering_controller/:/home/repo/future_vision/src/diff_drive_steering_controller/" \
  --volume="$SCRIPT_DIR/../sq2_ccv_upper_body_controller/:/home/repo/future_vision/src/sq2_future_vision_top_controller/" \
  $IMAGE_NAME 
