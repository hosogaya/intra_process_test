from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    talker = Node(
        package='talker', 
        executable='talker_node', 
        name='talker', 
        output = 'screen'
    )
    
    listener = Node(
        package='listener', 
        executable='listener_node', 
        name='listener', 
        output = 'screen'
    )
    
    return LaunchDescription([
        talker, 
        listener
    ])