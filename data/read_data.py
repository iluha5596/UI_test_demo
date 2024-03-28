import json


class ReadData:

    def __init__(self, fail_path):
        self.file_path = fail_path
        self.file_data = self.read_data()

    def read_data(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            return json.load(file)


class LoginPageData(ReadData):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.logins = self.file_data['logins']
        self.passwords = self.file_data['passwords']

