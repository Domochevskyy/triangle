## Что делать?...

Открываем терминал  
Клонируем репозиторий командой ниже

    git clone https://github.com/Domochevskyy/triangle.git

Переходим в директорию, куда склонировали проект

    cd triangle

Создаём виртуальное окружение

    python -m venv venv

Если не работает команда выше, то попробуй

    python3 -m venv venv

Активируем виртуальное окружение

    source venv/bin/activate

Далее устанавливаем необходимые библиотеки

    pip install -r requirements.txt

А также установим сторонний пакет, который нужен для библиотеки wand  
для мака:

    brew install imagemagick
    
Если в команде выше возникают ошибки, то попробуй

    brew install python3-wand

Далее Запускаем скрипт

    python -m main.py

Готово. Вы восхитительны
