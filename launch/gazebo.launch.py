import asyncio
import logging
import os
import threading

from ament_index_python.packages import get_package_share_directory
import launch
import launch_ros
import rclpy
from geometry_msgs.msg import Pose
from gazebo_msgs.srv import SpawnEntity

_logger = logging.getLogger('empty_world.launch')


class Spawn(launch.action.Action):
    __node_lock = threading.Lock()
    __node = None

    def __init__(self, name, xml, initial_pose=None, robot_namespace="",
                 **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__xml = xml
        self.__robot_namespace = robot_namespace
        if initial_pose is None:
            self.__initial_pose = Pose()
            self.__initial_pose.orientation.w = 1.0
        else:
            self.__initial_pose = initial_pose
        self.__completed_future = None

    @classmethod
    def _get_node(cls):
        # https://en.wikipedia.org/wiki/Double-checked_locking
        if not cls.__node:
            with cls.__node_lock:
                if not cls.__node:
                    cls.__node = rclpy.create_node('Spawner')
                    rclpy.get_global_executor().add_node(cls.__node)
        return cls.__node

    async def _wait_and_spawn(self, context):
        try:
            node = self._get_node()
            cli = node.create_client(SpawnEntity, 'spawn_entity')
            while True:
                if cli.service_is_ready():
                    res = await cli.call_async(SpawnEntity.Request(
                        name=self.__name,
                        xml=self.__xml,
                        robot_namespace=self.__robot_namespace,
                        initial_pose=self.__initial_pose))
                    if not res.success:
                        _logger.error("failed to spawn: {0}".
                                      format(res.status_message))
                    else:
                        _logger.info("spawned: {0}".
                                     format(res.status_message))
                    break
                await asyncio.sleep(1)
        finally:
            node.destroy_client(cli)

        self.__completed_future.set_result(None)

    def execute(self, context):
        self.__completed_future = context.asyncio_loop.create_future()
        context.asyncio_loop.create_task(self._wait_and_spawn(context))
        return None

    def get_asyncio_future(self):
        return self.__completed_future

def generate_launch_description():
    gzserver_exe = launch.actions.ExecuteProcess(
        cmd=['gzserver', '--verbose',
             '-s', 'libgazebo_ros_factory.so',
             '-s', 'libgazebo_ros_init.so',
             launch.substitutions.LaunchConfiguration('world')],
        output='screen'
    )
    
    gzclient_exe = launch.actions.ExecuteProcess(
        cmd=['gzclient'],
        output='screen'
    )

    REPO = "sq2_ccv_description"

    namespace = "sq2_ccv"

    # Get path to the robot sdf file
    sdf = os.path.join(
        get_package_share_directory(REPO), "models",
        "sq2_ccv", "model.sdf")
    xml = open(sdf, 'r').read()

    p = Pose()
    spawn_ccv = Spawn(
        'sq2_ccv', xml, initial_pose=p, robot_namespace=namespace)

    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(
          'world',
          default_value=['empty.world', ''],
          description='Gazebo world file'),
        gzserver_exe,
        gzclient_exe,
        spawn_ccv,
    ])