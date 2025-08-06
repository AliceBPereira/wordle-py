import random
import requests
from rich.console import Console

console = Console()

try:
    url = "https://raw.githubusercontent.com/pythonprobr/palavras/master/palavras.txt"
    resposta = requests.get(url)
    todas_as_palavras = resposta.text.splitlines()
    # Filtra apenas palavras com 5 letras e sem hífens/números
    banco_de_dados = [p.lower() for p in todas_as_palavras if len(p) == 5 and p.isalpha()]
    print(f"Banco de dados online carregado com {len(banco_de_dados)} palavras!")
except Exception as e:
    print("Falha ao carregar banco de dados online. Usando lista de emergência.")
    print(f"Erro: {e}")
    banco_de_dados = ['rosas', 'ratos', 'peixe', 'sucos', 'ideia', 'livro']

def escolher_palavra_aleatoria():
    return random.choice(banco_de_dados)

def receber_palavra():
    while True:
        palavra = input("Digite uma palavra: ").strip().lower()
        if len(palavra) == 5:
            return palavra
        else:
            print("A palavra deve ter exatamente 5 letras. Tente novamente.")

def verificar_caracteres(palavra_secreta, palavra_usuario):
    tentativa= ""
    for i in range(5):
        if palavra_usuario[i] == palavra_secreta[i]:
            tentativa += f"[bold white on green] {palavra_usuario[i].upper()} [/]"
        elif palavra_usuario[i] in palavra_secreta:
            tentativa += f"[bold white on yellow] {palavra_usuario[i].upper()} [/]"
        else:
            tentativa += f"[on #666666] {palavra_usuario[i].upper()} [/]"
    return tentativa

def jogar(palavra_secreta):
    i = 0
    tentativas = ['[on #666666] _ [/]' * 5 for i in range(5)]
    for t in tentativas:
            console.print(t)
    while i < 5:
        palavra_usuario = receber_palavra()
        tentativa = verificar_caracteres(palavra_secreta, palavra_usuario)
        console.clear()
        for t in tentativas:
            tentativas[i]= tentativa
        for t in tentativas:
            console.print(t)
        if palavra_usuario == palavra_secreta:
            print(f"Parabéns! Você acertou a palavra! {palavra_secreta.upper()}")
            return True
        else:
            print("Palavra incorreta. Tente novamente.")
        i += 1
            
    print("Você esgotou suas tentativas. A palavra era:", palavra_secreta)
    return False

if __name__ == "__main__":
    jogar(escolher_palavra_aleatoria())