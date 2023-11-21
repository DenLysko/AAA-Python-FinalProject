# AAA-Python-FinalProject

## Запуск директив из инструкции
Находясь по дирректории
```
..\AAA-Python-FinalProject
```

запустите директиву 
```
python cli.py menu
```
для того, чтобы посмотреть меню.

А для того чтобы сделать заказ, запустите директиву
```
python cli.py order <pizza_name> --delivery
```

## Запуск текстов
Находясь по дирректории
```
..\AAA-Python-FinalProject
```

запустите директиву 
```
python -m pytest -v tests_pizza.py
```
для тестов к файлу pizzas.py.

А для того, чтобы запустить тексты для файла sizes.py, используйте команду
```
python -m pytest -v tests_sizes.py
```

## Примечание
Для облегчения проверки, сразу предупрежу, что не успел встроить декоратор