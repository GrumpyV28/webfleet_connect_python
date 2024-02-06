import requests
from .webfleet_connect_error import WebfleetConnectError
from .webfleet_connect_response import WebfleetConnectResponse
from .format_handlers.csv_error_parser import CsvErrorParser
from .format_handlers.json_error_parser import JsonErrorParser

class Connection:
  def __init__(self, session):
    self._session = session
    self._error_parser = self._build_error_parser(session)

  def exec(self, url):
    response = requests.get(url)
    is_json = self._session.has_json()
    if self._is_error_found(response):
      raise WebfleetConnectError(response, url, is_json)
    return WebfleetConnectResponse(response, url, is_json)
  
  def _is_error_found(self, response):
    return self._error_parser.is_error_found(response)

  def _build_error_parser(self, session):
    if session.has_json():
      return JsonErrorParser()
    return CsvErrorParser()