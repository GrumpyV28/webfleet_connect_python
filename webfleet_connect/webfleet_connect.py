from .session import Session
from .credentials import Credentials
from .config import Config

def create(params = {}):
  credentials = Credentials(params)
  config = Config(params)
  session = Session(credentials, config)
  session.set_connection()
  return session