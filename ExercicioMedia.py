while True:

	print('Bem Vinda(o), digite "exit" a qualquer momento para sair.\n')
	count = 1

	try:
		total_cursos = input('Total de cursos realizados: ')
		if total_cursos == 'exit':
			print('\nAté logo!')
			break
		else:
			total_cursos = eval(total_cursos)
	
	except NameError:
		print('\nDigite os dados corretamente!\n')
		total_cursos = input('Total de cursos realizados: \n')	
		
	
	while count <= int(total_cursos):
		try:
			nota = input(f'Insira a(s) nota(s) do curso {count}: ')
			if type(eval(nota)) == type(int()):
				print(f'A média do curso é: {eval(nota):.1f}\n')
				count += 1
			else:
				print(f'A média do curso é: {sum(eval(nota))/len(eval(nota)):.1f}\n')
				count += 1

		except (NameError, TypeError):
			if nota == 'exit':
				print('\nAté logo!')
				break
			else:
				print('\nDigite os dados corretamente, ex: 10, 9, 8 !\n')

	if nota != 'exit':
		print('Até logo!')
		break
	else:
		break
