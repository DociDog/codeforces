import psycopg2

class BotDB:

    def __init__(self):
        """Инициализируем соеденение с БД"""
        self.conn = psycopg2.connect(dbname="codeforces_db", user="postgres", password="915890", host="127.0.0.1", port="5432")
        self.cursor = self.conn.cursor()

    def tasks_exists(self, tasks_id):
        """Проверяем уникальность номера таски в БД"""
        data =[tasks_id]
        self.cursor.execute("SELECT tasks_id FROM tasks WHERE tasks_id = %s", data)
        return bool(len(self.cursor.fetchall()))

    def add_data_tasks(self, tasks_id, complexity, tasks_name_topic, solutions):
        """Создаем запись данных о задаче"""
        data = [tasks_id, complexity, tasks_name_topic, solutions]
        self.cursor.execute("INSERT INTO tasks (tasks_id, complexity, tasks_name_topic, solutions) VALUES(%s, %s, %s, %s)", data)
        print('Данные добавлены')
        return self.conn.commit()
    
    def get_topic(self, complexity):
        """Получаем topic в БД по теме"""
        self.cursor.execute("SELECT * FROM tasks WHERE complexity = %s", (complexity, ))
        return self.cursor.fetchall()
    
    def close(self):
        """Закрытие БД"""
        self.conn.close()

#bot = BotDB()
#print(bot.get_topic('1000'))