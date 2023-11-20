import requests


class Requester:
    def __init__(self, base_url):
        self.base_url = base_url

    def make_request(self, method, data=None):
        headers = {"Content-Type": "application/json"}

        try:
            if method.upper() == "POST":
                response = requests.post(self.base_url, headers=headers, json=data)
            elif method.upper() == "PUT":
                response = requests.put(self.base_url, headers=headers, json=data)
            elif method.upper() == "DELETE":
                response = requests.delete(self.base_url, headers=headers, json=data)
            elif method.upper() == "GET":
                response = requests.get(self.base_url, headers=headers, json=data)
            else:
                raise Exception("Method not allowed")

            response.raise_for_status()
            return response.json()

        except Exception as e:
            print(e)
            return None
