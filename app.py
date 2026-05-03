from colorama import Fore, Style

# Lista para armazenar as situações
situacoes = [
    "Muito baixo (crítico)", 
    "Baixo", 
    "Médio", 
    "Alto", 
    "Muito alto (alerta)"
]

# Função
def mostrar_nivel(nivel):
    if nivel == 1:
        print(Fore.RED + f"Nível 1: {situacoes[0]}")
    elif nivel == 2:
        print(Fore.YELLOW + f"Nível 2: {situacoes[1]}")
    elif nivel == 3:
        print(Fore.GREEN + f"Nível 3: {situacoes[2]}")
    elif nivel == 4:
        print(Fore.CYAN + f"Nível 4: {situacoes[3]}")
    elif nivel == 5:
        print(Fore.BLUE + f"Nível 5: {situacoes[4]}")
    
    # Resetar o estilo
    print(Style.RESET_ALL)

# Simulação
print("Monitoramento de Reservatório")
mostrar_nivel(1)
mostrar_nivel(2)
mostrar_nivel(3)
mostrar_nivel(4)
mostrar_nivel(5)