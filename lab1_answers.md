# Lab 1 Answers

Name: Christopher JH
NRP: <NRP kamu>
Setup: Ubuntu 26.04, ROS 2 Lyrical, ROS_DOMAIN_ID=28

1. How many subscribers, publishers and service servers does /turtlesim have?

I ran `ros2 node info /turtlesim` and counted: <N> subscribers, <N> publishers, and
<N> service servers. The one I care about most is the subscriber on /turtle1/cmd_vel,
because that's how the turtle receives its movement commands. A lot of the extra entries
(like the parameter services) are there because every ROS 2 node gets them by default.

2. At what rate does /turtle1/pose publish? Why does /turtle1/cmd_vel have no steady rate?

When I ran `ros2 topic hz /turtle1/pose`, the average rate was about <rate> Hz. It's steady
because turtlesim publishes the pose on its own timer, even if nobody is listening.
/turtle1/cmd_vel is different: a message only gets sent when someone presses a key or runs
a publisher, so the rate depends on whoever is sending, not on turtlesim.

3. Which two Twist values can a differential-drive robot use, and why not linear.y?

Only linear.x (go forward or backward) and angular.z (turn around). linear.y would mean
moving sideways, and a differential-drive robot can't do that because its wheels are on
one axle and can only roll in the direction they're facing. The other three values
(linear.z, angular.x, angular.y) don't matter on a flat floor.

4. What did turtlesim know about the echo subscriber, and what did it do when it left?

Basically nothing. Turtlesim just publishes messages and doesn't keep track of who is
listening. Keeping track of connections is handled by the middleware underneath, not by
turtlesim's own code. So when I pressed Ctrl+C on the echo node, turtlesim didn't have to
do anything and kept publishing like before.

5. Two things an action has that a service doesn't. What would you use for "navigate to the kitchen"?

An action gives you feedback while it's running, and it lets you cancel the goal halfway.
A service can't do either: it just blocks until it's finished. "Navigate to the kitchen"
takes a long time and I'd want to see the progress and maybe stop it, so I'd use an action.

6. Why did the edit work without rebuilding? What if it were a C++ ament_cmake package?

I built with `--symlink-install`, so the files in install/ are just links to my original
.py files. When I ran the node again, Python read the newest version of the file. A C++
package has to be compiled into a binary first, so I would need to run `colcon build`
again after every change.

7. Two reasons `ros2 run lab1_turtle circle_driver` says "No executable found"

-. I forgot to source the workspace in that new terminal. The fix is
   `source ~/mobile_robotics_ws/install/setup.bash`.
-. The entry point in setup.py is missing or wrong, or I didn't rebuild after editing it.
   The fix is to correct the `console_scripts` line, run
   `colcon build --symlink-install --packages-select lab1_turtle`, and source again.
