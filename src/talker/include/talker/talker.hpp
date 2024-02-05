#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>
#include <chrono>

class Talker: public rclcpp::Node
{
public:
    Talker(const rclcpp::NodeOptions options = rclcpp::NodeOptions().use_intra_process_comms(true));
    ~Talker();

private:
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr pub_;
    rclcpp::TimerBase::SharedPtr timer_;
    void callbackTimer();
};