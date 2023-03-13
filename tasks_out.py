from bot import bot
import random
import re

min_lavel = 800
max_lavel = 3500
def comlexiti(number):
    if (min_lavel <= number <= max_lavel) and (number % 100 == 0):
        tasks = []
        list_task = []
        list_tasks = bot.get_topic(number)
        tasks.append(random.sample(list_tasks, 10))
        for i in tasks:
            for k in i:
                list_task.append(list(k))
        for task in list_task:
            task[3] = task[3].splitlines()
            new_str = ''
            for i in task[3]:
                if i != '':
                    new_str += i.lstrip().rstrip() + ' '
            task[3] = new_str
            task.pop(0)
        return list_task
    
    else:
        return('Вы написали неверное число с:')
