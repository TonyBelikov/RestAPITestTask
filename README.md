# RestAPITestTask

## Установка необходимого ПО

1) Python 3.9.10+
2) PyCharm или другая IDE
3) Java 8
4) Git

## Настройка проекта в PyCharm

1) Сделать директорию restapitesttask - корневой (ПКМ по директории - Mark Directory As - Root Source)
2) Добавить интерпретатор python (File - Settings - Project: restapitesttask - Project Interpreter - Add). `Python 3.9+. Venv path: restapitesttask\venv`.
3) В терминале активировать venv (cd restapitesttask/venv/Scripts; activate)
4) Выполнить установку всех зависимостей (pip install -r restapitesttask/requirements.txt)

Если все прошло успешно, то все библиотеки будут успешно установлены.

## Настройка Allure

Для запуска allure необходимо установить Java.

Затем создать переменную среды, где в качестве имени указать JAVA_HOME, а в 
значение передать путь до папки jdk включительно.

После потребуется установить scoop.

Для этого потребуется открыть PowerShell от имени администратора и запустить команду 
`Set-ExecutionPolicy RemoteSigned -scope CurrentUser`.

После выполнения команды потребуется выполнить следующую команду:
`Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')`.

Как закончится установка - потребуется перезапуск PowerShell.

Далее выполняем установку allure:
`scoop install allure`.

Перезапускаем PowerShell еще раз и выполняем команду `allure` для проверки успешной 
установки.

## Добавление переменных среды

Перейти в `Свойства системы - Переменные среды`. В список `Переменные среды пользователя` добавить следующие переменные:

1) JAVA_HOME
2) ALLURE_HOME

Добавление JAVA_HOME:
1) Имя: JAVA_HOME
2) Значение: `Путь до папки Java\JDK папка с указанной версией`. Пример: `C:\Program Files\Java\jdk1.8.0_271`

Добавление ALLURE_HOME
1) Имя: ALLURE_HOME
2) Значение: `Установочный диск\Users\<Текущий пользователь>\scoop\apps\allure\current`. Текущая переменная среды должна быть создана автоматически при установки allure.

## Запуск тестов 

Запуск всех тестов: `pytest Tests --alluredir results`

Запуск тестов по маркерам: `pytest -m 'marker_name' Tests --alluredir results`, где marker_name можно посмотреть 
в pytest.ini

Для запуска конкретного набора тестов: `pytest Tests/TestImageMetrics.py --alluredir results`

P.S.: `--alluredir results` запускает сбор информации для отчетов allure. `results` - наименование директории, где хранятся 
все allure-отчеты. Чтобы очистить эту директорию достаточно запустить скрипт allure_cleaner.py.