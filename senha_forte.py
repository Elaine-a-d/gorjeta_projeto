
def verificar_senha_forte(senha):
    """
    Verifica se uma senha é forte.

    Uma senha forte deve ter:
    - Pelo menos 8 caracteres
    - Pelo menos um número
    """
    if len(senha) < 8:
        return False, "A senha deve ter pelo menos 8 caracteres."

    tem_numero = False
    for caractere in senha:
        if caractere.isdigit():
            tem_numero = True
            break
    
    if not tem_numero:
        return False, "A senha deve conter pelo menos um número."
    
    return True, "Senha forte e válida!"

def main():
    while True:
        senha = input("Digite sua senha (ou 'sair' para finalizar): ")
        
        if senha.lower() == 'sair':
            print("Saindo do programa.")
            break
        
        eh_forte, mensagem = verificar_senha_forte(senha)
        
        if eh_forte:
            print(mensagem)
            print("Senha aceita. Programa finalizado.")
            break
        else:
            print(f"Senha inválida: {mensagem}")
            print("Tente novamente.")

if __name__ == "__main__":
    main()
    