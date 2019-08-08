from launch import LaunchDescription
import launch.actions
import launch.substitutions
import launch_ros.actions

def generate_launch_description():
    gzserver_exe = launch.actions.ExecuteProcess(
        cmd=['gzserver', '--verbose', '-s', 'libgazebo_ros_factory.so', '-s', 'libgazebo_ros_init.so',
             launch.substitutions.LaunchConfiguration('world')],
        output='screen'
    )
    
    gzclient_exe = launch.actions.ExecuteProcess(
        cmd=['gzclient'],
        output='screen'
    )

    spawn_ccv = launch_ros.actions.Node(package='sq2_ccv_manipulation', node_executable='spawn_ccv',
             output='screen'),

    return LaunchDescription([
        launch.actions.DeclareLaunchArgument(
          'world',
          default_value=['empty.world', ''],
          description='Gazebo world file'),
        gzserver_exe,
        gzclient_exe,
        spawn_ccv,
    ])