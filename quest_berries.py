import datetime as dt
import time

class Quest:
    def __init__(self, name, description, goal):
        self.name = name
        self.description = description
        self.goal = goal
        self.start_time = None
        self.end_time = None

    def accept_quest(self):
        if self.end_time:
            return 'С этим испытанием вы уже справились.'
        self.start_time = dt.datetime.now()
        return f'Начало квеста "{self.name}" положено.'

    def pass_quest(self):
        if not self.start_time:
            return 'Нельзя завершить то, что не имеет начала!'
        self.end_time = dt.datetime.now()
        completion_time = self.end_time - self.start_time
        return (f'Квест "{self.name}" окончен.'
                f' Время выполнения квеста: {completion_time}')

    def __str__(self):
        if self.end_time:
            return (f'Цель квеста {quest_name} — {quest_goal}. Квест завершён.')
        if self.start_time:
            return (f'Цель квеста {quest_name} — {quest_goal}. Квест выполняется.')
        return (f'Цель квеста {quest_name} — {quest_goal}.')



quest_name = 'Сбор пиксельников'
quest_goal = 'Соберите 12 ягод пиксельников.'
quest_description = '''
В древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельников.'''

new_quest = Quest(quest_name, quest_description, quest_goal) 

print(new_quest.pass_quest())
print(new_quest.accept_quest())
time.sleep(3)
print(new_quest.pass_quest())
print(new_quest.accept_quest())

# Печатаем объекта класса Quest:
print(new_quest)