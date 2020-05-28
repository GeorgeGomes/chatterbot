from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from csvfactory import CsvFactory
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

class Bot:

    def __init__(self, name, acurrency):
        self.name = name
        self.acurrency = acurrency
        self.bot = ChatBot(name)
        # Salva as perguntas e respostas do usuário
        self.fulltext = 'Você gosta de cozinhar?'

    # Faz o treino em array
    def training_array(self, speaking):
        self.trainer = ListTrainer(self.bot)
        self.trainer.train(speaking)

    # Faz o treino em csv
    def training_csv(self, path):
        csv = CsvFactory(path)
        list = csv.to_array()

        self.trainer = ListTrainer(self.bot)
        self.trainer.train(list)

    # Exporta o treino do banco de dados
    def export_train(self):
        self.trainer.export_for_training('./my_export.json')

    def add_model(self, path, rows):
        csv = CsvFactory(path)
        csv.write(rows)

    #### Acuracia Naive Bayes #####
    def get_accuracy(self, path):
        dataset = pd.read_csv(path, sep=';', encoding = "ISO-8859-1")
        
        token = RegexpTokenizer(r'[a-zA-Z0-9]+')
        cv = CountVectorizer(analyzer='word', lowercase=True, stop_words='english', min_df=1, ngram_range = (1,1), tokenizer = token.tokenize)
        text_counts = cv.fit_transform(dataset['Text'])

        # Aqui começa o treinamento
        y = dataset['Sentiment']
        X = text_counts
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)
        
        NaiveB = MultinomialNB()
        NaiveB.fit(X_train, y_train)

        y_pred_test_NaiveB= NaiveB.predict(X_test)

        #retorno 
        print('Acurácia NaiveBayes:',metrics.accuracy_score(y_test, y_pred_test_NaiveB))

    # Resposta do robo
    def response(self, question):
        answer = self.bot.get_response(question)
        text = 'Eita, não entendi.'
    
        if float(answer.confidence) > self.acurrency:
            # acumulador para salvar no futuro modelo
            self.fulltext += ' ' + question + ' ' + str(answer)
            text = str(answer)
            
        return text
