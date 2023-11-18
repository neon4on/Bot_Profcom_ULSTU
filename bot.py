import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vktools import Keyboard, ButtonColor, Text, OpenLink, Location
import time
vk_session = vk_api.VkApi(token="vk1.a.h9NqJdw2Bmybks7mC01e66EYc5J7DhN_5_S8Xfx-1b7lpC6xl4qJDm7nA4NpWmHMl250Wjp0lJGLykh9teSujehd9IxWeXJ4jRPfj6pOevjnAFdCqPqMufweIE523nG5BkCjkXfOHs54L8ejjmKwRaD_QksdT7O50mu8_XXmQzOaz3Q3S9b1S71ZCEglc-W-I3TKjKdIx8xcGXAHuPsr4A")
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)

def send_some_msg(id, some_text, keyboard=None):
    post = {
        "user_id": id, 
        "message": some_text,
        "random_id": 0
    }

    if keyboard != None:
        post["keyboard"] = keyboard.add_keyboard()

    vk_session.method("messages.send", post)

    time.sleep(120)

    empty_keyboard(post, keyboard, some_text)
    
def empty_keyboard(post, keyboard, some_text):
    post["keyboard"] = keyboard.get_empty_keyboard()
    some_text = "Выбор действий скрыт"
    post["message"] = some_text
    vk_session.method("messages.send", post)
    start_keyboard(post, keyboard)

def start_keyboard(post, keyboard):
    keyboard = Keyboard(
                    [
                        [
                            Text("START", ButtonColor.PRIMARY),
                        ],
                    ],
                )
    some_text = "Для возвращения выбора действий напишите start"
    post["message"] = some_text
    post["keyboard"] = keyboard.add_keyboard()
    vk_session.method("messages.send", post)

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.lower()
            id = event.user_id
            if msg == "начать" or msg == "старт" or msg == "start":
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
                send_some_msg(id, "Если кнопки скрыты - повторите start в чат", keyboard)
            elif msg == 'привет':
                send_some_msg(id, "Привет! Для старта работы бота напиши start")
            # elif msg == "администратор" or "админ":

                
                
                # keyboard.add_line()
                # buttons = ["blue", "red", "white", "green"]
                # button_colors = [VkKeyboardColor.PRIMARY]
                # for btn, btn_color in zip(buttons, button_colors):
                #     keyboard.add_button(btn, btn_color)




                # keyboard.add_openlink_button("MEOW", 'https://vk.com/wall-22117146_3840')
                # send_some_msg(id, "Hi first!", keyboard)
                # send_some_msg(id, "Hi second!", keyboard)