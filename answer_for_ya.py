class Human:
    def __init__(self, name):
        self.name = name
    # ответ по умолчанию для всех одинаковый, можно 
    # доверить его родительскому классу
    
    
    def answer_question(self, question):
        print('Очень интересный вопрос! Не знаю.')
        
class Student(Human):
    #  метод ask_question() принимает параметр someone:
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос; 
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question
    def ask_question(self, someone, question):
        self.someone = someone
        self.question = question
        # напечатайте на экран вопрос в нужном формате
        print(f'{someone.name}, {self.question}')
        # запросите ответ на вопрос у someone
        someone.answer_question(question)
        print()  # этот print выводит разделительную пустую строку  
class Curator(Human):
    def __init__(self, name):
        super().__init__(name)
        
    def answer_question(self, question):
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        # если да - ответить на него
        # если нет - вызвать метод answer_question() у родительского класса
        if question == 'мне грустненько, что делать?':
            return print(f'Держись, всё получится. Хочешь видео с котиками?')
        else:
            return super().answer_question(question)
    # объявите и реализуйте классы CodeReviewer и Mentor
class Mentor(Human):
    def __init__(self, name):
        super().__init__(name)
    def answer_question(self, question):
        if question == 'мне грустненько, что делать?':
            return print(f'Отдохни и возвращайся с вопросами по теории.')
        elif question == 'как устроиться работать питонистом?':
            return print(f'Сейчас расскажу.')
        else:
            return super().answer_question(question)
class CodeReviewer(Human):
    def __init__(self, name):
        super().__init__(name)
    def answer_question(self, question):
        if question == 'что не так с моим проектом?':
            return print(f'О, вопрос про проект, это я люблю.')
        else:
            return super().answer_question(question)
# следующий код менять не нужно, он работает, мы проверяли
student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')
student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')