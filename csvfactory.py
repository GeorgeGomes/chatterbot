from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import csv

class CsvFactory:

    def __init__(self, path):
        self.path = path

    def to_array(self):
        my_list = list()
        with open(self.path, newline='', encoding="ISO-8859-1") as csvfile:
            next(csvfile)
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in spamreader:
                for column in row:
                    my_list.append(column)
                
            print(my_list)
            return my_list

    # Salvar o resultado de perguntas e resposta no novo modelo csv para analisar a acuracia 
    def write(self, rows):
        with open(self.path, 'a', newline='', encoding="ISO-8859-1") as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            
            for row in rows:
                writer.writerow(row)

