#//information//
#//version 0.2//
#//vk: @blinchikvk//
#//tg: @blinchiktg//

#//imports//
from settings import message
import pyautogui as waspam
import time

#//info of user//

msglimit = input('Введите кол-во сообщений для отправки: ')
msg = message

#//wait :) //
time.sleep(5)

x = 0
#//spam//
if msglimit is not None:

	while x < int(msglimit):

		waspam.typewrite(msg)
		waspam.press('Enter')
		x += 1
else:
	pass
