# encoding=utf-8

from collections import namedtuple
import numpy

from towhee.operator.base import Operator, SharedType


class Imshow(Operator):
    def __init__(self):
        pass
    def __call__(self, im):
        return namedtuple('Outputs', [('im')])(im)

    @property
    def shared_type(self):
        return SharedType.Shareable
