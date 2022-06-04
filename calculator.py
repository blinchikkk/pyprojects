#//information://

#//Version 0.3//
#//git: https://github.com/blinchikkk/pyprojects/blob/main/calculator.py //
#//vk: @blinchikvk//

#//import//
import time
from colorama import init
from colorama import Fore, Back, Style
init()

#//calc//



def calc():
	request1 = float(input('Введите первое число: '))
	request2 = float(input('Введите второе число: '))
	request3 = input('Введите действие: ')

	if request1 and request2 and request3 is not None:

		if request3 in ['+', 'сумма', 'плюс']:
			time.sleep(0.2)
			print(f'Результат: {Fore.GREEN}{request1 + request2}')

		elif request3 in ['-', 'вычетание', 'минус']:
			time.sleep(0.2)
			print(f'Результат: {Fore.GREEN}{request1 - request2}')

		elif request3 in ['*', 'произведение', 'умножить', 'умножение']:
			time.sleep(0.2)
			print(f'Результат: {Fore.GREEN}{request1 * request2}')

		elif request3 in ['/', '//', 'деление']:
			time.sleep(0.2)
			print(f'Результат: {Fore.GREEN}{request1 / request2}')

		else:
			pass

calc()

