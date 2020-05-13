from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import csv

class CsvFactory:

    def __init__(self, path):
        self.path = path

    def to_array(self):
        my_list = list()
        with open(self.path, newline='') as csvfile:
            next(csvfile)
            spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in spamreader:
                for column in row:
                    my_list.append(column)
                
            print(my_list)
            return my_list



