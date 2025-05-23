# Aeza API

### Описание
Пакет предназначенный для получения легкого доступа к API Aeza в ваших проектах

### Методы
#TODO
### Примеры

```python
from aeza_api import api as aeza

aeza_client = aeza.AuthAeza('API-KEY')


def test() -> str:
    """Функция проверит баланс,
       если он меньше 50 рублей,
       то создаcт счёт на сумму 500 рублей
       при этом метод сразу возвращает ссылку для оплаты."""
    if aeza_client.get_balance() < 50:
        return TOKEN.invoice_card(500)
    return 'Всё хорошо'
```

<b>Покупка сервера</b>

```python
from aeza_api import api as aeza

TOKEN = aeza.AuthAeza('API-KEY')


def test() -> str:
    """Покупка сервера."""
    return aeza_client.ordering_service(1, # Количество
                                  'mount', # Срок (hour, mount, quarter_year, year, half_year)
                                  'NameServer', # Имя сервера
                                  3, # ID сервера (Можно узнать методом get_product)
                                  25, # os
                                  True) # Автопродление
```

### Начало работы

Для начала работы импортируйте библиотеку, предварительно установив её
```
pip install aeza_api
```
```python
from aeza_api import api 
```
Далее инициализируйте API-ключ
```python
aeza_client = api.AuthAeza('API-KEY')
```
Все методы делаются через переменную в которой вы инициализировали API-ключ
```python
aeza_client.get_my_server()
```
