from launch import LaunchDescription
import launch.actions
import launch.substitutions
import launch_ros.actions
import os

moidel = os.path.relpath


def generate_launch_description():
    gzserver_exe = launch.actions.ExecuteProcess(
        cmd=['gzserver', '--verbose', '-s', 'libgazebo_ros_init.so',
             launch.substitutions.LaunchConfiguration('world')],
        output='screen'
    )
    
    gzclient_exe = launch.actions.ExecuteProcess(
        cmd=['gzclient'],
        output='screen'
    )

    keyboard_pub = launch_ros.actions.Node(
        package='travel',
        node_executable='keyboard_publisher',
        output='screen',
    )

    obj_detect_pub = launch_ros.actions.Node(
        package='travel',
        node_executable='object_detection_publisher',
        output='screen',
    ) 

    agent = launch_ros.actions.Node(
        package='travel',
        node_executable='agent',
        output='screen',
    )

    paused = launch.

    return LaunchDescription([
        launch.actions.DeclareLaunchArgument(
          'world',
          default_value=['empty.world', ''],
          description='Gazebo world file'),
        gzserver_exe,
        gzclient_exe,
        keyboard_pub,
        obj_detect_pub,
        agent
        #ローンチ時にプログラムを実行する
    ])