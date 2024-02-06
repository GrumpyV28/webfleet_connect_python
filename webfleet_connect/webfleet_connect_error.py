from .format_handlers.json_response_parser import JsonResponseParser
from .format_handlers.csv_response_parser import CsvResponseParser

class WebfleetConnectError(Exception):
  SITE = 'https://www.webfleet.com'
  PATH = '/static/help/webfleet-connect/en_gb/index.html'

  def __init__(self, response, url, is_json):
    parser = self._build_parser(is_json)
    hash = parser.to_hash(response)
    self._code = hash['errorCode']
    self._message = hash['errorMsg']
    self._url = url

  def message(self):
    return f'{self._code}, {self._message}\n\n' \
      f'Check {self._api_docs_url()} for more details.\n\n'
  
  def code(self):
    return self._code
  
  def url(self):
    return self._url
  
  def _api_docs_url(self):
    return f'{WebfleetConnectError.SITE}{WebfleetConnectError.PATH}'

  def _build_parser(self, is_json):
    if is_json:
      return JsonResponseParser()
    return CsvResponseParser()
