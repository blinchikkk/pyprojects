#//imports//
from settings import message
import pyautogui as waspam
import time

#//info of user//

msglimit = input('Введите кол-во сообщений для отправки: ')
msg = message
print('Подождите 5 секунд и нажмите Enter!')

#//wait :) //
time.sleep(5)

x = 0 

#//spam//
while x < int(msglimit):

	waspam.typewrite(msg)
	waspam.press('Enter')
	x += 1
