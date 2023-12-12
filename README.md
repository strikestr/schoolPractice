[# _schoolPractice_](https://e.sfu-kras.ru/mod/assign/view.php?id=1516444)
### Функционал
- Функция lighten(сolor, percent):
  Делает полученный цвет светлее.
  - Получаемые данные:
    - color: str (#xxxxxx)
    - percent: int
  - Формула:
    ```python
    nred = min(255, red + (255 - red) * percent // 100) 
    ngreen = min(255, green + (255 - green) * percent // 100)
    nblue = min(255, blue + (255 - blue) * percent // 100)
    ```
    
- Функция darken(сolor, percent):
  Делает полученный цвет темнее.
  - Получаемые данные:
    - color: str (#xxxxxx)
    - percent: int
  - Формула:
    ```python
    nred = max(0, red - red * percent // 100)
    ngreen = min(0, green - green * percent // 100)
    nblue = max(0, blue - blue * percent // 100)
    ```
  
### Пример использования
1. Вводим значения
<img width="361" alt="image" src="https://github.com/strikestr/schoolPractice/assets/68343771/fbd333d1-dfb6-4239-a203-0dba8e38c683">
   
2. Полученный ответ
<img width="707" alt="image" src="https://github.com/strikestr/schoolPractice/assets/68343771/bc4cbd87-3df3-4722-a5a5-f5f0296fc693">



### Запуск и настройка проекта
1. Склонировать проект
2. Обновить pip:
   ```bash
   pip install --upgrade pip
   ```
3. Установить необходимые пакеты:
   ```bash
   pip install -r requirements.txt
   ```
4. Запуск проекта:
   ```bash
   python main.py
   ```
5. [x] Готово


    
