# EM MANUTENÇÃO!

while True:

	print('Bem Vinda(o), digite "exit" a qualquer momento para sair.')
	print('Use pontos ao invés de vírgulas para separar as casas decimais\n')

	count = 1

	try:
		total_cursos = input('Total de cursos realizados: ')
		print('\n')

		if total_cursos == 'exit':
			print('\nAté logo!')
			break
		else:
			total_cursos = eval(total_cursos)
	
	except NameError:
		print('Digite os dados corretamente!\n')
		total_cursos = input('Total de cursos realizados: \n')	

	
	while count <= int(total_cursos):
		try:
			nota = eval(input(f'Insira a(s) nota(s) do curso {count}: '))
			if type(nota) == type(int()) or type(float()): 
				print(f'A média do curso é: {nota:.1f}\n')
				count += 1
			else:
				nota = str(nota).replace(',','.')
				nota = nota.split()
				print(f'A média do curso é: {sum(nota)/len(nota):.1f}\n')
				count += 1

		except (NameError, TypeError, SyntaxError):
			if nota == 'exit':
				print('\nAté logo!')
				break
			else:
				try:
					nota = str(nota).replace(',','.')
					nota = nota.split()
					print(f'A média do curso é: {sum(nota)/len(nota):.1f}\n')
					count += 1
				except (NameError, TypeError, SyntaxError):
					print('\nDigite os dados corretamente: 10, 9, 8.8\n')

	if nota != 'exit':
		print('Até logo!')
		break
	else:
		break
