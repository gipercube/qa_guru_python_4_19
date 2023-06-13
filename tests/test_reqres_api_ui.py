import allure
from allure_commons.types import Severity
from requests import Response
from selene.support.shared import browser
from allure import step
from pages.main import single_resource, user_not_found, register_successful, login_successful, login_unsuccessful


@allure.tag("ui")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'gipercube')
@allure.feature('UI')
@allure.title('Пользователь не найден')
def test_single_user_not_found(reqres_ui):
    """Ответ в случае отсутствия запрашиваемого пользователя"""
    # GIVEN
    with step("SINGLE USER NOT FOUND (API)"):
        response = reqres_ui.get(
            url='/api/users/23'
        )
    # WHEN
    with step("Go to reqres.in (UI)"):
        browser.open('https://reqres.in/')
    # THEN
    user_not_found(response.status_code)


@allure.tag("ui")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'gipercube')
@allure.feature('UI')
@allure.title('Один ресурс')
def test_single_resourse_name(reqres):
    """Показан один ресурс"""
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

    # THEN
    single_resource(response_data, response_name)

@allure.tag("ui")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'gipercube')
@allure.feature('UI')
@allure.title('Успешная регистрация')
def test_login_successful(reqres):
    """Успешная регистрация пользователя с получением токена"""
    # GIVEN
    with step("REGISTER REQUEST (API)"):
        response: Response = reqres.post(
            url='/api/register',
            data={'email': 'eve.holt@reqres.in', 'password': 'pistol'}
        )
        response_token = str(response.json()['token'])
    # WHEN
    with step("Go to reqres.in (UI)"):
        browser.open('https://reqres.in')

    # THEN
    register_successful(response_token)


@allure.tag("ui")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'gipercube')
@allure.feature('UI')
@allure.title('Успешная авторизация')
def test_login_successful(reqres):
    """Успешная авторизация пользователя"""
    # GIVEN
    with step("LOGIN REQUEST (API)"):
        response: Response = reqres.post(
            url='/api/login',
            data={'email': 'eve.holt@reqres.in', 'password': 'cityslicka'}
        )
        response_token = str(response.json()['token'])
    # WHEN
    with step("Go to reqres.in (UI)"):
        browser.open('https://reqres.in')

    # THEN
    login_successful(response_token)


@allure.tag("ui")
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'gipercube')
@allure.feature('UI')
@allure.title('Ошибка авторизации при входе без пароля')
def test_login_unsuccessful(reqres):
    """Ошибка авторизации - не введен пароль"""
    # GIVEN
    with step("LOGIN REQUEST (API)"):
        response: Response = reqres.post(
            url='/api/login',
            data={'email': 'peter@klaven'}
        )
        response_error = str(response.json()['error'])
    # WHEN
    with step("Go to reqres.in (UI)"):
        browser.open('https://reqres.in')

    # THEN
    login_unsuccessful(response_error)

