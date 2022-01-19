# Pytorch Yolov5 Operator

## Overview

The operator uses YOLOv5 to detect the target object in the image, and the yolov5 model is trained with COCO dataset.

- Input: the image path in str format.
- Output: a list with multiple PIL.Image.
- This Operator used the ultralytics/yolov5 model of Pytorch.
- Before creating the operator, please run `pip install -r requirements.txt`.

## How to use

This Operator can deploy in the yaml file of Pilple, for example:

```yaml
name: 'yolo_example'
operators:
    -
        name: '_start_op'
        function: '_start_op'
        init_args:
        inputs:
            -
                df: '_start_df'
                name: 'img_path'
                col: 0
        outputs:
            -
                df: 'img_file'
        iter_info:
            type: map
    -
        name: 'object_detection'
        function: 'towhee/pytorch_yolov5_coco'
        init_args:
            model_name: 'yolov5s'
        inputs:
            -
                df: 'img_file'
                name: 'img_path'
                col: 0
        outputs:
            -
                df: 'obj_list'
        iter_info:
            type: flatmap
    -
        name: '_end_op'
        function: '_end_op'
        init_args:
        inputs:
            -
                df: 'obj_list'
                name: 'obj_list'
                col: 0
        outputs:
            -
                df: '_end_df'
        iter_info:
            type: map
dataframes:
    -
        name: '_start_df'
        columns:
            -
                name: 'img_path'
                vtype: 'str'
    -
        name: 'img_file'
        columns:
            -
                name: 'img_path'
                vtype: 'str'
    -
        name: 'obj_list'
        columns:
            -
                name: 'obj_list'
                vtype: 'list'
    -
        name: '_end_df'
        columns:
            -
                name: 'obj_list'
                vtype: 'list'
```
