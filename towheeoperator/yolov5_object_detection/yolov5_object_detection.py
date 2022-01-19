# Copyright 2021 Zilliz. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import torch
import cv2
import numpy
from PIL import Image
from typing import NamedTuple
from towhee.operator import Operator


class Yolov5ObjectDetection(Operator):
    """
    Use YOLOv5 model with PyTorch to extract the object of the image and return to the list.

    Args:
        model_name (`str`):
            The name of the model, usually is "yolov5s".
    """

    def __init__(self, model_name) -> None:
        super().__init__()
        self._model = torch.hub.load("ultralytics/yolov5",
                                     model_name,
                                     pretrained=True)

    def __call__(
            self, im: numpy.ndarray
    ) -> NamedTuple("Outputs", [("obj", Image.Image)]):
        """
        Call it when use this class.

        Args:
            img_path (`str`):
                The path of the image to be detected.

        Returns:
            (`Tuple[list([PIL.Image])]`)
                A tuple with one values, which is a list of objects detected in the image.
        """
        # Get object detection results with YOLOv5 model
        results = self._model(im)
        self.bboxes = results.xyxy[0].tolist()

        for bbox in self.bboxes:
            cv2.rectangle(im, (int(bbox[1]), int(bbox[3])),
                          (int(bbox[0]), int(bbox[2])), (255, 0, 0), 2)

        # Get the detected object list([PIL.Image])
        Outputs = NamedTuple("Outputs", [("im", Image.Image)])
        return Outputs(im)

    def get_obj_imgs(self):
        obj_list = []
        img = cv2.imread(self.img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Convert image from openCV format to PIL.Image
        for bbox in self.bboxes:
            tmp_obj = img[int(bbox[1]):int(bbox[3]), int(bbox[0]):int(bbox[2])]
            pil_img = Image.fromarray(cv2.cvtColor(tmp_obj, cv2.COLOR_BGR2RGB))
            obj_list.append(pil_img)
        return obj_list
