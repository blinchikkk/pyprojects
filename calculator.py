#//import//
import time

#//calc//

request1 = float(input('Введите первое число: '))
request2 = float(input('Введите второе число: '))
request3 = input('Введите действие: ')

def calc(request1, request2, request3):
	if request1 and request2 and request3 is not None:
		if request3 in ['+', 'сумма', 'плюс']:
			print(request1 + request2)
		elif request3 in ['-', 'вычетание', 'минус']:
			print(request1 - request2)
		elif request3 in ['*', 'произведение', 'умножить', 'умножение']:
			print(request1 * request2)
		elif request3 in ['/', '//', 'деление']:
			return request1 / request2
		else:
			pass

calc(request1, request2, request3)