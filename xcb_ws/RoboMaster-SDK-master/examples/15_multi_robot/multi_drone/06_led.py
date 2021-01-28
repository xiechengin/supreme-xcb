# -*-coding:utf-8-*-
# Copyright (c) 2020 DJI.
#
# Licensed under The 3-Clause BSD License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     https://opensource.org/licenses/BSD-3-Clause
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import time
from multi_robomaster import multi_robot


def base_action_1(robot_group):
    robot_group.set_led(255, 255, 255)
    time.sleep(2)
    robot_group.set_led(command_dict={1: [255, 0, 0], 2: [255, 255, 0]})


if __name__ == '__main__':
    # get drone sn by run the expamles of /15_multi_robot/multi_drone/01_scan_ip.py

    robot_sn_list = ["0TQZH79ED00H56", "0TQZH79ED00H89"]
    multi_drone = multi_robot.MultiDrone()
    multi_drone.initialize(robot_num=2)
    multi_drone.number_id_by_sn([1, robot_sn_list[0]], [2, robot_sn_list[1]])
    multi_drone_group1 = multi_drone.build_group([1, 2])
    multi_drone.run([multi_drone_group1, base_action_1])
    multi_drone.close()
