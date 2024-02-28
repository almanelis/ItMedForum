# MedItForum

## Как установить

1. Клонируем репозиторий

```
git clone git@github.com:almanelis/ItMedForum.git
```

2. Создаём и активируем виртуальное окружение

```
python -m venv venv
```

```
source venv/Scripts/activate
```

3. Устанавливаем зависимости

```
pip install -r requirements.txt
```

## Как запустить Django приложение

```
python med_it_forum/manage.py runserver
```

Далее переходим по url из терминала

## Как запустить Tailwind css

```
python med_it_forum/manage.py tailwind start
```

### Создаём миграции и суперюзера

```
python med_it_forum/manage.py migrate
```

```
python med_it_forum/manage.py createsuperuser
```

### Работа с админкой

Так как база данных пустая, то в админке вы легко можете добавить необходимую инфу
Для этого нужно перейти по url и ввести логин и пароль своего суперюзера

```
http://127.0.0.1:8000/admin/
```

## Про работу с гитом

### Как обновить файлы до последнего коммита на локальном компьтере

```
git pull
```

### Как добавлять файлы в репозиторий на GitHub

1. Создаём новую ветку

```
git checkout -b <название ветки>
```
2. Работаем в своей ветке над своей задачей
3. Добавляем файлы в коммит

## Директории

```
|—— .gitignore
|—— med_it_forum
|    |—— db.sqlite3
|    |—— feed  <--- приложение ленты новостей
|    |—— manage.py
|    |—— media
|    |—— med_it_forum  <--- конфиги
|    |—— sent_emails                         <--- эмуляция электронных писем
|    |—— static  <--- статика
|        |—— css
|        |—— img
|        |—— js
|    |—— templates   <--- директория с шаблонами
|        |—— base.html                        <--- базовый шаблон
|        |—— feed
|            |—— index.html                   <--- главная страница
|        |—— includes
|            |—— footer.html
|            |—— header.html                  <--- хэдер c навбаром
|            |—— post_card.html
|        |—— profile
|            |—— user_profile.html            <--- страница профиля
|        |—— registration
|            |—— logged_out.html              <--- шаблон с уведомлением о разлогине
|            |—— login.html                   <--- шаблон с формой для аутентификации
|            |—— password_change_done.html    <--- шаблон о успешной смене пароля
|            |—— password_change_form.html    <--- шаблон с формой для смены пароля
|            |—— password_reset_complete.html <--- шаблон о успешном обновлении пароля
|            |—— password_reset_confirm.html  <--- шаблон о востановлении пароля
|            |—— password_reset_done.html     <--- шаблон с уведомление о письме на почту
|            |—— password_reset_form.html     <--- шаблон с формой для восстановления пароля
|            |—— registration_form.html       <--- форма регистрации
|    |—— users  <--- приложение пользователя
|—— README.md
|—— requirements.txt  <--- файл со списком зависимостей
```
