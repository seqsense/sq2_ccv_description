cd `dirname $0`

. /usr/share/gazebo/setup.sh
. ~/ws/install/setup.bash
export GAZEBO_RESOURCE_PATH=~/ccv_ws/src/sq2_ccv_description/worlds:${GAZEBO_RESOURCE_PATH}
