#include <ros/ros.h>
#include <actionlib/server/simple_action_server.h>
#include <hector_quadrotor_msgs/executerAction.h>
#include <geometry_msgs/Pose.h>
#include <geometry_msgs/PoseStamped.h>
#include <geometry_msgs/Twist.h>
#include <gazebo_msgs/GetModelState.h>
#include <gazebo_msgs/SetModelState.h>
#include <geometry_msgs/Twist.h>
#include <sstream>
#include <string>
#include <std_msgs/String.h>
#include <iostream>
#include <tf/LinearMath/Quaternion.h>
#include <stdio.h> 
#include <math.h>

class executerAction
{
protected:

  ros::NodeHandle nh_;
  ros::NodeHandle nh;
  // NodeHandle instance must be created before this line. Otherwise strange error may occur.
  actionlib::SimpleActionServer<hector_quadrotor_msgs::executerAction> action_; 
  std::string action_name_;
  // create messages that are used to published feedback/result
  hector_quadrotor_msgs::executerFeedback feedback_;
  hector_quadrotor_msgs::executerResult result_;
  ros::ServiceClient gms_c;  
  gazebo_msgs::SetModelState setmodelstate;
  gazebo_msgs::GetModelState getmodelstate; 
  ros::Publisher publisher;
  ros::ServiceClient smsl;

public:

  executerAction(std::string name) :
    action_(nh_, name, boost::bind(&executerAction::executeCB, this, _1), false),
    action_name_(name)
  {
    action_.start();
    ROS_INFO("Waiting for the Client to start the process");
  }
  
  ~executerAction(void)
  {
  }
  
  void executeCB(const hector_quadrotor_msgs::executerGoalConstPtr &goal)
  {
    ROS_INFO("Client is registered, lets start the executing");
    publisher = nh.advertise<geometry_msgs::Twist>("cmd_vel", 1);
    gms_c = nh_.serviceClient<gazebo_msgs::GetModelState>("/gazebo/get_model_state");
    // smsl = m.serviceClient<gazebo_msgs::SetModelState>("/gazebo/set_model_state");
    getmodelstate.request.model_name="quadrotor";


    geometry_msgs::Twist tw;
    publisher.publish(tw);
    ros::Duration(5.0).sleep();
    
    gms_c.call(getmodelstate);
    double now_x =  getmodelstate.response.pose.position.x;
    double now_y =  getmodelstate.response.pose.position.y;
    double now_z =  getmodelstate.response.pose.position.z;
    
    // geometry_msgs::PoseStamped msg;
    // msg.header.frame_id = "/world";
    // msg.header.stamp = ros::Time::now();
    double new_x = goal->goal.pose.position.x;
    double new_y = goal->goal.pose.position.y;
    double new_z = goal->goal.pose.position.z;

    double x_diff, y_diff, z_diff;
    double tmp_x, tmp_y, tmp_z;
    double var_x, var_y, var_z;

    ros::Rate r(1);
    bool success = true;
    
    // publish info to the console for the user
    
    ROS_INFO("%s: Executing!", action_name_.c_str());
    
    
    if (action_.isPreemptRequested() || !ros::ok())
      {
	ROS_INFO("%s: Preempted", action_name_.c_str());
	// set the action state to preempted
	action_.setPreempted();
	success = false;
	//break;
      }
    
    publisher.publish(tw);
    ros::Duration(2.0).sleep();
       
    
    x_diff=new_x - now_x;
    y_diff=new_y - now_y; 
    z_diff=new_z - now_z;

    // if(now_z < 0)
    //   {
    // 	now_z=now_z*(-1);
    //   z_diff=new_z - now_z;
    //   z_diff=z_diff*(-1);
    //   }else
    //   z_diff = new_z - now_z;
    
    
    // tmp_x= modf(new_x, &var_x);
    // tmp_y= modf(new_y, &var_y);
    // tmp_z= modf(new_z, &var_z);
    
    ROS_INFO(" Come Up Hector! ");
   
    if(now_z < 0.5)
      {
	tw.linear.z = 0.6;
      }
    else
      {
	tw.linear.z = 0.0;
      }
    
    publisher.publish(tw);
    ros::Duration(2.0).sleep();
    // tw.angular.z = -0.5;
    tw.linear.z = 0;
    tw.linear.x = 0;
    tw.linear.y = 0;

    // publisher.publish(tw);
    // ros::Duration(2.0).sleep();
    // tw.angular.z = 0;
    publisher.publish(tw);
    ros::Duration(2.0).sleep();	
    ROS_INFO(" Good Boy, let's go further! ");
  
    while( x_diff < -0.3 || x_diff > 0.3 || y_diff < -0.3 || y_diff > 0.3)
      {
	if(now_x < var_x || now_y < var_y)
	  {
	    
	    tw.linear.x = x_diff * 0.1;
	    tw.linear.y = y_diff * 0.1;
	  }else 
	  if(now_x > var_x || now_y > var_y)
	    {	
	      tw.linear.x =x_diff * 0.1;
	      tw.linear.y =y_diff * 0.1;
	    }
	
	publisher.publish(tw);
	ros::Duration(2.0).sleep();
	gms_c.call(getmodelstate);
	now_y =  getmodelstate.response.pose.position.y;
	y_diff=new_y - now_y;
	now_x =  getmodelstate.response.pose.position.x;
	x_diff=new_x - now_x;
      }
    
	ros::Duration(2.0).sleep();
	tw.linear.z = 0;
	tw.linear.x = 0;
	tw.linear.y = 0;
       	// tw.angular.z = -0.5;	
	publisher.publish(tw);
	
	ros::Duration(5.0).sleep();
	// tw.angular.z = 0;
	// publisher.publish(tw);
	
	// ros::Duration(5.0).sleep();
	// publisher.publish(tw);
  // 	ros::Duration(2.0).sleep();
  // 	gms_c.call(getmodelstate);
  // 	now_y =  getmodelstate.response.pose.position.y;
  // 	y_diff=new_y - now_y;
  // 	now_x =  getmodelstate.response.pose.position.x;
  // 	x_diff=new_x - now_x;
  // }
	
	action_.publishFeedback(feedback_);
	// this sleep is not necessary, the sequence is computed at 1    }
	
	if(success)
	  {
	    result_.result = feedback_.feedback;
	    ROS_INFO("%s: Succeeded", action_name_.c_str());
	    // set the action state to succeeded
	    action_.setSucceeded(result_);
	  }}
};




int main(int argc, char** argv)
{
  ros::init(argc, argv, "executer");

  executerAction execute(ros::this_node::getName());
  ros::spin();

  return 0;
}
