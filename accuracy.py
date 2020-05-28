# Bibliotecas padrão  e carga de dados
import pandas as pd
dataset = pd.read_csv('accuracy.csv', sep=';') 

#------------------------------------------------------------------------------------------
# Processamento do Texto
# https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html
#------------------------------------------------------------------------------------------
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
token = RegexpTokenizer(r'[a-zA-Z0-9]+') # Expressão regular para remover simbolos
cv = CountVectorizer(   analyzer='word',lowercase=True, stop_words='english',min_df=1,
                        ngram_range = (1,1), tokenizer = token.tokenize)
text_counts = cv.fit_transform(dataset['Text'])
# print(cv.vocabulary_)

##------------------------------------------------------------
## Tratamento do alvo para rodar (inclusive) Regressão Linear
##------------------------------------------------------------
dataset['Sentiment']   = [1 if x == 'Positivo' else 0 for x in dataset['Sentiment']]


##------------------------------------------------------------
## Separa os dados em treinamento e teste
##------------------------------------------------------------
y = dataset['Sentiment']   # Carrega alvo
X = text_counts            # Carrega as colunas geradas
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

#---------------------------------------------------------------------------
## Ajusta modelo Naive Bayes, Árvore e Regressão Linear com treinamento 
#---------------------------------------------------------------------------
# Naive Bayes
from sklearn.naive_bayes import MultinomialNB
NaiveB = MultinomialNB()
NaiveB.fit(X_train, y_train)

# Árvore de Decisão
from sklearn.tree import DecisionTreeClassifier
dtree = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
dtree.fit(X_train, y_train)

# Regressão linear 
from sklearn.linear_model import LinearRegression
LinearReg = LinearRegression()
LinearReg.fit(X_train, y_train)


#---------------------------------------------------------------------------
## Previsão usando os dados de teste
#---------------------------------------------------------------------------
y_pred_test_NaiveB= NaiveB.predict(X_test)  # Naive Bayes
y_pred_test_Tree= dtree.predict(X_test)     # Árvore de Decisão
y_pred_test_RLin= LinearReg.predict(X_test) # Regressão linear 



#---------------------------------------------------------------------------
## Cálcula e mostra a Acurácia dos modelos
#---------------------------------------------------------------------------
from sklearn import metrics
print()
print('----------------------------------------------------------')
print('Acurácia NaiveBayes:',metrics.accuracy_score(y_test, y_pred_test_NaiveB))
print('Acurácia Árvore:',metrics.accuracy_score(y_test, y_pred_test_Tree))
print('Acurácia Regressão Linear:',metrics.accuracy_score(y_test, [1 if x > 0.5 else 0 for x in y_pred_test_RLin]))
print('----------------------------------------------------------')