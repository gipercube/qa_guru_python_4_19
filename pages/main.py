from selene import browser, have
from allure import step
from utils.tools import data_len
from selene.core import query


def single_resource(response_data, response_name):
    with step("SINGLE <RESOURCE> click"):
        browser.element("[href='/api/unknown/2']").click()
        assert data_len(response_data) == 1
        assert browser.element('[data-key="output-response"]').should(have.text(response_name))


def user_not_found(status_code):
    with step("User not found. Status code is 404"):
        browser.element("[href='/api/users/23']").click()
        assert browser.element('[data-key="response-code"]').should(have.text("404"))
        assert browser.element('[data-key="response-code"]').get(query.text) == str(status_code)


def register_successful(response_token):
    with step("Registration is successful"):
        browser.element("[href='/api/register']").click()
        assert browser.element('[data-key="response-code"]').should(have.text("200"))
        assert browser.element('[data-key="output-response"]').should(have.text(str(response_token)))


def login_successful(response_token):
    with step("Login is successful"):
        browser.element('[data-id="login-successful"] [href="/api/login"]').click()
        assert browser.element('[data-key="response-code"]').should(have.text("200"))
        assert browser.element('[data-key="output-response"]').should(have.text(str(response_token)))


def login_unsuccessful(response_error):
    with step("Login is successful"):
        browser.element("[data-id='login-unsuccessful'] [href='/api/login']").click()
        assert browser.element('[data-key="response-code"]').should(have.text("400"))
        assert browser.element('[data-key="output-response"]').should(have.text(str(response_error)))
