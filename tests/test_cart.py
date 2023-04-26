import allure
from allure_commons.types import AttachmentType
from selene.support.shared import browser
from allure import step
from selene import have

from conftest import LOGIN, webshop, API_URL, PASSWORD, WEB_URL


def test_login_through_api(login):
    """Successful authorization to some demowebshop (UI)"""

    with step("Verify successful authorization"):
        browser.element(".account").should(have.text(LOGIN))


def test_add_book_in_cart(login, webshop):
    """Добавление товара КНИГА в карзину"""
    # GIVEN
    with step("Add book to cart (API)"):
        webshop.post(
            url='addproducttocart/catalog/45/1/1'
        )
    # WHEN
    with step("Go to cart (UI)"):
        browser.open('/cart')
    # THEN
    with step("BOOK 'Fiction' is added to cart"):
        png = browser.driver.get_screenshot_as_png()
        allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')
        assert browser.element('.product-name').should(have.text("Fiction"))

