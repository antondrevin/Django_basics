from datetime import datetime


def greeting() -> str:
    """
    Приветствие
    """

    now_time = int(datetime.now().strftime("%H"))

    if 18 <= now_time <= 21:
        result = "Добрый вечер"
    elif 6 <= now_time <= 10:
        result = "Доброе утро"
    elif 11 <= now_time <= 17:
        result = "Добрый день"
    else:
        result = "Доброй ночи"
    return result
