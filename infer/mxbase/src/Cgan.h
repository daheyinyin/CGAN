
#ifndef CGAN_H
#define CGAN_H
#include <dirent.h>
#include <memory>
#include <vector>
#include <map>
#include <string>
#include <fstream>
#include <iostream>
#include <opencv2/opencv.hpp>
#include "MxBase/Log/Log.h"
#include "MxBase/DvppWrapper/DvppWrapper.h"
#include "MxBase/ModelInfer/ModelInferenceProcessor.h"
#include "MxBase/Tensor/TensorContext/TensorContext.h"
#include "MxBase/DeviceManager/DeviceManager.h"

struct InitParam {
    uint32_t deviceId;
    std::string savePath;
    std::string modelPath;
};

class Cgan {
 public:
        APP_ERROR Init(const InitParam &initParam);
        APP_ERROR DeInit();
        APP_ERROR CVMatToTensorBase(const cv::Mat &imageMat, MxBase::TensorBase *tensorBase);
        APP_ERROR Inference(const std::vector<MxBase::TensorBase> &inputs, std::vector<MxBase::TensorBase> *outputs);
        APP_ERROR PostProcess(std::vector<MxBase::TensorBase> outputs, cv::Mat *resultImg);
        APP_ERROR Process(const cv::Mat &imageMat, const cv::Mat &label, const std::string &imgName);
        // get infer time
        double GetInferCostMilliSec() const {return inferCostTimeMilliSec;}

 private:
        APP_ERROR SaveResult(const cv::Mat &resultImg, const std::string &imgName);
        std::shared_ptr<MxBase::ModelInferenceProcessor> model_;
        std::string savePath_;
        MxBase::ModelDesc modelDesc_;
        uint32_t deviceId_ = 0;
        // infer time
        double inferCostTimeMilliSec = 0.0;
};


#endif
