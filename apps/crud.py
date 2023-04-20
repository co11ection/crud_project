import json

class FileMixin:
    def __init__(self, filename) -> None:
        self.filename = filename
    
    def write(self, data):
        with open(f"/home/tima/Desktop/projects_for_students/Course/db/{self.filename}", "w") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    
    def read(self):
        try:
            with open(f"/home/tima/Desktop/projects_for_students/Course/db/{self.filename}", "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return []
        
class CRUDmixin:
    def create(self, obj):
        data = self.read()
        data.append(obj.__dict__)
        self.write(data)
    
    def read_all(self):
        return self.read()
    
    def update(self, key, value, new_data):
        data = self.read()
        for obj in data:
            if obj[key] == value:
                obj[new_data["key"]] = new_data['value']
        self.write(data)


