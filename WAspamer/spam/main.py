#//information//
#//version 0.2//
#//vk: @blinchikvk//
#//tg: @blinchiktg//

#//imports//
from settings import message, timemsg
import pyautogui as waspam
import time

#//info of user//

msglimit = input('Введите кол-во потоков для отправки: ')
msg = message
print(f'Перейдите в поле отправки сообщения в web.whatsapp.com! У вас {timemsg} секунд!')

#//wait :) //
time.sleep(timemsg)

x = 0
#//spam//
if msglimit is not None:

	while x < int(msglimit):

		waspam.typewrite(msg) # поток 1
		waspam.press('Enter')
		waspam.typewrite(msg) # поток 2
		waspam.press('Enter')
		waspam.typewrite(msg) # поток 3
		waspam.press('Enter')
		waspam.typewrite(msg) # поток 4
		waspam.press('Enter')
		waspam.typewrite(msg) # поток 5
		waspam.press('Enter')
		waspam.typewrite(msg) # поток 6
		waspam.press('Enter')
		waspam.typewrite(msg) # поток 7
		waspam.press('Enter')
		waspam.typewrite(msg) # поток 8
		waspam.press('Enter')
		waspam.typewrite(msg) # поток 9
		waspam.press('Enter')
		waspam.typewrite(msg) # поток 10
		waspam.press('Enter')
		x += 1
		print(f'info: Отправлено потоков: {x}')
		
else:
	pass
