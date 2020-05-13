from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from csvfactory import CsvFactory

class Bot:

    def __init__(self, name, acurrency):
        self.name = name
        self.acurrency = acurrency
        self.bot = ChatBot(name)

    def training_array(self, speaking):
        self.trainer = ListTrainer(self.bot)
        self.trainer.train(speaking)

    def training_csv(self, path):
        csv = CsvFactory(path)
        list = csv.to_array()

        self.trainer = ListTrainer(self.bot)
        self.trainer.train(list)
        

    def response(self, question):
        answer = self.bot.get_response(question)
        text = self.name + ': Eita, não entendi.'
    
        if float(answer.confidence) > self.acurrency:
            text = self.name + ': ' + str(answer)
            
        print("Precisão: ", answer.confidence)
        return text
    