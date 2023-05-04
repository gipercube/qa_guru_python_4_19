import logging

import allure
import curlify
from allure import step
from allure_commons.types import AttachmentType
from requests import Session
from selene import browser


class BaseSession(Session):
    def __init__(self, **kwargs):
        self.base_url = kwargs.pop('base_url')
        super().__init__()

    def request(self, method, url, **kwargs):
        with step(f'{method} {url}'):
            response = super().request(method=method, url=f'{self.base_url}{url}', **kwargs)
            logging.info(curlify.to_curl(response.request))
            logging.info(response.url)
            logging.info(response.text)
            logging.info(response.status_code)
            allure.attach(f'{str(response.status_code)} {curlify.to_curl(response.request)}', 'curl_request',
                          AttachmentType.TEXT, '.log')
            allure.attach(response.text, 'response', AttachmentType.TEXT, '.log')
        return response
