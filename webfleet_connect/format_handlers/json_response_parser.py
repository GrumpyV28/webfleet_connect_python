class JsonResponseParser():
  def to_hash(self, response):
    return response.json()
