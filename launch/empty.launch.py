from launch import LaunchDescription
import launch.actions
import launch.substitutions
import launch_ros.actions
import os

moidel = os.path.relpath


def generate_launch_description():
    # Don't forget to include "libgazebo_ros_factory.so" if using spawn command
    gzserver_exe = launch.actions.ExecuteProcess(
        cmd=['gzserver', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so',
             launch.substitutions.LaunchConfiguration('world')],
        output='screen'
    )
    
    gzclient_exe = launch.actions.ExecuteProcess(
        cmd=['gzclient'],
        output='screen'
    )

    return LaunchDescription([
        launch.actions.DeclareLaunchArgument(
          'world',
          default_value=['empty.world', ''],
          description='Gazebo world file'),
        gzserver_exe,
        gzclient_exe,
    ])