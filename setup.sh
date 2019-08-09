cd `dirname $0`

. /usr/share/gazebo/setup.sh
. ~/ccv_ws/install/setup.bash
export GAZEBO_MODEL_PATH=~/ccv_ws/src/sq2_ccv_description/models:${GAZEBO_MODEL_PATH}
export GAZEBO_RESOURCE_PATH=~/ccv_ws/src/sq2_ccv_description/worlds:${GAZEBO_RESOURCE_PATH}
