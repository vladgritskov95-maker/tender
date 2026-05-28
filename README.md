# ТендерСкан — Деплой на Render.com (бесплатно)

## Инструкция за 5 минут

### Шаг 1 — Зарегистрируйся на GitHub
Зайди на https://github.com → Sign up (бесплатно)

### Шаг 2 — Создай репозиторий
1. Нажми **New repository** (зелёная кнопка)
2. Название: `tenderscam` (или любое)
3. Выбери **Public**
4. Нажми **Create repository**

### Шаг 3 — Загрузи файлы
1. На странице репозитория нажми **uploading an existing file**
2. Перетащи ВСЕ файлы из этой папки:
   - `app.py`
   - `requirements.txt`
   - `Procfile`
   - папку `static/` с файлом `index.html`
3. Нажми **Commit changes**

### Шаг 4 — Деплой на Render.com
1. Зайди на https://render.com → Sign up with GitHub
2. Нажми **New +** → **Web Service**
3. Выбери свой репозиторий `tenderscam`
4. Настройки (всё заполнится автоматически):
   - **Name**: tenderscam
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: Free
5. Нажми **Create Web Service**

### Готово!
Через 2-3 минуты получишь ссылку вида:
**https://tenderscam.onrender.com**

Открывается с любого устройства, телефона, планшета — везде.

---

## Важно
- Бесплатный план Render "засыпает" через 15 минут неактивности
- Первый запрос после "сна" занимает ~30 секунд (потом всё быстро)
- Для постоянно активного сервиса — план Starter ($7/мес)
