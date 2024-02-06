from .csv_response_parser import CsvResponseParser

class CsvErrorParser():
  def is_error_found(self, response):
    json = self._parse(response)
    if isinstance(json, list):
      return False
    return json['errorCode']

  def _parse(self, response):
    return CsvResponseParser(response).to_hash()
