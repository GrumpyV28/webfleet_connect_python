from .param import Param

class DefaultParam(Param):
  def __init__(self, key, value):
    self._key = key
    self._value = value

  def _param_name(self):
    return self._key
    