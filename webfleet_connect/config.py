class Config:
  HOST = 'csv.webfleet.com'
  PATH = 'extern'

  def __init__(self, params = {}):
    merged = self._default_params() | params
    self._lang = merged['lang']
    self._format = merged['format']
    self._useUTF8 = merged['useUTF8']
    self._useISO8601 = merged['useISO8601']

  def __str__(self):
    return f'{self._base_url()}?{self.lang()}&{self.format()}' \
      f'&{self.useUTF8()}&{self.useISO8601()}'
  
  def has_json(self):
    return self._format == 'json'

  def _base_url(self):
    return f'https://{Config.HOST}/{Config.PATH}'

  def _default_params(self):
    return {
      'lang': 'en',
      'format': 'json',
      'useUTF8': False,
      'useISO8601': False
    }

  def lang(self):
    return f'lang={self._lang}'
  
  def format(self):
    return f'outputformat={self._format}'
  
  def useUTF8(self):
    return f'useUTF8={self._useUTF8}'
  
  def useISO8601(self):
    return f'useISO8601={self._useISO8601}'
