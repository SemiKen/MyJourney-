import os

class Path:
    def __init__(self, path: str):
        self.set_path(path)

    def set_path(self, path: str):
        """เปลี่ยน path ปัจจุบัน"""
        self.raw_path = path.strip()
        self.path = os.path.normpath(self.raw_path)
        self.basename = os.path.basename(self.path)
        self.name, self.ext = os.path.splitext(self.basename)
        return self

    def get_name(self):
        """ชื่อไฟล์แบบไม่มีนามสกุล"""
        return self.name

    def get_extension(self):
        """ดึงนามสกุลแบบไม่มีจุด (เช่น json ไม่ใช่ .json)"""
        return self.ext.lstrip(".")

    def get_full_name(self):
        """ชื่อเต็มของไฟล์ รวม .ext"""
        return self.basename

    def is_file(self):
        return os.path.isfile(self.path)

    def is_dir(self):
        return os.path.isdir(self.path)

    def get_children(self, full_path=True, include_hidden=False, path=None):
        """ดึงรายชื่อไฟล์หรือโฟลเดอร์ย่อย (ภายใน path นี้)"""
        target_path = path if path else self.path
        if not os.path.isdir(target_path):
            return []

        entries = os.listdir(target_path)
        if not include_hidden:
            entries = [e for e in entries if not e.startswith(".")]

        if full_path:
            return [os.path.join(self.path, e) for e in entries]
        else:
            return entries

    def search_folders(self, extension):
        """ค้นหาไฟล์ตาม extension"""
        if not self.is_dir():
            return []

        entries = self.get_children(full_path=True)
        return [e for e in entries if e.endswith(extension)]
    
    def is_json(self):
        return self.get_extension().lower() == "json"

    def as_dict(self):
        return {
            "raw_path": self.raw_path,
            "normalized": self.path,
            "name": self.get_name(),
            "ext": self.get_extension(),
            "full_name": self.get_full_name(),
            "is_file": self.is_file(),
            "is_dir": self.is_dir(),
            "is_json": self.is_json()
        }

    def __repr__(self):
        return f"<Path name='{self.name}' ext='{self.get_extension()}' dir={self.is_dir()}>"
