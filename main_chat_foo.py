import numpy as np
import speech_recognition

def process_unsupervised_data(data):
    # Здесь происходит обработка данных без учителя 
    # Выполните необходимые операции для предобработки и подготовки данных 
    # Пример обработки данных: преобразование текста в числовые векторы
    
    processed_data = [] 
    for sample in data: 
        vector = text_to_vector(sample) # Функция text_to_vector преобразует текст в числовой вектор 
        processed_data.append(vector) 
        
        return processed_data
    
def text_to_vector(text): 
    # Простейший пример: преобразование текста в вектор путем подсчета частоты встречаемости символов 

    # Переводим текст в нижний регистр 
    text = text.lower() 

    # Инициализируем вектор нулями 
    vector = [0] * 50 # В примере используется алфавит из 26 символов 


    # Подсчитываем частоту встречаемости каждого символа в тексте 
    
    for char in text: 
        if char.isalpha(): 
            index = ord(char) - ord('a') # Определяем индекс символа в алфавите 
            vector[index] += 1 
            
    return vector

def calculate_weights(processed_data):
    total_weights = 0

    # Перебираем каждую обработанную запись данных
    for record in processed_data:
        # Получаем количество элементов в записи данных
        num_elements = len(record)

        # Суммируем количество элементов в записи данных
        total_weights += num_elements

    return total_weights


def load_unsupervised_data():
    # Здесь выполняется загрузка данных для обучения без учителя
    # Это может быть любой процесс, включая чтение данных из файлов, подключение к базе данных и т.д.

    # Пример загрузки данных из файла
    data = []
    with open('req/res.txt', 'r') as file:
        for line in file:
            # Обработка каждой строки данных и добавление в массив
            processed_line = process_unsupervised_data(line)
            data.append(processed_line)

    return data


def generate_next_char(hidden_state, weights):
    # Вычисляем сумму всех весов
    total_weights = sum(weights)

    # Вычисляем вероятности для каждого веса
    probabilities = [weight / total_weights for weight in weights]

    # Выбираем следующий символ на основе вероятностей
    next_char = np.random.choice(len(hidden_state), p=probabilities)

    return hidden_state[next_char]


def update_hidden_state(hidden_state, next_char):
    # Создаем новое скрытое состояние с добавлением нового символа
    updated_hidden_state = hidden_state[1:] + [next_char]
    
    return updated_hidden_state


def record_and_recognize_audio(recognizer, microphone):
    """
    Запись и распознавание аудио
    """
    with microphone:
        recognized_data = ""

        # регулирование уровня окружающего шума
        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Listening...")
            audio = recognizer.listen(microphone, 5, 5)

        except speech_recognition.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
            return

        # использование online-распознавания через Google 
        try:
            print("Started recognition...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        # в случае проблем с доступом в Интернет происходит выброс ошибки
        except speech_recognition.RequestError:
            print("Check your Internet Connection, please")

        return recognized_data