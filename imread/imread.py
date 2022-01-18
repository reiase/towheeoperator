# encoding=utf-8
from collections import namedtuple
from typing import Any
import cv2
import numpy
from towhee.operator.base import Operator, SharedType

from hyperparameter import param_scope

class Imread(Operator):
    def __init__(self, input):
        self._input = input
        self._cap = cv2.VideoCapture(self._input)

        with param_scope() as hp:
            self._scale = hp().towheeoperator.imread.scale.getOrElse(1.0)
    def __call__(self, im: int):
        while True:
            retval, im = self._cap.read()
            if self._scale != 1.0:
                w = int(im.shape[1] * self._scale)
                h = int(im.shape[0] * self._scale)
                im = cv2.resize(im, (w, h))
            if retval:
                return namedtuple('Outputs', [('im')])(im)

    @property
    def shared_type(self):
        return SharedType.Shareable
