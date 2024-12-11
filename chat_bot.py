import os
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_PT.UTF-8')

def obter_resposta(texto: str) -> str:
    comando: str = texto.lower()

    # if comando in ('olá', 'boa tarde', 'bom dia'):
    #     return 'Olá tudo bem!'
    # if comando == 'como estás':
    #     return 'Estou bem, obrigado!'
    # if comando == 'como te chamas':
    #     return 'O meu nome é: Bot :)'
    # if comando == 'tempo':
    #     return 'Está um dia de sol!'
    # if comando in ('bye', 'adeus', 'tchau'):
    #     return 'Gostei de falar contigo! Até breve...'
    # if 'horas' in comando:
    #     return f'São: {datetime.now():%H:%M} horas'
    # if 'data' in comando:
    #     return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    # return f'Desculpa, não entendi a questão! {texto}'

    respostas = {
        ('olá', 'boa tarde', 'bom dia'): 'Olá tudo bem!',
        'como estás': 'Estou bem, obrigado!',
        'como te chamas': 'O meu nome é: Bot :)',
        'tempo': 'Está um dia de sol!',
        ('que horas são', 'horas'): f'São: {datetime.now():%H:%M} horas',
        ('data', 'dia'): f'Hoje é dia: {datetime.now():%d-%m-%Y}',
        ('que dia da semana é hoje?', 'dia da semana'): f'Hoje é {datetime.now().strftime("%A")}.',
        ('faltam quantos dias para o natal?', 'dias para o natal'): dias_para_o_natal(),
        ('bye', 'adeus', 'tchau'): 'Gostei de falar contigo! Até breve...'
    }

    for chave, resposta in respostas.items():
        if isinstance(chave, tuple):
            if comando in chave:
                return resposta
        elif chave in comando:
            return resposta

    if 'horas' in comando:
        return f'São: {datetime.now():%H:%M} horas'

    if 'data' in comando:
        return f'Hoje é dia: {datetime.now():%d-%m-%Y}'

    return f'Desculpa, não entendi a questão! {texto}'

def dias_para_o_natal():
    hoje = datetime.now()
    natal = datetime(hoje.year, 12, 25)
    if hoje > natal:
        natal = datetime(hoje.year + 1, 12, 25)
    dias_faltando = (natal - hoje).days
    return f'Faltam {dias_faltando}'

def chat() -> None:
    print('Bem-vindo ao ChatBot!')
    print('Escreva "bye" para sair do chat')
    name: str = input('Bot: Como te chamas? ')
    print(f'Bot: Olá, {name}! \n Como te posso ajudar?')

    while True:
        user_input: str = input('Tu: ')
        resposta: str = obter_resposta(user_input)
        print(f'Bot: {resposta}')

        if resposta == 'Gostei de falar contigo! Até breve...':
            break

    print('Chat acabou')
    print()


def main() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')
    chat()


if __name__ == '__main__':
    main()
