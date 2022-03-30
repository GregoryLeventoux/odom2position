from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='real_pose_viewer',
            executable='real_pose_viewer',
            name='viewer1',
            parameters=[{"subscribed_topic": "/r2d2/odom"},{"published_topic": "/real_position"}]),
        Node(
            package='real_pose_viewer',
            executable='real_pose_viewer',
            name='viewer2',
            parameters=[{"subscribed_topic": "/odometry/filtered"},{"published_topic": "/position/filtered"}])])
