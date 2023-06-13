import allure
import pytest
from allure_commons.types import Severity
from pytest_voluptuous import S
from requests import Response
from allure import step
from schemas.reqres import list_users_schema

@allure.tag("api")
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'gipercube')
@allure.feature('API')
@allure.title('Соответствие номера страницы запрашивамой')
def test_get_users_page_number(reqres_api):
    """Когда запросили вторую страницу, убеждаемся что вернулась вторая страница."""
    # WHEN
    with step("USER PAGE NUMBER REQUEST (API)"):
        response: Response = reqres_api.get(
            url='/api/users?page=2'
        )
    # THEN
    with step("USER PAGE NUMBER = 2 (API)"):
        assert response.status_code == 200
        assert response.json()["page"] == 2


@allure.tag("api")
@allure.severity(Severity.TRIVIAL)
@allure.label('owner', 'gipercube')
@allure.feature('API')
@allure.title('Количество пользователей на странице')
def test_get_users_users_on_page(reqres_api):
    """Проверяем дефолтное количество пользователей на странице и что вернулось столько же пользователей."""
    # WHEN
    with step("USER ON PAGE REQUEST (API)"):
        response: Response = reqres_api.get(
            url='/api/users?page=2'
        )
    per_page = response.json()["per_page"]
    data_len = len(response.json()["data"])

    # THEN
    with step("USERS COUNT ON PAGE (API)"):
        assert data_len == per_page == 6


@allure.tag("api")
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'gipercube')
@allure.feature('API')
@allure.title('Валидация схемы ответа')
def test_get_users_validate_schema(reqres_api):
    """Валидируем схему ответа."""
    with step("USERS SCHEMA REQUEST (API)"):
        response: Response = reqres_api.get(
            url='/api/users'
        )
    # THEN
    with step("VALIDATE SCHEMA (API)"):
        assert S(list_users_schema) == response.json()


@allure.tag("api")
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'gipercube')
@allure.feature('API')
@allure.title('Проверка доступности нескольких страниц')
@pytest.mark.parametrize("path_part", ["users", "cutomers", "products"])
def test_get_path_is_200(reqres_api, path_part):
    """Параметризацованный тест с множеством путей для проверки доступности каждой страницы."""
    with step("OPEN PAGE URL REQUEST (API)"):
        response: Response = reqres_api.get(
            url=f"/api/{path_part}"
        )
    # THEN
    with step("PAGE IS OPEN (API)"):
        assert response.status_code == 200
