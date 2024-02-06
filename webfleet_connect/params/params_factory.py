from .defult_param import DefaultParam

class ParamsFactory():
  @classmethod
  def build_params(self, args):
    return [ParamsFactory._build(k, v) for k, v in args.items()]

  @classmethod
  def _build(self, key, value):
    return DefaultParam(key, value)
