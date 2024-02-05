#include <rclcpp/rclcpp.hpp>
#include <std_msgs/msg/string.hpp>

class Listener: public rclcpp::Node
{
public:
    Listener(const rclcpp::NodeOptions options = rclcpp::NodeOptions().use_intra_process_comms(true));
    ~Listener();

private:
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr sub_;
    void callbackString(const std_msgs::msg::String::UniquePtr msg);
};