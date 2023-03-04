from flask import Flask, render_template, request
from utils import db, openai

# Flask
app = Flask(__name__, static_folder='templates')
app.config['DEBUG'] = True

conversations = []

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
        conversations.append(question)

        answer = openai.get_answer(question)
        conversations.append(answer)

        db.insert_answer(question, answer)

        return render_template('index.html', chat=conversations)
    else:
        return render_template('index.html')


@app.route('/list', methods=['GET'])
def list_answers():
    """
    Function that returns the DDBB classified in questions and answers.
    No Parameters needed, just the endpoint.
    """
    rows = db.get_answers()
    
    return render_template('list.html', rows=rows)

app.run(host='0.0.0.0')