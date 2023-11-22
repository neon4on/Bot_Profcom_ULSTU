import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
import socket
import urllib3.exceptions
from vktools import Keyboard, ButtonColor, Text, OpenLink

vk = vk_api.VkApi(token="vk1.a.h9NqJdw2Bmybks7mC01e66EYc5J7DhN_5_S8Xfx-1b7lpC6xl4qJDm7nA4NpWmHMl250Wjp0lJGLykh9teSujehd9IxWeXJ4jRPfj6pOevjnAFdCqPqMufweIE523nG5BkCjkXfOHs54L8ejjmKwRaD_QksdT7O50mu8_XXmQzOaz3Q3S9b1S71ZCEglc-W-I3TKjKdIx8xcGXAHuPsr4A")


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
                                OpenLink("ПГАС", "https://vk.com/wall-22117146_3797"),
                                OpenLink("ГСС", "https://vk.com/wall-22117146_3785"),
                            ],
                            [
                                OpenLink("ПСС", "https://vk.com/wall-22117146_3799"),
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
                                Text("АДМИНИСТРАТОР", ButtonColor.NEGATIVE),
                            ],
                        ],
                    )

                    send_message(user_id, "Если кнопки скрыты - повторите start в чат", keyboard)
    except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError, socket.timeout, urllib3.exceptions.ReadTimeoutError):
        print('_______Timeout______')
