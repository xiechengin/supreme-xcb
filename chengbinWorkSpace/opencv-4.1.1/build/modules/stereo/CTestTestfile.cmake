# CMake generated Testfile for 
# Source directory: /home/xcb/shuikeWorkSpace/opencv_contrib-4.1.1/modules/stereo
# Build directory: /home/xcb/shuikeWorkSpace/opencv-4.1.1/build/modules/stereo
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(opencv_test_stereo "/home/xcb/shuikeWorkSpace/opencv-4.1.1/build/bin/opencv_test_stereo" "--gtest_output=xml:opencv_test_stereo.xml")
set_tests_properties(opencv_test_stereo PROPERTIES  LABELS "Extra;opencv_stereo;Accuracy" WORKING_DIRECTORY "/home/xcb/shuikeWorkSpace/opencv-4.1.1/build/test-reports/accuracy")
add_test(opencv_perf_stereo "/home/xcb/shuikeWorkSpace/opencv-4.1.1/build/bin/opencv_perf_stereo" "--gtest_output=xml:opencv_perf_stereo.xml")
set_tests_properties(opencv_perf_stereo PROPERTIES  LABELS "Extra;opencv_stereo;Performance" WORKING_DIRECTORY "/home/xcb/shuikeWorkSpace/opencv-4.1.1/build/test-reports/performance")
add_test(opencv_sanity_stereo "/home/xcb/shuikeWorkSpace/opencv-4.1.1/build/bin/opencv_perf_stereo" "--gtest_output=xml:opencv_perf_stereo.xml" "--perf_min_samples=1" "--perf_force_samples=1" "--perf_verify_sanity")
set_tests_properties(opencv_sanity_stereo PROPERTIES  LABELS "Extra;opencv_stereo;Sanity" WORKING_DIRECTORY "/home/xcb/shuikeWorkSpace/opencv-4.1.1/build/test-reports/sanity")
