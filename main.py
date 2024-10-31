with open('text.txt', 'r') as file: 
    cont = file.read()  #считывание файла
    words = cont.split() 
    
    print("Слов в файле: " + str(len(words)))  #длинна строки