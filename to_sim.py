
def convert_to_numeric(text,dictionary): #dictionary в файле tg/secr
    result = []
    for char in text:
        if char in dictionary:
            result.append(dictionary[char])
        else:
            result.append("999")
    return result


#print (convert_to_numeric("привет "))