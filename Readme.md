# Intra process test

## Success case
* `ros2 launch launcher same_container.launch.py`
* `ros2 run launcher executer`

# Faild case
* `ros2 launch launcher nodes.launch.py`
* `ros2 launch launcher other_container.launch.py`