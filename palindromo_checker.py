import re

def verificar_palindromo(texto):
    """
    Verifica se um texto (palavra ou frase) é um palíndromo.

    Ignora espaços, pontuação e diferencia maiúsculas de minúsculas.

    Args:
        texto (str): A palavra ou frase a ser verificada.

    Returns:
        bool: True se for um palíndromo, False caso contrário.
    """
    # 1. Converter o texto para letras minúsculas
    texto = texto.lower()

    # 2. Remover espaços, pontuação e caracteres não alfanuméricos
    #    Usamos uma expressão regular (re.sub) para remover tudo que não é letra ou número.
    texto_limpo = re.sub(r'[^a-z0-9]', '', texto) #

    # 3. Comparar o texto limpo com sua versão invertida
    #    [::-1] é uma técnica Python para inverter strings.
    return texto_limpo == texto_limpo[::-1] #

# --- Exemplos de uso da função ---

# ESTAS SÃO AS VARIÁVEIS QUE ESTAVAM FALTANDO:
frase1 = "A Rita, tira!"
frase2 = "Socorram-me, subi no ônibus em Marrocos"
frase3 = "Roma me tem amor"
palavra1 = "Arara"
palavra2 = "Ovo"

# Exemplos que não devem ser palíndromos
frase4 = "Isso não é um palindromo"
palavra3 = "Python"

print(f"'{frase1}' é um palíndromo?")
if verificar_palindromo(frase1):
    print("Sim")
else:
    print("Não")

print(f"\n'{frase2}' é um palíndromo?")
if verificar_palindromo(frase2):
    print("Sim")
else:
    print("Não")

print(f"\n'{frase3}' é um palíndromo?")
if verificar_palindromo(frase3):
    print("Sim")
else:
    print("Não")

print(f"\n'{palavra1}' é um palíndromo?")
if verificar_palindromo(palavra1):
    print("Sim")
else:
    print("Não")

print(f"\n'{palavra2}' é um palíndromo?")
if verificar_palindromo(palavra2):
    print("Sim")
else:
    print("Não")

print(f"\n'{frase4}' é um palíndromo?")
if verificar_palindromo(frase4):
    print("Sim")
else:
    print("Não")

print(f"\n'{palavra3}' é um palíndromo?")
if verificar_palindromo(palavra3):
    print("Sim")
else:
    print("Não")

# Você pode testar com sua própria entrada:
# minha_entrada = input("\nDigite uma palavra ou frase para verificar se é um palíndromo: ")
# if verificar_palindromo(minha_entrada):
#    print("Sim")
# else:
#    print("Não")
