import json

class Data():
    @classmethod
    def save(cls, path, data):
        with open(path, "w") as file_handler:
            json_dict = json.dumps(data)
            file_handler.write(json_dict)
    
    @classmethod
    def load(cls, path):
        try:
            with open(path, "r") as file_handler:
                json_dict = file_handler.read()
                return json.loads(json_dict)
        except:
            return {}