from PIL import Image, ImageDraw, ImageFont


def lighten(color: str, percent: int) -> str:
    """_lighten_ - делает полученный цвет светлее на percent

    Описание:
        Получает на входе HEX Код в string форме.
        Далее конвертирует данный код в RGB и по формуле, получаем ответ.

    Формула:
        Нужно сделать для каждого цвета, то есть 3-ех. Для примера берем красный:
        min(255, red + (255 - red) * percent // 100)

    Аргументы:
        color (str): HEX код
        percent (int): Процент

    Пример:
        lighten("2FECAB", 20)

    Исключения:
        Неверные данные - это означает, что вы ввели недопустимые значения
    """
    color = color.lstrip("#")

    red = int(color[0:2], 16)
    green = int(color[2:4], 16)
    blue = int(color[4:6], 16)

    nred = min(255, red + (255 - red) * percent // 100)
    ngreen = min(255, green + (255 - green) * percent // 100)
    nblue = min(255, blue + (255 - blue) * percent // 100)

    make_img(red, green, blue, nred, ngreen, nblue)


def darken(color: str, percent: int) -> str:
    """_darken_ - делает полученный цвет темнее на percent

    Описание:
        Получает на входе HEX Код в string форме.
        Далее конвертирует данный код в RGB и по формуле, получаем ответ.

    Формула:
        Нужно сделать для каждого цвета, то есть 3-ех. Для примера берем красный:
        max(0, red - red * percent // 100)

    Аргументы:
        color (str): HEX код
        percent (int): Процент

    Пример:
        darken("2FECAB", 20)

    Исключения:
        Неверные данные - это означает, что вы ввели недопустимые значения
    """
    color = color.lstrip("#")

    red = int(color[0:2], 16)
    green = int(color[2:4], 16)
    blue = int(color[4:6], 16)

    nred = max(0, red - red * percent // 100)
    ngreen = max(0, green - green * percent // 100)
    nblue = max(0, blue - blue * percent // 100)

    make_img(red, green, blue, nred, ngreen, nblue)


def make_img(r, g, b, nr, ng, nb):
    font = ImageFont.truetype("SFU.ttf", 24)
    image = Image.open("template.png")
    draw = ImageDraw.Draw(image)
    draw.rectangle([30, 175, 180, 325], fill=(r, g, b))
    draw.text(
        (30, 340), "#{:02X}{:02X}{:02X}".format(r, g, b), fill=(r, g, b), font=font
    )
    draw.rectangle([320, 175, 470, 325], fill=(nr, ng, nb))
    draw.text(
        (320, 340),
        "#{:02X}{:02X}{:02X}".format(nr, ng, nb),
        fill=(nr, ng, nb),
        font=font,
    )

    image.show()


while True:
    print("[0] - закрыть программу\n[1] - сделать светлее\n[2] - сделать темнее")
    answer = input("Введите действие: ")
    if answer == "1":
        try:
            color = input("Введите HEX код цвета (#XXXXXX): ")
            to = int(input("Введите на сколько % сделать ярче без знака %: "))
            lighten(color, to)
        except ValueError:
            print("Неверные данные")
        except TypeError:
            print("Неверные данные")
    elif answer == "2":
        try:
            color = input("Введите HEX код цвета (#XXXXXX): ")
            to = int(input("Введите на сколько % сделать темнее без знака %: "))
            darken(color, to)
        except ValueError:
            print("Неверные данные")
    elif answer == "0":
        print("Программа завершена")
        break
    else:
        print("Такого действия нет")
