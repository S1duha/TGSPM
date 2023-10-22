import pyautogui
import time,pyperclip, keyboard

time.sleep(0.3)
while True:
    while True:
        # Клик по определенным координатам L1.1
        click_x, click_y = -1803, -43 #беседа 1
        pyautogui.click(click_x, click_y)
        time.sleep(1)
        click_q, click_e = -1834, 334 #чат 1
        pyautogui.click(click_q, click_e)
        keyboard.press_and_release('ctrl + a')
        break

    def paste(text: str):    
        # Сохраняем текущее содержимое буфера обмена
        buffer = pyperclip.paste()
        # Копируем указанный текст в буфер обмена
        pyperclip.copy(text)
        # Эмулируем нажатие сочетания клавиш Ctrl+V для вставки текста
        keyboard.press_and_release('ctrl + v')
        # Восстанавливаем предыдущее содержимое буфера обмена
        pyperclip.copy(buffer)


    def type(text: str, interval=0.0):    
        if interval == 0.0:
            # Если интервал равен нулю, используем функцию paste() для вставки всего текста сразу
            paste(text)
            return

        # Сохраняем текущее содержимое буфера обмена
        buffer = pyperclip.paste()
        for char in text:
            # Копируем текущий символ в буфер обмена
            pyperclip.copy(char)
            # Эмулируем нажатие сочетания клавиш Ctrl+V для вставки символа
            keyboard.press_and_release('ctrl + v')
            # Ждем указанный интервал времени перед следующей итерацией
            time.sleep(interval)
        # Восстанавливаем предыдущее содержимое буфера обмена
        pyperclip.copy(buffer)

    # Вызываем функцию type() для набора текста "Привет мир!" с интервалом 0.1 секунды между символами
    type('Подпишусь на вас взаимно и без отписок!                                                             https://twitter.com/atopamsss', 0.07)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)

    while True:
        # Клик по определенным координатам L1.2
        click_x, click_y = -1778, 16 #беседа 2
        pyautogui.click(click_x, click_y)
        time.sleep(1)
        click_q, click_e = -1834, 334 #чат 2
        pyautogui.click(click_q, click_e)
        keyboard.press_and_release('ctrl + a')
        break

    type('Подпишусь на вас взаимно и без отписок!                                                             https://twitter.com/atopamsss', 0.07)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)

    
    while True:
        # Клик по определенным координатам L1.3
        click_x, click_y = -1840, 73 #беседа 3
        pyautogui.click(click_x, click_y)
        time.sleep(1)
        click_q, click_e = -1834, 334 #чат 3
        pyautogui.click(click_q, click_e)
        keyboard.press_and_release('ctrl + a')
        break

    type('Подпишусь на вас взаимно и без отписок!                                                             https://twitter.com/atopamsss', 0.07)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(1)

    while True:
        # Клик по определенным координатам L1.4
        click_x, click_y = -1758, 136 #беседа 4
        pyautogui.click(click_x, click_y)
        time.sleep(1)
        click_q, click_e = -1834, 334 #чат 4
        pyautogui.click(click_q, click_e)
        keyboard.press_and_release('ctrl + a')
        break

    type('Подпишусь на вас взаимно и без отписок!                                                             https://twitter.com/atopamsss', 0.07)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press('esc')
    time.sleep(4000)