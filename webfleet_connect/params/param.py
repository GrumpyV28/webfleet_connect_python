class Param():
  def __init__(self, value):
    self._value = value

  def __str__(self):
    return f'&{self._param_name()}={self._value}'
  
  def _param_name(self):
    return self._pascal_to_snake(self.__class__.__name__)
  
  def _pascal_to_snake(text):
    result = [text[0].lower()]
    for char in text[1:]:
      if char.isupper():
        result.extend(['_', char.lower()])
      else:
        result.append(char)
    return ''.join(result)
