from requests import Response
from selene.core import query
from selene.support.shared import browser
from allure import step
from selene import have

from utils.tools import data_len


def test_single_user_not_found(reqres):
    """SINGLE USER NOT FOUND"""
    # GIVEN
    with step("SINGLE USER NOT FOUND (API)"):
        response = reqres.get(
            url='/api/users/23'
        )
    # WHEN
    with step("Go to reqres.in (UI)"):
        browser.open('https://reqres.in/')
        browser.element("[href='/api/users/23']").click()
    # THEN
    with step("Status code is 404"):
        assert browser.element('[data-key="response-code"]').should(have.text("404"))
        assert browser.element('[data-key="response-code"]').get(query.text) == str(response.status_code)


def test_single_resourse_name(reqres):
    """SINGLE <RESOURCE>"""
    # GIVEN
    with step("SINGLE <RESOURCE> (API)"):
        response: Response = reqres.get(
            url='/api/unknown/2'
        )
        response_data = response.json()
        response_name = str(response.json()['data']['name'])
    # WHEN
    with step("Go to reqres.in (UI)"):
        browser.open('https://reqres.in')
        browser.element("[href='/api/unknown/2']").click()
    # THEN
    with step("SINGLE <RESOURCE> click"):
        assert data_len(response_data) == 1
        assert browser.element('[data-key="output-response"]').should(have.text(response_name))
