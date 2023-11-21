import requests
from services.requester import Requester


class DataUpdater:
    def __init__(self, base_url, prefix):
        self.prefix = prefix
        self.requester = Requester(base_url + prefix)

    def post(self, data_list):
        try:
            for data in data_list:
                response = self.requester.make_request("POST", data=data)
                print("Resposta:", response)
                print("\n")
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
