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

SIGNOS = [
    ("Capricórnio", (1, 1), (1, 19)),
    ("Aquário", (1, 20), (2, 18)),
    ("Peixes", (2, 19), (3, 20)),
    ("Áries", (3, 21), (4, 19)),
    ("Touro", (4, 20), (5, 20)),
    ("Gêmeos", (5, 21), (6, 20)),
    ("Câncer", (6, 21), (7, 22)),
    ("Leão", (7, 23), (8, 22)),
    ("Virgem", (8, 23), (9, 22)),
    ("Libra", (9, 23), (10, 22)),
    ("Escorpião", (10, 23), (11, 21)),
    ("Sagitário", (11, 22), (12, 21)),
    ("Capricórnio", (12, 22), (12, 31)), 
]

def obter_signo(data_nascimento: str) -> str:
    try:
        data_nascimento = datetime.strptime(data_nascimento, "%d-%m-%Y")
    except ValueError:
        return "Desculpa, não consegui entender a data. Por favor, use o formato dd-mm-aaaa."
    
    mes = data_nascimento.month
    dia = data_nascimento.day

    for signo, (mes_inicial, dia_inicial), (mes_final, dia_final) in SIGNOS:
        if (mes == mes_inicial and dia >= dia_inicial) or (mes == mes_final and dia <= dia_final):
            return f"O teu signo é {signo}."
    
    return "Não consegui determinar o teu signo."

def obter_resposta(texto: str, espera_data_nascimento=False) -> str:
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


    if 'qual é o meu signo' in comando or 'signo' in comando:
        return "Qual é a tua data de nascimento? Por favor, diga no formato dd-mm-aaaa."
    

    if espera_data_nascimento:
        return obter_signo(comando)
    

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
    return f'Faltam {dias_faltando} dias para o Natal.'

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

    espera_data_nascimento = False 

    while True:
        user_input: str = input('Tu: ')
        resposta: str = obter_resposta(user_input, espera_data_nascimento)

        if 'qual é o meu signo' in user_input or 'signo' in user_input:
            espera_data_nascimento = True
            print(f'Bot: {resposta}')
            continue

        if espera_data_nascimento:
            print(f'Bot: {resposta}')
            espera_data_nascimento = False
            continue
        
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