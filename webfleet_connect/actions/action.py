from ..params.params_factory import ParamsFactory

class Action():
  def __init__(self, name, args):
    self._name = name
    self._params = ParamsFactory.build_params(args)

  def __str__(self):
    return f'action={self._name}{self.params()}'
  
  def params(self):
    stringified_list = map(str, self._params)
    return ''.join(stringified_list)
