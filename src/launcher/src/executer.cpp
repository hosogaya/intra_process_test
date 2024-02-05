#include <rclcpp/rclcpp.hpp>
#include <talker/talker.hpp>
#include <listener/listener.hpp>

int main(int argc, char** argv)
{
    rclcpp::init(argc, argv);
    rclcpp::NodeOptions options = rclcpp::NodeOptions().use_intra_process_comms(true);

    rclcpp::Node::SharedPtr talker = std::make_shared<Talker>(options);
    rclcpp::Node::SharedPtr listener = std::make_shared<Listener>(options);

    rclcpp::executors::SingleThreadedExecutor executer;
    executer.add_node(talker);
    executer.add_node(listener);

    executer.spin();

    rclcpp::shutdown();

    return 0;
}