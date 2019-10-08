# rtsp-snapshoter
Этот скрипт каждую секунду делает снимок RTSP-потока
и сохраняет его в директорию `output/`.

## Установка зависимостей

```shell script
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

## Запуск
```shell script
$ python3 main.py
```

## Деактивация виртуального окружения (venv)
```shell script
$ deactivate
```
