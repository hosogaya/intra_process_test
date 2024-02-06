from launch import LaunchDescription
from launch_ros.actions import Node, ComposableNodeContainer, LoadComposableNodes
from launch_ros.descriptions import ComposableNode
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription
from launch.substitutions import TextSubstitution
from ament_index_python import get_package_share_directory

def generate_launch_description():
    container_name = "talker_listener_container"
    container = ComposableNodeContainer(
        name=container_name, 
        package="rclcpp_components",
        executable="component_container",
        namespace="",
        output="screen",
    )

    listener = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory("listener"), '/launch/listener.launch.py']), 
        launch_arguments={'container_name': TextSubstitution(text=container_name)}.items()
    )

    talker = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([get_package_share_directory("talker"), '/launch/talker.launch.py']), 
        launch_arguments={'container_name': TextSubstitution(text=container_name)}.items()
    )

    return LaunchDescription([
        container, 
        listener, 
        talker
    ])