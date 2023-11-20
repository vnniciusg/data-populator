import os
import json


class JsonLoader:
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def load_json_data(self):
        json_data = []

        for file in os.listdir(self.dir_path):
            if file.endswith(".json"):
                file_path = os.path.join(self.dir_path, file)

                with open(file_path, "r") as json_file:
                    file_data = json.load(json_file)

                    json_data.append(
                        {"prefix": os.path.splitext(file)[0], "data": file_data}
                    )

        return json_data
