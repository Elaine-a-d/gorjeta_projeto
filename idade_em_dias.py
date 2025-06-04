
# Importa o módulo datetime para obter o ano atual
from datetime import datetime

def calcular_idade_em_dias(ano_nascimento):
    """
    Calcula a idade de uma pessoa em dias, baseada no ano de nascimento.
    Considera 365 dias por ano para simplificação (não considera anos bissextos).

    Args:
        ano_nascimento (int): O ano de nascimento da pessoa.

    Returns:
        int: A idade aproximada da pessoa em dias.
    """
    ano_atual = datetime.now().year
    
    idade_em_anos = ano_atual - ano_nascimento
    
    # Considera 365 dias por ano para simplificação
    idade_em_dias = idade_em_anos * 365
    
    return idade_em_dias

def main():
    while True:
        try:
            # Pede o ano de nascimento ao usuário
            ano_nascimento_str = input("Digite o ano de nascimento (ex: 1990) ou 'sair' para finalizar: ")

            if ano_nascimento_str.lower() == 'sair':
                print("Saindo do programa.")
                break

            ano_nascimento = int(ano_nascimento_str)

            # Validação básica para o ano de nascimento
            ano_atual = datetime.now().year
            if ano_nascimento <= 0 or ano_nascimento > ano_atual:
                print(f"Ano de nascimento inválido. Por favor, digite um ano entre 1 e {ano_atual}.")
                continue

            idade_dias = calcular_idade_em_dias(ano_nascimento)
            print(f"A idade aproximada em dias é: {idade_dias} dias.")
            print("-" * 30) # Linha separadora para a próxima execução ou saída

        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para o ano.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
    