"""
Crie um programa que leia o nome, ano de nascimento e
carteira de trabalho de uma pessoa.
Cadastre-a (com idade) em um dicionário.
Se por acaso, a CTPS for diferente de ZERO, o dicionário
receberá também o ano de contratação e o salário.
Calcule a crescente, além da idade com quantos anos a pessoa vai
se aposentar """

from datetime import datetime

pessoa = dict()
# GUARDANDO TODOS OS DADOS DENTRO NO DICIONÁRIO PESSOAS ------------------------------------------------
pessoa['Nome'] = str(input('Digite seu nome:'))
pessoa['ano_de_nascimento'] = int(input('Digite o ano em que nasceu:'))
pessoa['CTPS'] = int(input('Digite o numero da sua CTPS: (0 se não tiver):'))


# CALCULANDO A IDADE DA PESSOA --------------------------------------------------------------------------
idade_atual = datetime.now().year - pessoa['ano_de_nascimento']
pessoa['idade_atual'] = datetime.now().year - pessoa['ano_de_nascimento']


# CRIANDO UMA CONDIÇÃO ----------------------------------------------------------------------------------
if pessoa['CTPS'] != 0:
    pessoa['ano_contratacao'] = int(input('Em que ano você foi contratado:'))
    pessoa['salario'] = float(input('Digite o seu salário R$'))


    # CALCULANDO A APOSENTADORIA -----------------------------------------------------------------------
    idade_aposentadoria = 65
    anos_trabalhados = datetime.now().year - pessoa['ano_contratacao']
    anos_restantes = idade_aposentadoria - pessoa['idade_atual']
    aposentadoria = idade_atual + (pessoa['ano_contratacao'] + 35) - datetime.now().year

    if anos_restantes <= 0:
        print('Você já pode se aposentar')
    else:
        print(f'Você irá se aposentar em: {datetime.now().year + anos_restantes}', end=' ')
        print(f'Com {aposentadoria} anos ')

    # EXIBINDO RESULTADO FINAL ------------------------------------------------------------------------
    print('_______ Relatoório _________')
    for dado_da_pessoa, valor_obtido in pessoa.items():
        print(f'- {dado_da_pessoa}: {valor_obtido}')

else:
    print('Você ainda não tem uma carteira de trabalho')