#include <listener/listener.hpp>

Listener::Listener(const rclcpp::NodeOptions options)
: rclcpp::Node("listener", options)
{
    sub_ = create_subscription<std_msgs::msg::String>(
        "topic", 1, std::bind(&Listener::callbackString, this, std::placeholders::_1)
    );
}

Listener::~Listener() {}

void Listener::callbackString(const std_msgs::msg::String::UniquePtr msg)
{
    RCLCPP_INFO(get_logger(), "Received msg address: %x", &(msg->data));
}

#include <rclcpp_components/register_node_macro.hpp>
RCLCPP_COMPONENTS_REGISTER_NODE(Listener);