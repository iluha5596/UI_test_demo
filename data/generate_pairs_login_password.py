from data.read_data import LoginPageData
import pytest


def value_logins_passwords_non_pass():
    data_password_login = LoginPageData('data/login_page_data.json')
    logins_non_pass = [login_value for login_value in data_password_login.logins_non_pass.values()]
    passwords_non_pass = [password_value for password_value in data_password_login.passwords_non_pass.values()]

    return logins_non_pass, passwords_non_pass


def value_logins_non_valid():
    data_password_login = LoginPageData('data/login_page_data.json')
    logins_non_valid = [login_value for login_value in data_password_login.logins_non_valid.values()]

    return logins_non_valid


def value_login_password_pass():
    data_password_login = LoginPageData('data/login_page_data.json')
    login_valid = [login_value for login_value in data_password_login.login_valid.values()]
    password_valid = [password_value for password_value in data_password_login.password_valid.values()]

    return login_valid, password_valid


def generate_non_valid_pairs():
    logins_non_pass, passwords_non_pass = value_logins_passwords_non_pass()
    login_valid, password_valid = value_login_password_pass()
    logins = logins_non_pass + login_valid
    pairs_non_valid = []
    for login in logins:
        for password in passwords_non_pass:
            pairs_non_valid.append(pytest.param((login, password), id=f'{login}, {password}'))

    return pairs_non_valid


def generate_non_valid_email():
    logins = value_logins_non_valid()
    logins_non_valid = []
    for login in logins:
        logins_non_valid.append(pytest.param(login, id=f'{login}'))

    return logins_non_valid


def generate_valid_pairs():
    logins, passwords = value_login_password_pass()
    pairs_valid = [(pytest.param((logins[0], passwords[0]), id=f'{logins[0]}, {passwords[0]}'))]

    return pairs_valid
