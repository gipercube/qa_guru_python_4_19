# Проект автотестов для https://reqres.in/

## Проект совмещает UI + API  тесты
* UI + API тесты
    * ✅ Регистрация пользователя
    * ✅ Авторизация пользователя
    * ✅ Ошибка авторизации - не введен пароль
    * ✅ Отображение ресурса
    * ✅ Отсутствие пользователя
* API тесты
    * ✅ Соответствие номера страницы запрашивамой 
    * ✅ Количество пользователей на странице
    * ✅ Валидация схемы ответа
    * ✅ Проверка доступности нескольких страниц (Параметризацованный тест)


## Применнные технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="resources/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="resources/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="resources/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="resources/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="resources/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="resources/logo/Github.png"></code>
  <code><img width="5%" title="Jenkins" src="resources/logo/Jenkins.png"></code>
  <code><img width="5%" title="selenoid" src="resources/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="resources/logo/allure.png"></code>
  <code><img width="5%" title="Telegram" src="resources/logo/tg.png"></code>
</p>




## Запуск тестов
### Локально
Склонировать проект. Через консоль в папке проекта выполнить команду:
```
pytest
```

### Удаленно
```bash
rm -rf allure-results/*
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest . --alluredir=allure-results
```

## <img width="6%" title="Jenkins" src="resources/logo/Jenkins.png"> Запуск тестов из [Jenkins](https://jenkins.autotests.cloud/job/qa_guru_python_4_25/)
Запуск тестов из Jenkins:
Добавить проект в Jenkins и нажать кнопку "Собрать сейчас".

<p><img src="resources/screenshots/chrome_wDkwqD6g8l.png" alt="Jenkins"/></p>

Нажать на иконку Allure возле завершившегося процесса для просмотра отчета

<p><img src="resources/screenshots/chrome_37wxhxSSAY.png" alt="Allure in Jenkins"/></p>


### <img width="6%" title="Allure" src="resources/logo/allure.png"> [Allure](https://jenkins.autotests.cloud/job/lastfm_graduate_work_qa_quru_ui/100/allure/)

#### Примеры отчетов

<img src="resources/screenshots/chrome_svRy4SokZf.png" alt="Allure"/>

<img src="resources/screenshots/chrome_0fD0R4DN59.png" alt="Allure"/>

### <img width="6%" title="Telegram" src="resources/logo/tg.png"> Telegram

#### Настроена отправка отчета в Telegram

<img src="resources/screenshots/Telegram_XIvtt3wAXC.png" alt="Telegram"/>

## Пример видео тестового прогона

В отчетах Allure для каждого UI-теста прикреплен не только скриншот, но и видео прохождения теста

<p align="center">
  <img title="Video" src="resources/video/4f561a214d4de655f056eee249f26c95.gif"/>
</p>