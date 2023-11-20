import requests
from services.requester import Requester


class DataUpdater:
    def __init__(self, base_url, prefix, headers=None):
        self.prefix = prefix
        self.requester = Requester(base_url + prefix)
        self.headers = headers or {}

    def post(self, data_list):
        try:
            for data in data_list:
                response = self.requester.make_request("POST", data=data)
                print("Status Code:", response.status_code)
                print("Resposta:", response)
                print("\n")
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")