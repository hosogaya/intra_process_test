#include <talker/talker.hpp>
#include <chrono>

using namespace std::chrono_literals;
Talker::Talker(const rclcpp::NodeOptions options)
: rclcpp::Node("talker", options)
{
    timer_ = create_wall_timer(500ms, std::bind(&Talker::callbackTimer, this));
    pub_ = create_publisher<std_msgs::msg::String>(
        "topic", 1
    );
}

Talker::~Talker() {}

void Talker::callbackTimer()
{
    std_msgs::msg::String::UniquePtr msg(new std_msgs::msg::String);
    msg->data = "Hello world";
    RCLCPP_INFO(get_logger(), "Publish msg address: %x", &(msg->data));
    pub_->publish(std::move(msg));
}

#include <rclcpp_components/register_node_macro.hpp>
RCLCPP_COMPONENTS_REGISTER_NODE(Talker);