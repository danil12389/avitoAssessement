# avitoAssessement

Клонируем репозиторий

Создаем виртуальное окружение

Устаниавливаем зависимости

`pip install -r requirements.txt`

Запускать можно двумя путями:

1. Кидаем файл .json с тестовыми данными в директорию проекта и удаляем предыдущий файл .json.
    
    **файл .json в директории должен быть только один**
    
    Затем вызываем `python main.py`


2. Либо сразу вызываем `python main.py absolutePath`, передавая абсолютный путь до файла .json. 

   Пример: `python main.py C:\Users\Dan\Desktop\Test\example.json`
