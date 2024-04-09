import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
import socket
import urllib3.exceptions
from vktools import Keyboard, ButtonColor, Text, OpenLink
<<<<<<< HEAD
import time
import logging

logging.basicConfig(filename='bot.log', level=logging.ERROR)

vk = vk_api.VkApi(token="vk1.a._-5iqt02c4nom0Y8ZMKNr5XgVCHVKGCmn6SpNwcYW01xSC_jinZRmCCW9pzcjso_iZouXiq3IN33oSNraVU1GcDcfO1CAigGe9v-6LsBFjEG5gNrHt23NMUo_AK0Jx3ETuhJZNOiElMnq4OmOw3eXxSPGJAwBBSNcpyEy0hz6RQKTx_zmjHRTZ-oUnR7n6KFJzMNfkokrF8jV-Mgs9ancQ")

def send_message(user_id, message, keyboard=None):
    try:
        values = {
            "user_id": user_id,
            "message": message,
            "random_id": 0
        }
        if keyboard is not None:
            values["keyboard"] = keyboard.add_keyboard()
        vk.method("messages.send", values)
        time.sleep(1)
    except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError, socket.timeout, urllib3.exceptions.ReadTimeoutError, vk_api.exceptions.ApiHttpError) as e:
        logging.error(f"Ошибка при отправке сообщения: {str(e)}")
=======

vk = vk_api.VkApi(token="xxx")


def send_message(user_id, message, keyboard=None):
    values = {
        "user_id": user_id,
        "message": message,
        "random_id": 0
    }

    if keyboard is not None:
        values["keyboard"] = keyboard.add_keyboard()

    vk.method("messages.send", values)
>>>>>>> a514e8ab0267ed230d89a6994a0966f208a1ee46

while True:
    try:
        for event in VkLongPoll(vk).listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                text = event.text.lower()
                user_id = event.user_id

                if text == "начать" or text == "старт" or text == "start":
                    keyboard = Keyboard(
                        [
                            [
                                OpenLink("ПОВЫШЕННАЯ ГОС. СОЦИАЛЬНАЯ СТИПЕНДИЯ", "https://vk.com/wall-22117146_3797"),
<<<<<<< HEAD
                            ],
                            [
                                OpenLink("ГОСУДАРСТВЕННАЯ СОЦИАЛЬНАЯ СТИПЕНДИЯ", "https://vk.com/wall-22117146_3785"),
=======

                            ],
                            [
                                OpenLink("ГОСУДАРСТВЕННАЯ СОЦИАЛЬНАЯ СТИПЕНДИЯ", "https://vk.com/wall-22117146_3785"),

>>>>>>> a514e8ab0267ed230d89a6994a0966f208a1ee46
                            ],
                            [
                                OpenLink("ПОВЫШЕННАЯ СОЦИАЛЬНАЯ СТИПЕНДИЯ", "https://vk.com/wall-22117146_3799"),
                                OpenLink("ПРОФКАРД", "https://vk.com/wall-22117146_3807"),
<<<<<<< HEAD
=======

>>>>>>> a514e8ab0267ed230d89a6994a0966f208a1ee46
                            ],
                            [
                                OpenLink("Мат.помощь от Профсоюза", "https://vk.com/wall-22117146_3800"),
                                OpenLink("Мат.помощь от ВУЗа", "https://vk.com/wall-22117146_3818"),
                            ],
                            [
                                OpenLink("Стипендии", "https://vk.com/wall-22117146_3783"),
                            ],
<<<<<<< HEAD
                            # [
                            #     Text("Вызвать администратора", ButtonColor.NEGATIVE),
                            # ],
                        ],
                    )
                    send_message(user_id, "Если кнопки скрыты - повторите start в чат", keyboard)
    except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError, socket.timeout, urllib3.exceptions.ReadTimeoutError, vk_api.exceptions.ApiHttpError) as e:
        logging.error(f"Ошибка в основном цикле: {str(e)}")
        time.sleep(5)  
    except KeyboardInterrupt:
        print("Программа завершена пользователем.")
        break
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
=======
                            [
                                Text("Вызвать администратора", ButtonColor.NEGATIVE),
                            ],
                        ],
                    )

                    send_message(user_id, "Если кнопки скрыты - повторите start в чат", keyboard)
    except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError, socket.timeout, urllib3.exceptions.ReadTimeoutError, vk_api.exceptions.ApiHttpError):
        print('_______Timeout______')
>>>>>>> a514e8ab0267ed230d89a6994a0966f208a1ee46
