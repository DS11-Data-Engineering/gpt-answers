import pymysql
import os

# To connect with the Cloud DDBB
def __connection():
    connection = pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD'),
        cursorclass=pymysql.cursors.DictCursor)
    
    cursor = connection.cursor()
    
    cursor.connection.commit()
    cursor.execute('''USE answers''')

    return connection

def insert_answer(question: str, answer: str) -> bool:
    cursor = __connection().cursor()
    query = '''INSERT INTO answers (question, answer) VALUES ('%s', '%s')''' % (question, answer)
    cursor.execute(query)
    cursor.connection.commit()
    cursor.close()

def get_answers():
    cursor = __connection().cursor()
    cursor.execute('''SELECT * FROM answers''')
    rows = cursor.fetchall()
    cursor.close()

    return rows