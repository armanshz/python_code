# Private classes can only be used within the same file or within a specific scope
class _Private:
    def __init__(self, name):
        self.name = self

# Public classes can be accessed by anyone
class notPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)

    def _display(self):
        print("Hello")

    def display(self):
        print("Hi")