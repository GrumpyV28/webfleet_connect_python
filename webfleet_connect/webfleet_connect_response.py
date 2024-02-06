from .format_handlers.json_response_parser import JsonResponseParser
from .format_handlers.csv_response_parser import CsvResponseParser

class WebfleetConnectResponse():
  def __init__(self, response, url, is_json):
    self._response = response
    self._url = url
    self._parser = self._build_parser(is_json)

  def status_code(self):
    return self._response.status_code
  
  def to_hash(self):
    return self._parser.to_hash(self._response)
  
  def url(self):
    return self._url
  
  def __str__(self):
    return self._response.text

  def _build_parser(self, is_json):
    if is_json:
      return JsonResponseParser()
    return CsvResponseParser()
  
  def to_excel(self, filename='output.xlsx'):
        workbook = Workbook()
        sheet = workbook.active

        data = self._parser.to_hash(self._response)

        headers = list(data.keys())
        sheet.append(headers)
        row_data = [data[header] for header in headers]
        sheet.append(row_data)
        workbook.save(filename)
        
webfleet_response = WebfleetConnectResponse()
webfleet_response.to_excel('nom_du_fichier.xlsx')
