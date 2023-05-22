


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