# класс обробтки запроса, и вывода ответа 

class Type_pharse():
    def __init__(self,request,response):
        # Список фраз на которые бот будет откликается
        self.request = request 
        # Функция ответа
        self.response = response
# Список всех команд для бота
pharse_list = []
