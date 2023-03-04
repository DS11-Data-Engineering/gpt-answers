from flask import Flask, render_template, request
import pymysql
import openai
import os
from dotenv import load_dotenv
load_dotenv()

# Openai
openai.api_key = os.getenv('OPENAI_KEY')

# Flask
app = Flask(__name__, static_folder='templates')
app.config['DEBUG'] = True

# MySQL
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')

conversations = []

def db_connection():
    cursor = pymysql.connect(
        host=host,
        user=username,
        password=password,
        cursorclass=pymysql.cursors.DictCursor).cursor()
    
    cursor.connection.commit()
    cursor.execute('''USE answers''')

    return cursor

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    if request.form['question']:
        
        question = request.form['question'] + ''

        answer = openai.Completion.create(
            engine='text-davinci-003',
            prompt=question,
            max_tokens=1000
        ).choices[0].text.strip()

        conversations.append(question)
        conversations.append(answer)

        cursor = db_connection()
        query = '''INSERT INTO answers (question, answer) VALUES ('%s', '%s')''' % (question, answer)
        cursor.execute(query)
        cursor.connection.commit()

        cursor.close()

        return render_template('index.html', chat = conversations)
    else:
        return render_template('index.html')


@app.route('/list', methods=['GET'])
def list_answers():
    cursor = db_connection()
    cursor.execute('''SELECT * FROM answers''')
    rows = cursor.fetchall()
    cursor.close()
    return rows #hacerlo más bonito como en html?
app.run()