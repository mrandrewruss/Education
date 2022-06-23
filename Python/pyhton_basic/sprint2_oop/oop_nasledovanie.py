class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    def show(self):
        print(f'{self.name} ({self.phone})')
        
#Обьявляем Friend класс, дочерним к User
class Friend(User):
    # пишем конструктор класса-наследника, чтобы он принимал все нужные параметры
    def __init__(self, name, phone, address):   
        super().__init__(name, phone)
        # наследуем функциональность конструктора из класса-родителя
        self.address = address
        # добавляем новую функциональность: свойство address
    def show(self):
        print(f'Имя: {self.name} || Телефон: {self.phone} || Адрес: {self.address}')
        
#создаем обьекты User и Friend
father = User("Отец", "+1 223 342 45")
son = Friend("Сын", "+1 234 234 33", "Екб")

father.show()
son.show()
