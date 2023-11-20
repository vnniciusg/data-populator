import os

from dotenv import load_dotenv

from services.json_loader import JsonLoader
from services.data_updater import DataUpdater

load_dotenv()


class Main:
    def __init__(self, dir_data, base_url):
        self.dir_data = dir_data
        self.base_url = base_url

    def run(self):
        json_data = JsonLoader(self.dir_data)
        data_list = json_data.load_json_data()

        for data in data_list:
            prefix = data["prefix"]
            data_updater = DataUpdater(self.base_url, prefix)
            data_updater.post([data])


if __name__ == "__main__":
    dir_data = os.getenv("DIR_DATA")
    base_url = os.getenv("BASE_URL")

    main = Main(dir_data, base_url)
    main.run()
