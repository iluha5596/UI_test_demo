class GenerateDictProduct:

    def __init__(self):
        self.data = {}
        self.current_key = 0

    def add_value_in_dict(self, value):
        self.current_key += 1
        self.data[self.current_key] = value
        return self.data
