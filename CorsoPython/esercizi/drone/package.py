

class Package:
    def __init__(self, package_id, content, weight, value):
        self.id = package_id
        self.content = content
        self.weight = weight
        self.value = value

    def __repr__(self):
        return f"[{self.id}] {self.content} - €{self.value}"