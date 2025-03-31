# Парсер сайта https://dodopizza.ru

## Описание

Парсер на основе _Scrapy_ собирает товары с главной страницы и отправляет в их в _RabbitMQ_.

Дополнительно реализован comsumer на основе бибилотеки _FastStream_ для брокера, который записывает собранные обьекты в _PostgreSQL_.


## Требования для запуска
    - Docker version 28.0.4
    - GNU Make 4.3 (optional)


## Инструкция по запуску
1. Переименуйте файл _.env.example_ в _.env_:
```mv .env.example .env```

2. Опционально, определите список городов в файле _.env_. Например:
```CITIES=https://dodopizza.ru/moscow, https://dodopizza.ru/samara, https://dodopizza.ru/ufa```
3. Если у вас установлен Make, выполните команду для запуска всех необходимых сервисов:
```make up_prod_compose```
4. Если Make не установлен, можете использовать следующую команду Docker:
```docker compose -f docker-compose-prod.yaml up -d```

## Пример собранных данных
```{"item_id": "11eceba2b8864f6e96179b0606a94a70", "name": "Жюльен", "description": "Цыпленок, шампиньоны, ароматный грибной соус, лук, сухой чеснок, моцарелла, смесь сыров чеддер и пармезан, фирменный соус альфредо", "section": "Пиццы", "size": [25, 30, 35], "price": 619, "images": ["https://media.dodostatic.net/image/r:233x233/11ee7d6175c10773bfe36e56d48df7e3.avif", "https://media.dodostatic.net/image/r:233x233/11ee7d6175c10773bfe36e56d48df7e3.webp", "https://media.dodostatic.net/image/r:233x233/11ee7d6175c10773bfe36e56d48df7e3.png"], "city_link": "https://dodopizza.ru/moscow"}, {"item_id": "a0afbdbbc3fc8f0411ec8f1a00ebc0ad", "name": "Кофе Капучино", "description": "Легендарный рецепт кофе: эспрессо, горячее молоко и плотная молочная пенка ", "section": "Кофе", "size": null, "price": 179, "images": ["https://media.dodostatic.net/image/r:233x233/11ee7d61ae1813b4ab42d8927d061035.avif", "https://media.dodostatic.net/image/r:233x233/11ee7d61ae1813b4ab42d8927d061035.webp", "https://media.dodostatic.net/image/r:233x233/11ee7d61ae1813b4ab42d8927d061035.png"], "city_link": "https://dodopizza.ru/moscow"},```

## Описание обхода блокировки
В файле паука _dodo/dodo/spiders/dodo.py_  на 24-ой строчке содержится запрос для получения токена авторизации и сессионных куки, что позволяет обойти ограничения и успешно получать информацию со страницы города.

---
