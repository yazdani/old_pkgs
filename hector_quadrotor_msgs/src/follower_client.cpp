#include <ros/ros.h>
#include <actionlib/client/simple_action_client.h>
#include <actionlib/client/terminal_state.h>
#include <hector_quadrotor_msgs/followerAction.h>
#include <geometry_msgs/Twist.h>
#include <geometry_msgs/Pose.h>

int main (int argc, char **argv)
{
  ros::init(argc, argv, "action_client");
  
  // create the action client
  // true causes the client to spin its own thread
  actionlib::SimpleActionClient<hector_quadrotor_msgs::followerAction> ac("follower", true);
  geometry_msgs::Twist twist;
  ROS_INFO("Waiting for action server to start.");
  // wait for the action server to start
  ac.waitForServer(); //will wait for infinite time

  ROS_INFO("Action server started, sending goal.");
  // send a goal to the action
 hector_quadrotor_msgs::followerGoal goal;
 goal.goal.position.x = 5.5;
 goal.goal.position.y = 10;
  goal.goal.position.z = 0.499;
  ac.sendGoal(goal);

  //wait for the action to return
  bool finished_before_timeout = ac.waitForResult(ros::Duration(30.0));

  if (finished_before_timeout)
  {
    actionlib::SimpleClientGoalState state = ac.getState();
    ROS_INFO("Action finished: %s",state.toString().c_str());
  }
  else
    ROS_INFO("Action did not finish before the time out.");

  //exit
  return 0;
}
