import csv
import hashlib

class CsvResponseParser():
  def to_hash(self, response):
    csv_reader = csv.DictReader(response.text.splitlines())
    data_list = list(csv_reader)
    return hashlib.sha256(str(data_list).encode())
