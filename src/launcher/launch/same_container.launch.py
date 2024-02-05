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
    
    load_composable_nodes = LoadComposableNodes(
        target_container="my_container",
        composable_node_descriptions=[
            ComposableNode(
                package="listener",
                plugin="Listener",
                name="listener",
                extra_arguments=[{"use_intra_process_comms": True}],
            ),
        ],
    )
    
    return LaunchDescription([
        container, 
        load_composable_nodes
    ])