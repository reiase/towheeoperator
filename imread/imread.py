# encoding=utf-8
from collections import namedtuple
from typing import Any
import cv2
import numpy
from towhee.operator.base import Operator, SharedType

class Imread(Operator):
    def __init__(self, input):
        self._input = input
        self._cap = cv2.VideoCapture(self._input)

    def __call__(self, im: int):
        while True:
            retval, im = self._cap.read()
            if retval:
                return namedtuple('Outputs', [('im')])(im)

    @property
    def shared_type(self):
        return SharedType.Shareable
