# Ли Бо — Телеграм-бот и веб-аналитика

Телеграм-бот для чайного бара «Ли Бо» с веб-сайтом аналитики.

## Возможности

### Телеграм-бот
- **Меню** — полное меню с описанием, составом и ценами. Категории: холодные безалкогольные, горячие безалкогольные, алкогольные. Навигация инлайн-кнопками. Поддержка фотографий (опционально).
- **О нас** — информация о баре, авторах, ссылки на соц. сети (VK, Telegram, Instagram).
- **Подобрать коктейль** — тест из 5 вопросов с подбором 3 лучших коктейлей. Возможность оценить и оставить отзыв.
- **Карточка гостя** — личная статистика: число подборов, оценки и отзывы.

### Веб-сайт аналитики
- Авторизация (логин: `admin`, пароль: `adminLIBO`).
- Метрики: кол-во гостей, подборов, оценок.
- Таблица гостей с переходом в детальную карточку.
- Таблица популярных коктейлей.
- Экспорт данных в CSV и Excel.
- Ссылки на соц. сети.

## Быстрый старт

### Требования
- Python 3.10+
- Токен Telegram-бота (получить через [@BotFather](https://t.me/BotFather))

### Локальная установка

```bash
# Клонировать репозиторий
git clone <URL>
cd chaykabarka

# Создать виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Установить зависимости
pip install -r requirements.txt

# Задать токен бота
export BOT_TOKEN="ваш_токен"  # Linux/macOS
# set BOT_TOKEN=ваш_токен     # Windows

# Запустить бот + веб-сервер
python run.py
```

Веб-аналитика будет доступна по адресу `http://localhost:5000`.

### Запуск через Docker

```bash
docker build -t libo-bot .
docker run -d \
  -e BOT_TOKEN="ваш_токен" \
  -p 5000:5000 \
  --name libo \
  libo-bot
```

## Структура проекта

```
chaykabarka/
├── bot.py              # Телеграм-бот (Aiogram 3)
├── web.py              # Flask веб-сервер аналитики
├── run.py              # Запуск бота и веб-сервера вместе
├── database.py         # Модуль работы с SQLite
├── cocktails.py        # Данные о коктейлях и логика подбора
├── requirements.txt    # Python-зависимости
├── Dockerfile          # Docker-контейнер
├── pictures/           # Фотографии коктейлей (опционально)
├── templates/          # HTML-шаблоны для веб-сайта
│   ├── login.html
│   ├── dashboard.html
│   └── user_detail.html
└── static/
    └── style.css       # Стили веб-сайта
```

## Фотографии коктейлей

Фотографии помещаются в папку `pictures/`. Имена файлов должны соответствовать полю `image` в `cocktails.py`. Поддерживаемые форматы: `.jpg`, `.jpeg`, `.png`, `.webp`.

### Таблица имён файлов

| Коктейль | Имя файла |
|---|---|
| Банановое молоко | `bananovoe_moloko.jpg` |
| Лиловая гуанинь | `lilovaya_guanin.jpg` |
| Старый князь | `stariy_knyaz.jpg` |
| Нефритовая река | `nefritovaya_reka.jpg` |
| Золотая обезьяна | `zolotaya_obezyana.jpg` |
| Тайваньские пираты | `tayvanskie_piraty.jpg` |
| Аметистовое вино | `ametistovoe_vino.jpg` |
| Сестрицы мэй | `sestricy_mey.jpg` |
| Южный феникс | `yuzhniy_feniks.jpg` |
| Цветы и птицы Сюй Вэя | `cvety_i_pticy.jpg` |
| Гроздья ягод бытия | `grozdya_yagod.jpg` |
| Без тревог | `bez_trevog.jpg` |
| Сычуаньские перцы | `sychuanskie_percy.jpg` |
| Красная обезьяна | `krasnaya_obezyana.jpg` |
| Чутка киселе | `chutka_kisele.jpg` |
| Горячая свинюшка | `goryachaya_svinyushka.jpg` |
| Правила Чэн Ай Сао | `pravila_chen_ay_sao.jpg` |
| Лунный апельсин | `lunniy_apelsin.jpg` |
| Еще киселе | `eshe_kisele.jpg` |
| Осенняя дымка | `osennyaya_dymka.jpg` |
| Полночь в саду | `polnoch_v_sadu.jpg` |
| Чукинский экспресс | `chukinskiy_ekspress.jpg` |
| Биси | `bisi.jpg` |
| Яцзы | `yaczi.jpg` |
| Чивэнь | `chiven.jpg` |
| Цуню | `cunyu.jpg` |
| Чаофэн | `chaofeng.jpg` |
| Цзяоту | `czyaotu.jpg` |
| Пулао | `pulao.jpg` |
| Биань | `bian.jpg` |
| Суаньни | `suanni.jpg` |

Расширение может быть `.jpg`, `.jpeg`, `.png` или `.webp`. Бот автоматически ищет файл с любым из этих расширений. Если фотография не найдена, коктейль отображается только текстом.

## Поддержка и внесение изменений

### Добавление нового коктейля

1. Откройте `cocktails.py`.
2. Добавьте словарь в нужный список (`COLD_COCKTAILS`, `HOT_COCKTAILS` или `ALCOHOLIC_COCKTAILS`):
   ```python
   {
       "name": "Название",
       "description": "Описание вкуса.",
       "ingredients": "Ингредиент 1, ингредиент 2",
       "price": 350,
       "image": "imya_fayla",
       "tags": {"taste": "sweet", "tea": "more", "strength": "soft"},
   }
   ```
3. Положите фото в `pictures/imya_fayla.jpg` (опционально).

### Теги для подбора

- `taste`: `sweet` (сладкий), `sour_sweet` (кисло-сладкий), `sour` (кислый)
- `tea`: `more` (более чайный), `less` (менее чайный)
- `strength`: `strong` (крепкий), `soft` (мягкий)

### Изменение пароля веб-панели

В `web.py` измените переменные `ADMIN_LOGIN` и `ADMIN_PASSWORD`.

### Переменные окружения

| Переменная | По умолчанию | Описание |
|---|---|---|
| `BOT_TOKEN` | — | Токен Telegram-бота (обязательный) |
| `DB_PATH` | `libo.db` | Путь к файлу базы данных |
| `WEB_PORT` | `5000` | Порт веб-сервера |
| `FLASK_SECRET` | auto | Секретный ключ Flask |

### База данных

SQLite база `libo.db` создаётся автоматически при первом запуске. Таблицы:

- `users` — пользователи бота
- `quiz_sessions` — сессии подбора коктейлей
- `cocktail_ratings` — оценки и отзывы

### Обновление зависимостей

```bash
pip install --upgrade -r requirements.txt
```

## Лицензия

Проект разработан для бара «Ли Бо».

**Авторы:**
- Разработчик — Руденко Вячеслав Александрович
- Тестировщик — Баркалов Владимир Вячеславович
