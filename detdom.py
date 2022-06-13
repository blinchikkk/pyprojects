#detdom module 

def detdom():
	name = input("Введите имя: ")
	old = int(input("Введите возраст: "))
	gender = input("Введите пол: ")
	gender = gender.lower()
	reason = input("Введите причину: ")
	
	
	listgender = ['мужской', 'женский']

	if old >= 130:
		print('Неверный возраст!')

	if gender not in listgender:
		print('Неверный пол!')

	if gender in listgender[0]:
		x = ''

	elif gender in listgender[1]:
		x = 'а'

	print(f'Ребенок {name} в возрасте {old} полных лет был{x} сдан{x} в детский дом по причине: {reason}')
	

