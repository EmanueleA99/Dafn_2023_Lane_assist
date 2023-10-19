How to launch demo: 

launch file
type on terminal1 : ros2 launch my_opencv_demo lane_sub.launch.py

enable service
type on terminal2 : ros2 service call /car1/lane_sub/enable std_srvs/srv/SetBool "{data: true}"

launch ros2 image publisher
type on terminal2 : ros2 run cv_basics img_publisher


Lancio degli aruco detector: 

 
Terminale 1 lanciare: “ros2 launch ros2_examples_bringup image_processing_pipeline.launch.py” 

Terminale 2 : “ros2 run rqt_image_view rqt_image_view &” apro visualizzatore 

Terminale 2 : eseguire “ros2 service call /image_processing_pipeline/usb_camera_driver/enable_camera std_srvs/srv/SetBool "{data: true}"” 

Terminale 3 eseguire : ros2 service call /image_processing_pipeline/aruco_detector/enable std_srvs/srv/SetBool "{data: True}" 


For launch node lane_sub in real world change in lane_sub.cpp on line 62:
topic -- "/car1/usb_camera_driver/camera/image_rect_color" for real Use
topic -- "video_frames" for demo with webcam_pub publisher
