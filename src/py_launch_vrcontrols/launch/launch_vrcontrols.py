#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""An example calling multiple launch files"""

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch.actions import SetEnvironmentVariable


def generate_launch_description():    # export TURTLEBOT3_MODEL=waffle
    turtlebot_model = SetEnvironmentVariable(name="TURTLEBOT3_MODEL", value=["burger"])

    # ros2 launch turtlebot3_bringup robot.launch.py
    robot_launch = IncludeLaunchDescription(
        launch_description_source=PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [
                    FindPackageShare("turtlebot3_bringup"),
                    "launch",
                    "robot.launch.py",
                ]
            )
        )
    )

    # ros2 launch nav2_bringup navigation_launch.py
    navigation_launch = IncludeLaunchDescription(
        launch_description_source=PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [
                    FindPackageShare("nav2_bringup"),
                    "launch",
                    "navigation_launch.py"
                ]
            )
        ),
        launch_arguments={
            'params_file': '/home/ubuntu/nav2_params.yaml'
        }.items()
    )

    # ros2 launch slam_toolbox online_sync_launch.py
    online_launch = IncludeLaunchDescription(
        launch_description_source=PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [
                    FindPackageShare("slam_toolbox"),
                    "launch",
                    "online_sync_launch.py",
                ]
            )
        )
    )
    #
    # # ros2 launch rosbridge_server rosbridge_websocket_launch.xml
    # rosbridge_launch = IncludeLaunchDescription(
    #     launch_description_source=XMLLaunchDescriptionSource(
    #         PathJoinSubstitution(
    #             [
    #                 FindPackageShare("rosbridge_server"),
    #                 "launch",
    #                 "rosbridge_websocket_launch.xml",
    #             ]
    #         )
    #     ),
    # )

    ld = LaunchDescription()
    ld.add_action(turtlebot_model)
    ld.add_action(navigation_launch)
    ld.add_action(robot_launch)
    ld.add_action(online_launch)
    # ld.add_action(rosbridge_launch)
    return ld