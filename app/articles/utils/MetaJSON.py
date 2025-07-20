import json

class MetaJSONBase:
    def __init__(self, data: dict = "", file_path: str = None):
        self._data = data or {}
        self._path = None
        if file_path:
            file_path = file_path.strip()
            if file_path.endswith(".json"):
                self._path = file_path
                self.load(file_path)
            else:
                raise ValueError("File path must end with '.json'")

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    def to_dict(self):
        return self._data

    def save(self, path):
        with open(path, 'w') as f:
            json.dump(self._data, f, indent=4)

    def load(self, path):
        with open(path, 'r') as f:
            self._data = json.load(f)

    def get(self, key, default=None):
        return self._data.get(key, default)

    def set(self, key, value):
        self._data[key] = value

    def has(self, key):
        return key in self._data

    def add_to_list(self, key, value):
        if key not in self._data:
            self._data[key] = []
        self._data[key].append(value)

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __repr__(self):
        return f"<MetaJSON {self._data}>"
