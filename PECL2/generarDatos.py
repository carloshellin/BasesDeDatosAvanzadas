# Script para generar datos de PECL2 en BDA
# Carlos Hellín y Ana Cortés

import csv
from random import randint, choice, randrange, sample
import datetime

with open('tienda.csv', mode='w', newline='\n') as file:
	writer = csv.writer(file, delimiter=',')

	for i in range(1, 200001):
		writer.writerow([i, 'nombre' + str(i), 'ciudad' + str(i), 'barrio' + str(i), 'provincia' + str(i)])


with open('productos.csv', mode='w', newline='\n') as file:
	writer = csv.writer(file, delimiter=',')

	for i in range(1, 1000001):
		writer.writerow(['codigo' + str(i), 'nombre' + str(i), 'tipo' + str(i), 'descripcion' + str(i), randint(50, 1000)])


with open('tienda_productos.csv', mode='w', newline='\n') as file:
	writer = csv.writer(file, delimiter=',')

	for i in range(1, 200001):
		list = sample(range(1, 1000001), 100)
		for j in range(1, 101):
			writer.writerow([i, 'codigo' + str(list[j - 1]), randint(10, 200)])


with open('trabajador.csv', mode='w', newline='\n') as file:
	writer = csv.writer(file, delimiter=',')

	list = sample(range(10000000, 100000000), 1000000)
	for i in range(1, 1000001):
		writer.writerow([i, str(list[i - 1]) + choice('TRWAGMYFPDXBNJZSQVHLCKE'), 'nombre' + str(i), 'apellidos' + str(i), 'puesto' + str(i), randint(1000, 5000), randint(1, 200000)])

start_date = datetime.date(2019, 1, 1)
end_date = datetime.date(2020, 12, 31)
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days

with open('ticket.csv', mode='w', newline='\n') as file:
	writer = csv.writer(file, delimiter=',')

	for i in range(1, 5000001):
		random_number_of_days = randrange(days_between_dates)
		random_date = start_date + datetime.timedelta(days=random_number_of_days)

		writer.writerow([i, randint(100, 10000), random_date, randint(1, 1000000)])

with open('ticket_productos.csv', mode='w', newline='\n') as file:
	writer = csv.writer(file, delimiter=',')

	for i in range(1, 5000001):
		n = randint(1, 10)
		list = sample(range(1, 1000001), n)
		for j in range(n):
			writer.writerow([i, 'codigo' + str(list[j - 1]), randint(1, 10)])
