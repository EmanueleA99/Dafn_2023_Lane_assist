import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    ld = LaunchDescription()

    # Build config file path
    config_file = os.path.join(
        get_package_share_directory('my_opencv_demo'),
        'config',
        'lane_sub.yaml'
    )

    node = Node(
            package='my_opencv_demo',
            executable='lane_sub',
            output = 'screen',
            emulate_tty = True,
            name='lane_sub',
            namespace='car1',
            parameters=[config_file])

    ld.add_action(node)

    return ld
