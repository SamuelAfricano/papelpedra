import random
from colorama import init, Fore, Back, Style
from enum import IntEnum
init() # iniciando um terminal de cores com corama

class Jogadas(IntEnum):
	Papel = 0
	Pedra = 1
	Tesoura = 2
	Lagarto = 3
	Spock = 4

def pegar_do_usuario():
	escolhas = [f"{j.name}[{j.value}]" for j in Jogadas  ]
	escolhas_str = ", ".join(escolhas)
	entrada_usuario = int(input(f"Escolhe ({escolhas_str}): "))
	j = Jogadas(entrada_usuario)
	return j	

def pegar_do_computador():
	selecione = random.randint(0, len(Jogadas) - 1)
	j = Jogadas(selecione)
	return j

def determinar_vencedor(jogada_do_usuario, jogada_do_computador):
	victoria = {
	 Jogadas.Pedra: [Jogadas.Tesoura, Jogadas.Lagarto],
	 Jogadas.Tesoura: [Jogadas.Papel, Jogadas.Lagarto],
	 Jogadas.Papel: [Jogadas.Pedra, Jogadas.Spock],
	 Jogadas.Lagarto: [Jogadas.Spock, Jogadas.Papel],
	 Jogadas.Spock: [Jogadas.Tesoura, Jogadas.Pedra]
	}

	escolhas = victoria[jogada_do_usuario]
	if jogada_do_usuario == jogada_do_computador:
		print( Fore.YELLOW + "Jogo empatado." + Style.RESET_ALL)
	elif jogada_do_computador in escolhas :
		print(Fore.GREEN + f"{Fore.GREEN} {jogada_do_usuario.name} bate {jogada_do_computador.name} Venceste!" + Style.RESET_ALL)
	else:
		print(Fore.RED + f"{jogada_do_computador.name} bate {jogada_do_usuario.name} você perdeu!" + Style.RESET_ALL)


while True:
	try:
		jogada_do_usuario = pegar_do_usuario()
	except ValueError as e:
		aviso = f"[0, {len(Jogadas) -1}]"
		print( Fore.RED + f"Entrada inválida. Escolha um valor entre {aviso}" + Style.RESET_ALL)
		continue

	jogada_do_computador = pegar_do_computador()
	determinar_vencedor(jogada_do_usuario, jogada_do_computador)

	jogar_novamente = input("Jogar novamente (y/n): ")
	if jogar_novamente.lower() != "y":
		break
print( Fore.YELLOW + "Tchau !!")