import os
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_PT.UTF-8')

FERIADOS = {
    1: [1],  # Janeiro 1 - Ano Novo
    4: [25], # Abril 25 - Liberdade
    5: [1],  # Maio 1 - Dia do Trabalhador
    6: [10], # Junho 10 - Dia de Portugal
    8: [15], # Agosto 15 - Assunção de Nossa Senhora
    10: [5], # Outubro 5 - Implantação da República
    11: [1], # Novembro 1 - Dia de Todos os Santos
    12: [25], # Dezembro 25 - Natal
}

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
        
    if 'feriados no mês' in comando or 'quantos feriados' in comando:
        return feriados_no_mes_atual()

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

def feriados_no_mes_atual():
    hoje = datetime.now()
    mes_atual = hoje.month

    if mes_atual in FERIADOS:
        feriados_mes = FERIADOS[mes_atual]
        return f'No mês {hoje.strftime("%B")}, existem {len(feriados_mes)} feriado(s): {", ".join(str(f) for f in feriados_mes)}.'
    else:
        return f'No mês {hoje.strftime("%B")}, não há feriados conhecidos.'

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
