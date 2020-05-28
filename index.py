from bot import Bot

bot_name='Eucides'
_bot = Bot(bot_name, 0)
_bot.training_csv('training.csv')

rows = []

sentiment = 0

# Funcao que finaliza o bot e question o usuário sobre o resultado
def finished():
    end = input("A resposta foi suficiente? (s=Sim/n=Não): ")
    if(end.lower() == 's' or end.lower() == 'sim'):
        sentiment = 1
    else:
        sentiment = 0

    rows.append([_bot.fulltext, sentiment])
    print('OBRIGADO POR FAVOR VISITE O RECEITAPARADUMIES.COM.IMPACTA - As melhores receitas')
    # Adiciona no model os dados
    _bot.add_model('model.csv', rows)
    # Busca a acuracia 
    _bot.get_accuracy('model.csv')


print('Você gosta de cozinhar?')

while True:
    try:
        
        question = input("Usuário: ")
        if question.lower() == 'obrigado' or question.lower() == 'tchau' or question.lower() == 'voltar':
            finished()
            break
        
        answer = _bot.response(question)
        print(bot_name + ": " + answer)


    except(KeyboardInterrupt, EOFError, SystemExit):
        finished()
        break

