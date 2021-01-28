/*
By downloading, copying, installing or using the software you agree to this license.
If you do not agree to this license, do not download, install,
copy or use the software.


                          License Agreement
               For Open Source Computer Vision Library
                       (3-clause BSD License)

Copyright (C) 2000-2015, Intel Corporation, all rights reserved.
Copyright (C) 2009-2011, Willow Garage Inc., all rights reserved.
Copyright (C) 2009-2015, NVIDIA Corporation, all rights reserved.
Copyright (C) 2010-2013, Advanced Micro Devices, Inc., all rights reserved.
Copyright (C) 2015, OpenCV Foundation, all rights reserved.
Copyright (C) 2015, Itseez Inc., all rights reserved.
Third party copyrights are property of their respective owners.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

  * Redistributions of source code must retain the above copyright notice,
    this list of conditions and the following disclaimer.

  * Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.

  * Neither the names of the copyright holders nor the names of the contributors
    may be used to endorse or promote products derived from this software
    without specific prior written permission.

This software is provided by the copyright holders and contributors "as is" and
any express or implied warranties, including, but not limited to, the implied
warranties of merchantability and fitness for a particular purpose are disclaimed.
In no event shall copyright holders or contributors be liable for any direct,
indirect, incidental, special, exemplary, or consequential damages
(including, but not limited to, procurement of substitute goods or services;
loss of use, data, or profits; or business interruption) however caused
and on any theory of liability, whether in contract, strict liability,
or tort (including negligence or otherwise) arising in any way out of
the use of this software, even if advised of the possibility of such damage.
*/
#include "opencv2/face/predict_collector.hpp"

namespace cv {namespace face {

static std::pair<int, double> toPair(const StandardCollector::PredictResult & val) {
    return std::make_pair(val.label, val.distance);
}

static bool pairLess(const std::pair<int, double> & lhs, const std::pair<int, double> & rhs) {
    return lhs.second < rhs.second;
}

//===================================

StandardCollector::StandardCollector(double threshold_) : threshold(threshold_) {
    init(0);
}

void StandardCollector::init(size_t size) {
    minRes = PredictResult();
    data.clear();
    data.reserve(size);
}

bool StandardCollector::collect(int label, double dist) {
    if (dist < threshold)
    {
        PredictResult res(label, dist);
        if (res.distance < minRes.distance)
            minRes = res;
        data.push_back(res);
    }
    return true;
}

int StandardCollector::getMinLabel() const {
    return minRes.label;
}

double StandardCollector::getMinDist() const {
    return minRes.distance;
}

std::vector< std::pair<int, double> > StandardCollector::getResults(bool sorted) const {
    std::vector< std::pair<int, double> > res(data.size());
    std::transform(data.begin(), data.end(), res.begin(), &toPair);
    if (sorted)
    {
        std::sort(res.begin(), res.end(), &pairLess);
    }
    return res;
}

std::map<int, double> StandardCollector::getResultsMap() const {
    std::map<int, double> res;
    for (std::vector<PredictResult>::const_iterator i = data.begin(); i != data.end(); ++i) {
        std::map<int, double>::iterator j = res.find(i->label);
        if (j == res.end()) {
            res.insert(toPair(*i));
        } else if (i->distance < j->second) {
            j->second = i->distance;
        }
    }
    return res;
}

Ptr<StandardCollector> StandardCollector::create(double threshold) {
    return makePtr<StandardCollector>(threshold);
}

}} // cv::face::
