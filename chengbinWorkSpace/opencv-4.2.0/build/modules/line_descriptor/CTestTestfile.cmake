# CMake generated Testfile for 
# Source directory: /home/xcb/shuikeWorkSpace/opencv_contrib-4.2.0/modules/line_descriptor
# Build directory: /home/xcb/shuikeWorkSpace/opencv-4.2.0/build/modules/line_descriptor
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_line_descriptor "/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/bin/opencv_test_line_descriptor" "--gtest_output=xml:opencv_test_line_descriptor.xml")
set_tests_properties(opencv_test_line_descriptor PROPERTIES  LABELS "Extra;opencv_line_descriptor;Accuracy" WORKING_DIRECTORY "/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/test-reports/accuracy")
add_test(opencv_perf_line_descriptor "/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/bin/opencv_perf_line_descriptor" "--gtest_output=xml:opencv_perf_line_descriptor.xml")
set_tests_properties(opencv_perf_line_descriptor PROPERTIES  LABELS "Extra;opencv_line_descriptor;Performance" WORKING_DIRECTORY "/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/test-reports/performance")
add_test(opencv_sanity_line_descriptor "/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/bin/opencv_perf_line_descriptor" "--gtest_output=xml:opencv_perf_line_descriptor.xml" "--perf_min_samples=1" "--perf_force_samples=1" "--perf_verify_sanity")
set_tests_properties(opencv_sanity_line_descriptor PROPERTIES  LABELS "Extra;opencv_line_descriptor;Sanity" WORKING_DIRECTORY "/home/xcb/shuikeWorkSpace/opencv-4.2.0/build/test-reports/sanity")
