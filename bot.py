import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
import socket
import urllib3.exceptions
from vktools import Keyboard, ButtonColor, Text, OpenLink

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

                            ],
                            [
                                OpenLink("ГОСУДАРСТВЕННАЯ СОЦИАЛЬНАЯ СТИПЕНДИЯ", "https://vk.com/wall-22117146_3785"),

                            ],
                            [
                                OpenLink("ПОВЫШЕННАЯ СОЦИАЛЬНАЯ СТИПЕНДИЯ", "https://vk.com/wall-22117146_3799"),
                                OpenLink("ПРОФКАРД", "https://vk.com/wall-22117146_3807"),

                            ],
                            [
                                OpenLink("Мат.помощь от Профсоюза", "https://vk.com/wall-22117146_3800"),
                                OpenLink("Мат.помощь от ВУЗа", "https://vk.com/wall-22117146_3818"),
                            ],
                            [
                                OpenLink("Стипендии", "https://vk.com/wall-22117146_3783"),
                            ],
                            [
                                Text("Вызвать администратора", ButtonColor.NEGATIVE),
                            ],
                        ],
                    )

                    send_message(user_id, "Если кнопки скрыты - повторите start в чат", keyboard)
    except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError, socket.timeout, urllib3.exceptions.ReadTimeoutError, vk_api.exceptions.ApiHttpError):
        print('_______Timeout______')
