#include <uima/api.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <cmath>
#include <iostream>
#include <pcl/point_types.h>
#include <rs/types/all_types.h>
//RS
#include <rs/scene_cas.h>
#include <rs/utils/time.h>
#include <rs/DrawingAnnotator.h>

// OpenCV
#include <opencv2/opencv.hpp>

using namespace uima;


class DetectPolygons : public DrawingAnnotator
{
private:
  float test_param;
  cv::Mat images;
 
public:


  DetectPolygons(): DrawingAnnotator(__func__)
  {
  }

  TyErrorId initialize(AnnotatorContext &ctx)
  {
    outInfo("initialize");
    ctx.extractValue("test_param", test_param);
    return UIMA_ERR_NONE;
  }

  TyErrorId typeSystemInit(TypeSystem const &type_system)
  {
    outInfo("typeSystemInit");
    return UIMA_ERR_NONE;
  }

  TyErrorId destroy()
  {
    outInfo("destroy");
    return UIMA_ERR_NONE;
  }

  TyErrorId processWithLock(CAS &tcas, ResultSpecification const &res_spec)
  {

    outInfo("process start");
    rs::StopWatch clock;
    rs::SceneCas cas(tcas);
    pcl::PointCloud<pcl::PointXYZRGBA>::Ptr cloud_ptr(new pcl::PointCloud<pcl::PointXYZRGBA>);
    //cv::Mat image;
    cv::VideoCapture cap;
    //cap.set(CV_CAP_PROP_FRAME_WIDTH, 640);
    //cap.set(CV_CAP_PROP_FRAME_HEIGHT, 480); 

    //cap.read(images);
    //images = cv::imread("_happy_fish.png",1);
    //images = cv::Mat(300, 500, CV_8UC3);
    outInfo("Test param =  " << test_param);
    //  cv::imshow("ja", image);
    // cas.get(VIEW_COLOR_IMAGE_HD, images);
    //cas.get(VIEW_CLOUD, *cloud_ptr);
    // drawImageWithLock(image);
    outInfo("Cloud size: " << cloud_ptr->points.size());
    outInfo("took: " << clock.getTime() << " ms.");
    
    return UIMA_ERR_NONE;
   
  }
 void drawImageWithLock(cv::Mat &disp)
  {
    if (!images.empty()) {
    disp = images.clone();
    }
    cv::waitKey(33);
  }

  // void drawImageWithLock(cv::Mat &disp)
  // {
    // cv::Mat gray;
    //if (!images.empty()) {
      //	cv::cvtColor( images, gray,CV_BGR2GRAY );
	//	cv::namedWindow( "ja", 0 );
	//cv::namedWindow( "hm", 0 );
	
	//cv::resizeWindow("ja", 500,500);
        //cv::imshow("ja", src);
	//cv::resizeWindow("hm", 500,500);
	//cv::imshow("hm", dst);
	
    //  disp = images.clone();			
    //  cv::imshow("hello", images);
	
    //  }
    //cv::waitKey(33);
  //  }
};

// This macro exports an entry point that is used to create the annotator.
MAKE_AE(DetectPolygons)
