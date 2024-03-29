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
        self.logins_non_pass = self.file_data['logins_non_pass']
        self.passwords_non_pass = self.file_data['passwords_non_pass']
        self.login_valid = self.file_data['login_valid']
        self.password_valid = self.file_data['password_valid']

