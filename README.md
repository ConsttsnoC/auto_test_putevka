
<!-- Заголовок -->
<h1 align="center">
  <br>
  Тестовое задание для Путёвка.ком.
  <br>
</h1>
<!-- Описание -->
<p align="center">
  <a href="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" target="_blank">
  </a>
</p>
<!-- Иконки -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12.3-green">
  <img src="https://img.shields.io/badge/Page Object Model-red">
</p>

## Описание

Этот проект представляет собой тестовое задание для компании Путёвка.ком. Тесты написаны на Python с использованием подхода Page Object Model (POM). Для логирования используется библиотека `loguru`, а для отчётности тестов используется `pytest-html`. Для форматирования кода использовался `black`. 

## Установка

## Предварительные требования

1. **Клонируйте репозиторий используя команду**
    ```
      git clone
    ```

2. **Убедитесь, что у вас установлен Python 3.12.3**

   Проверьте версию Python с помощью команды:
   ```bash
   python --version
    ```
3. **Создайте и активируйте виртуальное окружение**
   Создайте виртуальное окружение в текущей директории (замените myenv на желаемое имя вашего окружения)
    ```
      python -m venv myenv
    ```
    Активируйте виртуальное окружение:
    ```
    Для Windows: myenv\Scripts\activate

    Для macOS и Linux: source myenv/bin/activate
    ```
    После активации виртуального окружения вы увидите его имя в начале строки командной строки.

4. **Установите зависимости из requirements.txt**
    
    ```bash
    pip install -r requirements.txt
   ```
        


### Запуск тестов с Pytest
Для запуска тестов используйте команду: 
`pytest`

## Запуск тестов с генерацией отчёта HTML
`pytest --html=report.html     `

## Для просмотра отчета, нужно перейти ссылке после прохождения теста в консоли
`Generated html report: ссылка`