from bot import Bot

_bot = Bot('Eucides', 0.2)
_bot.training_csv('training.csv')

while True:
    try:
        
        question = input("Usuário: ")
        if question.lower() == 'obrigado' or question.lower() == 'tchau' or question.lower() == 'voltar':
            print('OBRIGADO POR FAVOR VISITE O RECEITAPARADUMIES.COM.IMPACTA - As melhores receitas')
            break
        
        answer = _bot.response(question)
        print(answer)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
