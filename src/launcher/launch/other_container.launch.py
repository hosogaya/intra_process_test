from launch import LaunchDescription
from launch_ros.actions import Node, ComposableNodeContainer, LoadComposableNodes
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    container = ComposableNodeContainer(
        name="my_container", 
        package="rclcpp_components",
        executable="component_container",
        namespace="",
        composable_node_descriptions=[
            ComposableNode(
                package="talker",
                plugin="Talker",
                name="talker",
                extra_arguments=[{"use_intra_process_comms": True}],
            ),
        ],
        output="screen",
    )
    
    container2 = ComposableNodeContainer(
        name="my_container2", 
        package="rclcpp_components",
        executable="component_container",
        namespace="",
        composable_node_descriptions=[
            ComposableNode(
                package="listener",
                plugin="Listener",
                name="listener",
                extra_arguments=[{"use_intra_process_comms": True}],
            ),
        ],
        output="screen",
    )
    
    return LaunchDescription([
        container, 
        container2
    ])