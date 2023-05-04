
from selene.support.shared import browser
from allure import step
from selene import have

from conftest import LOGIN, PASSWORD
from utils import attach
from utils.helper import BaseSession


def test_login_through_api():
    """Successful authorization to some demowebshop (UI)"""
    # GIVEN
    with BaseSession(base_url="https://demowebshop.tricentis.com/") as session:
        response = session.post(
            url='login',
            params={'Email': LOGIN, 'Password': PASSWORD},
            headers={'content-type': "application/x-www-form-urlencoded; charset=UTF-8"},
            allow_redirects=False
        )
        authorization_cookie = response.cookies.get('NOPCOMMERCE.AUTH')
        session.cookies.set('NOPCOMMERCE.AUTH', authorization_cookie)
        browser.open("")
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": authorization_cookie})
    # WHEN
    with step("Go to main page (UI)"):
        browser.open('')
    # THEN
    with step("Verify successful authorization"):
        browser.element(".account").should(have.text(LOGIN))
        attach.add_screenshot(browser)


def test_add_book_in_cart(webshop):
    """Добавление товара КНИГА в карзину"""
    # GIVEN
    with step("Add book to cart (API)"):
        webshop.post(
            url='addproducttocart/catalog/45/1/1'
        )
    # WHEN
    with step("Go to cart (UI)"):
        browser.open('cart')
    # THEN
    with step("BOOK 'Fiction' is added to cart"):
        assert browser.element('.product-name').should(have.text("Fiction"))
