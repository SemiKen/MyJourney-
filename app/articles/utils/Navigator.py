from flask import request

class Navigator:
    def __init__(self):
        self.siblings = []
        self.parent_sibling = []
        self.breadcrumb = []

    def set_siblings(self, siblings, prefix="task"):
        if siblings:
            self.siblings = siblings
        else:
            self.siblings = []

    def generate(self):
        segments = request.path.strip("/").split("/")
        self.breadcrumb = []
        accumulated = ""
        sibling_accumulated = ""
        current_sibling = ""


        # 🧱 สร้าง breadcrumb
        if not segments or segments == ['']:
            self.breadcrumb = [{"url": "/", "text": "Home"}]
        else:
            self.breadcrumb.append({"url": "/", "text": "Home"})
            index = 0
            for seg in segments:
                index += 1
                if index < len(segments):
                    sibling_accumulated += f"/{seg}"
                else:
                    current_sibling = seg
                accumulated += f"/{seg}"
                self.breadcrumb.append({
                    "url": accumulated,
                    "text": seg.replace("-", " ").capitalize()
                })

        # 🧩 สร้าง siblings
        sibling_links = []
        if self.siblings:
            for s in self.siblings:
                name = s.get("name") if isinstance(s, dict) else str(s)
                if name == current_sibling:
                    continue
                sibling_links.append({
                    "url": f"{sibling_accumulated}/{name}",
                    "text": f"{name}"
                })

        # 🎁 แยก breadcrumb กับ sibling ออกชัดเจน
        return {
            "breadcrumb": self.breadcrumb,
            "siblings": sibling_links
        }

    def get_breadcrumb(self):
        return self.breadcrumb

    def get_siblings(self):
        return self.siblings
