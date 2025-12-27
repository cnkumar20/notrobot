class Alert:
    def __init__(self, message, level):
        self.message = message
        self.level = level

    def display(self):
        print(f"[{self.level}] {self.message}")
