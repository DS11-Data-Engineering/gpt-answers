from flask import Flask, render_template, request
import pymysql
import openai
import os

# Openai key
openai.api_key = os.getenv('OPENAI_KEY')

# Flask
app = Flask(__name__, static_folder='templates')
app.config['DEBUG'] = True

# MySQL keys(AWS)
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')

conversations = []

# To connect with the Cloud DDBB
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
    """
    Basic function where the user asks something and returns the answer from ChatGPT. It will also save it in the Cloud DDBB, in this case, AWS.

    Parameters 
    ----------
    Type in the interface what you want to ask and it will return the answer.
    """
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
    """
    Function that returns the DDBB classified in questions and answers.
    No Parameters needed, just the endpoint.
    """
    cursor = db_connection()
    cursor.execute('''SELECT * FROM answers''')
    rows = cursor.fetchall()
    cursor.close()
    return render_template('list.html', rows=rows)

app.run(host='0.0.0.0')