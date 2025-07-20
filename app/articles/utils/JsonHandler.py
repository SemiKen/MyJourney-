import os
import json

class Json:
    def __init__(self, path):
        self.path = path
        os.makedirs(self.path, exist_ok=True)  # ✅ สร้าง path ถ้ายังไม่มี

    def _load(self, filename):
        filepath = os.path.join(self.path, f"{filename}.json")
        if not os.path.exists(filepath):
            return None
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self, filename, data):
        filepath = os.path.join(self.path, f"{filename}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def to_dict(self, filename):
        return self._load(filename) or {}

    def to_json(self, filename):
        data = self.load(filename)
        return json.dumps(data, indent=2, ensure_ascii=False) if data else "{}"

    def get_all(self, extension=False):
        if extension:
            global files
            files = [
                f[:-5] for f in os.listdir(self.path)
                if f.endswith(".json")
            ]
        else:
            files = os.listdir(self.path)

        return files

    def create(self, filename, default_data=None):
        """สร้าง JSON ไฟล์ใหม่ถ้าไม่มีอยู่"""
        if default_data is None:
            default_data = {}
        filepath = os.path.join(self.path, f"{filename}.json")
        if not os.path.exists(filepath):
            self.save(filename, default_data)
            return default_data
        else:
            return self._load(filename)
