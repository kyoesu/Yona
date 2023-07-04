import numpy as np 
import tensorflow as tf 
import pickle

#print(tf.__version__)


def download_words():
    import requests

    response = requests.get('https://raw.githubusercontent.com/danakt/russian-words/master/russian.txt')

    text = response.content.decode('cp1251')
    #print(text)
    '''with open('gpt/russian1.txt', 'w') as ru:
        ru.write(text.encode('utf-8'))'''
    return text


def code_text(text):
    texts=[]
    ch=False
    i1=0
    '''with open('gpt/russian.txt', 'r') as ru:
        text = ru.read()'''
    for i in range(len(text)):
        '''if text[i]=="":
            i1=i
        el'''
        #print(text[i])
        if text[i]=="\n":
            i2=i
            ch=True
        if ch:
            texts.append(text[i1:i2])
            i1=i2+1
            ch=False
    
    tokenizer=tf.keras.preprocessing.text.Tokenizer()

    #texts=["exampe1","ex2","ex"]
    tokenizer.fit_on_texts(texts)
    with open ("gpt/tokenizer.pkl", "wb") as f:#запись в файл
        pickle.dump(tokenizer, f)
    return tokenizer

def encode_message(mess, tokenizer):
    '''
    tokenizer=tf.keras.preprocessing.text.Tokenizer()
    with open("gpt/tokenizer.pkl", "rb") as f:
        tokenizer=pickle.load(f)'''
    #tokenizer=tokenizer.load("tokenizer.h5")
    encoded_text=tokenizer.texts_to_sequences([mess])

    return(encoded_text)

def decoded_message(mess, tokenizer):
    '''tokenizer=tf.keras.preprocessing.text.Tokenizer()
    tokenizer=tokenizer.load("tokenizer.h5")'''
    decoded_text=tokenizer.sequences_to_texts([[mess]])

    return(decoded_text)

# Функция для выбора действия на основе текущего состояния 
def choose_action(state, model): 
    logits = model.predict(state) 
    action = np.argmax(logits) 
    return action 

def execute_action(action):
    done=False
    print (action)
    q=input ("оценка: ")
    if q=="end":
        done=True
        reward=-1
    else:
        reward=int(q)
        print(reward-5)

    return reward, done



def create_model(hidden_units, vocab_size):
    

    # Создаем модель рекуррентной нейронной сети 
    '''model = tf.keras.Sequential([ 
        tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=hidden_units), 
        tf.keras.layers.GRU(units=hidden_units), 
        tf.keras.layers.Dense(units=vocab_size, activation='softmax') 
    ]) '''
    model = tf.keras.Sequential([ 
        tf.keras.layers.Embedding(input_dim=vocab_size, output_dim=hidden_units), 
        tf.keras.layers.GRU(units=hidden_units, return_sequences=True), 
        tf.keras.layers.GRU(units=hidden_units), 
        tf.keras.layers.Dense(units=vocab_size, activation='softmax') ])
    

    return model




def training_model(model, num_epochs, hidden_units, tokenizer):
    
    
    '''with open("gpt/tokenizer.pkl", "rb") as fil:
        tokenizer=pickle.load(fil) #загрузка словаря'''


    # Определяем функцию потерь и оптимизатор 
    loss_fn = tf.keras.losses.SparseCategoricalCrossentropy() 
    optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)

    # Цикл обучения 
    for epoch in range(num_epochs): 
        # Инициализируем состояние
        state = np.zeros((1, hidden_units)) 
        total_reward = 0 
        done=False
        while not done: 
            # Получаем сообщение от пользователя 
            message = input("Ваше сообщение: ") 
            
            # Кодируем сообщение в числовое представление 
            encoded_message = encode_message(message, tokenizer) 
            
            # Получаем действие от модели 
            action = choose_action(encoded_message, model)#numpy.int64

            # Выполняем действие и получаем награду 
            #action2=[action,590243]#+мяу
            action1=decoded_message(action, tokenizer)#преобразование в текст
            reward, done = execute_action(action1) 
            total_reward += reward 
            
            # Обновляем состояние модели 
            next_state = np.concatenate([state, encoded_message], axis=1) 
            
            # Обновляем модель через обучение с подкреплением 
            with tf.GradientTape() as tape: 
                logits = model(next_state, training=True) 
                loss_value = loss_fn(action, logits) 
            grads = tape.gradient(loss_value, model.trainable_variables) 
            optimizer.apply_gradients(zip(grads, model.trainable_variables)) 
            
            # Переходим к следующему состоянию 
            state = next_state 
        
        print(f"Эпоха {epoch + 1}: Награда = {total_reward}")
    return model



# Задаем гиперпараметры 
learning_rate = 0.001 
num_epochs = 3
hidden_units = 128 
vocab_size=1532630


tokenizer=code_text(download_words())

model=create_model(hidden_units,vocab_size)

model=training_model(model, num_epochs, hidden_units, tokenizer)

model.save("gpt/gpt_zero_model.h5")


#loaded_model=tf.keras.models.load_model("gpt_zero_model.h5")

