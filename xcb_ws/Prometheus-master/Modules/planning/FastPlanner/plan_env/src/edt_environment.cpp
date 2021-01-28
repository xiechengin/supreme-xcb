#include <plan_env/edt_environment.h>

namespace dyn_planner
{
/* ============================== edt_environment ============================== */
void EDTEnvironment::init()
{
}

void EDTEnvironment::setMap(shared_ptr<SDFMap> map)
{
  EDTEnv_mode = LOCAL_MODE;
  this->sdf_map_ = map;
  resolution_inv_ = 1 / sdf_map_->getResolution();
  ROS_INFO("--- EDTEnvironment: set local sdf_map finished! ---");
}

void EDTEnvironment::setMap(shared_ptr<SDFMap_Global> map){

    EDTEnv_mode = GLOBAL_MODE;
    this->sdf_map_global = map;
    resolution_inv_ = 1 / sdf_map_global->getResolution();
    ROS_INFO("--- EDTEnvironment: set global sdf_map finished! ---");
}

void EDTEnvironment::evaluateEDTWithGrad(const Eigen::Vector3d& pos, const double& time, double& dist,
                                         Eigen::Vector3d& grad)
{
  if(EDTEnv_mode == LOCAL_MODE){
      vector<Eigen::Vector3d> pos_vec;
      Eigen::Vector3d diff;
      sdf_map_->getInterpolationData(pos, pos_vec, diff);

      /* ---------- value from surrounding position ---------- */
      double values[2][2][2];
      Eigen::Vector3d pt;
      for (int x = 0; x < 2; x++)
          for (int y = 0; y < 2; y++)
              for (int z = 0; z < 2; z++)
              {
                  pt = pos_vec[4 * x + 2 * y + z];
                  double d1 = sdf_map_->getDistance(pt);
                  values[x][y][z] = d1;
              }

      /* ---------- use trilinear interpolation ---------- */
      double v00 = (1 - diff(0)) * values[0][0][0] + diff(0) * values[1][0][0];
      double v01 = (1 - diff(0)) * values[0][0][1] + diff(0) * values[1][0][1];
      double v10 = (1 - diff(0)) * values[0][1][0] + diff(0) * values[1][1][0];
      double v11 = (1 - diff(0)) * values[0][1][1] + diff(0) * values[1][1][1];

      double v0 = (1 - diff(1)) * v00 + diff(1) * v10;
      double v1 = (1 - diff(1)) * v01 + diff(1) * v11;

      dist = (1 - diff(2)) * v0 + diff(2) * v1;

      grad[2] = (v1 - v0) * resolution_inv_;
      grad[1] = ((1 - diff[2]) * (v10 - v00) + diff[2] * (v11 - v01)) * resolution_inv_;
      grad[0] = (1 - diff[2]) * (1 - diff[1]) * (values[1][0][0] - values[0][0][0]);
      grad[0] += (1 - diff[2]) * diff[1] * (values[1][1][0] - values[0][1][0]);
      grad[0] += diff[2] * (1 - diff[1]) * (values[1][0][1] - values[0][0][1]);
      grad[0] += diff[2] * diff[1] * (values[1][1][1] - values[0][1][1]);

      grad[0] *= resolution_inv_;

  } else if(EDTEnv_mode == GLOBAL_MODE){
      sdf_map_global->evaluateEDTWithGrad(pos, dist, grad);

  } else{
      printf("mode error!\n");
      return;
  }
  }


double EDTEnvironment::evaluateCoarseEDT(const Eigen::Vector3d& pos, const double& time)
{
  if(EDTEnv_mode == 0){
      double d1 = sdf_map_->getDistance(pos);
      return d1;
  } else if(EDTEnv_mode == 1){
      double d1 = sdf_map_global->getDistance(pos);
      return d1;
  } else{
      printf("mode error!!\n");
      return -1.0;
  }

}

// jiangtao add
//bool EDTEnvironment::get_push_force(const Eigen::Matrix<double, 3, 1> current_odom, const double distance,
//        Eigen::Matrix<double, 3, 1> &push_force){
//
////    sdf_map_
////    vector<Eigen::Vector3d> pos_vec;
////    Eigen::Vector3d diff;
//    sdf_map_->get_arround_force(current_odom, distance, push_force);
//    return true;
//
//}

// EDTEnvironment::
}  // namespace dyn_planner