import os


class Credentials:
    def __init__(self, params=None):
        params = self._default_params() if params is None else {**self._default_params(), **params}
        self.params = params

    def __str__(self):
        return f'{self.account()}&{self.username()}&{self.password()}&{self.apikey()}'

    def _default_params(self):
        return {
            'account': os.getenv('WEBFLEET_CONNECT_ACCOUNT'),
            'username': os.getenv('WEBFLEET_CONNECT_USERNAME'),
            'password': os.getenv('WEBFLEET_CONNECT_PASSWORD'),
            'apikey': os.getenv('WEBFLEET_CONNECT_APIKEY')
        }

    def account(self):
        return f'account={self.params["account"]}'
  
    def username(self):
        return f'username={self.params["username"]}'
  
    def password(self):
        return f'password={self.params["password"]}'
  
    def apikey(self):
        return f'apikey={self.params["apikey"]}'

# Usage
credentials = Credentials()
print(credentials.params)
