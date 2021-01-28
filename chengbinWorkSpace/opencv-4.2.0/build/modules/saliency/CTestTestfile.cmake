# CMake generated Testfile for 
# Source directory: /home/xcb/shuikeWorkSpace/opencv_contrib-4.2.0/modules/saliency
# Build directory: /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/saliency
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_saliency "/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/bin/opencv_test_saliency" "--gtest_output=xml:opencv_test_saliency.xml")
set_tests_properties(opencv_test_saliency PROPERTIES  LABELS "Extra;opencv_saliency;Accuracy" WORKING_DIRECTORY "/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/test-reports/accuracy")
