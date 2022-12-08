import json
import os

class FileManger():
    def __init__(self, type="json"):
        self.type = type

    def save_in(self, data, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if self.type == "json":
            data_json = json.dumps(data)
            with open(path, mode='w') as f:
                f.write(data_json)

        elif self.type == "proto":
            print("Not implemented yet.")

    def load_from(self, path):
        if self.type == "json":
            with open(path, mode='r') as f:
                data_json = f.read()
                return json.loads(data_json)

        elif self.type == "proto":
            print("Not implemented yet.")
            return ""

if __name__ == '__main__':
    example = {"key1":"value1", "key2":"value2"}
    json_manager = FileManger()
    file_path = "testpath/test.json"
    json_manager.save_in(example, file_path)
    data = json_manager.load_from(file_path)
    print(data["key1"])
