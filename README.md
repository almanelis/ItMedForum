MedItForum
===
## Как установить
1. Клонируем репозиторий
  ```
  git clone git@github.com:almanelis/MedItForum.git
  ```
  или, если не используете SSH ключ(с ним лучше, напишите, если нужно помочь его подключить)
  ```
  git clone https://github.com/almanelis/MedItForum.git
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

## Директории
```
|—— .gitignore
|—— med_it_forum      <--- основная директория проекта
|    |—— main         <--- приложение главной сраницы
|        |—— admin.py
|        |—— apps.py
|        |—— migrations
|        |—— models.py
|        |—— tests.py
|        |—— urls.py
|        |—— views.py
|    |—— manage.py
|    |—— med_it_forum       <--- файл с конфигами проекта
|        |—— asgi.py
|        |—— settings.py
|        |—— urls.py
|        |—— wsgi.py
|    |—— static             <--- статические файлы проекта
|        |—— css
|        |—— js
|        |—— img
|    |—— templates          <--- папка с вёрсткой страниц
|        |—— auth
|        |—— main
|            |—— index.html   <--- пример страницы
|        |—— profile
|        |—— includes       <--- часто повторяющиеся фрагменты c примерами
|            |—— footer.html
|            |—— header.html
|            |—— post_card.html
|—— requirements.txt         <--- файл со списком необходимых для работы библиотеками
```
## Про работу с гитом
### Как добавлять файлы в репозиторий на GitHub
Когда написали какую-то часть и хотите ей поделиться, то выполняем следующие команды 
1. Проверяем какие файлы изменились/добавились:
  ```
  git status
  ```
2. Создаём локальный коммит:
  ```
  git commit -m "<комментарий>"
  ```
3. Ещё раз проверьте и запуште 
  ```
  git status
  ```
  ```
  git push
  ```
  Далее проверяем на гитхабе всё ли нормально

### Как обновить файлы до последнего коммита на локальном компьтере
  ```
  git pull
  ```
