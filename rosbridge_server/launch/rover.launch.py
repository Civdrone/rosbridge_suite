import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

configurable_parameters = [{'name': 'websocket_ping_interval',      'default': '0.5', 'description': ''},
                           {'name': 'websocket_ping_timeout',       'default': '5', 'description': 'time (seconds) until disconnection is announced'},
]

def declare_configurable_parameters(parameters):
    return [DeclareLaunchArgument(param['name'], default_value=param['default'], description=param['description']) for param in parameters]

def set_configurable_parameters(parameters):
    return dict([(param['name'], LaunchConfiguration(param['name'])) for param in parameters])


def generate_launch_description():
    return LaunchDescription(declare_configurable_parameters(configurable_parameters) + [
        Node
        (
            package="rosbridge_server",
            executable="rosbridge_websocket.py",
        )
    ])

