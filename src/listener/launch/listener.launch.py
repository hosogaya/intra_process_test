from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import TextSubstitution, LaunchConfiguration
from launch_ros.actions import Node, ComposableNodeContainer, LoadComposableNodes
from launch_ros.descriptions import ComposableNode


def generate_launch_description():
    arg_container_name = DeclareLaunchArgument(
        "container_name", default_value=TextSubstitution(text="my_container")
    )

    print(LaunchConfiguration("container_name"))

    load_composable_nodes = LoadComposableNodes(
        target_container=LaunchConfiguration("container_name"),
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
        arg_container_name,
        load_composable_nodes, 
    ])