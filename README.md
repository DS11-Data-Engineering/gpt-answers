# *ChatGPT* API

## An API to connect with *ChatGPT*

![answers](/media/answer.jpg)  

[![Powered by NumFOCUS](https://img.shields.io/badge/powered%20by-TheBridge-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](https://www.thebridge.tech/) ![Powered by NumFOCUS](https://img.shields.io/badge/Contributors-4-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)  

### Table of Contents  
[Intro](#Intro)  
[Initial Steps](#Initial-Steps)  
[Usage](#Usage)   
[Final Thoughts](#Final-Thoughts)
[Collaborators](#Collaborators)  
[Sources](#Sources)  

### Intro
-------------
The objective of this project is to provide an application that connects directly with *OpenAI* and give answers to the questions of the user. Everything is recorded in a DDBB automatically. 

### Initial Steps
-------------
To start with our application, you will need a few things first.
First of all, you will need an API key from *OpenAI*. You can get it from [*OpenAI*](https://openai.com/product).  
After that, you could also save your questions and answers in a Cloud based database such as AWS. If you want that, you will also need to register in [*AWS*](https://aws.amazon.com/).
Once registered, the user will have to create a database in RDS and there, it will get a chosen username and password, the BBDD host and port. If you don't want to touch our app code, the database must be named 'answers' and you will need to create a table like this:  
```
create_table = '''
CREATE TABLE answers (
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    question TEXT,
    answer TEXT,
    primary key (date))
'''
cursor.execute(create_table)
```  

And one last thing will be the use of [*Docker*](https://www.docker.com/) (in case you want a virtual environment). We also provide two *Docker* files so you can launch our app there. One is the file we used for development and the other one is for users. The steps to follow are quite simple, with the *Docker Desktop* app running, you will need to enter the following command. Remember to fill the previously mentioned keys and additional info.  

PowerShell:
```sh
docker run -d -t `
    --name gpt-answers `
    -p 5000:5000 `
    -e "OPENAI_KEY=<openai-key>" `
    -e "DB_USERNAME=<db-username>" `
    -e "DB_PASSWORD=<db-password>" `
    -e "DB_HOST=<db-host>" `
    -e "DB_PORT=<db-port>" `
    3moya/gpt-answers
```

Bash:
```sh
docker run -d -t \
    --name gpt-answers \
    -p 5000:5000 \
    -e "OPENAI_KEY=<openai-key>" \
    -e "DB_USERNAME=<db-username>" \
    -e "DB_PASSWORD=<db-password>" \
    -e "DB_HOST=<db-host>" \
    -e "DB_PORT=<db-port>" \
    3moya/gpt-answers
```
### Usage
-------------
The functionality of our app is similar to *ChatGPT*. You can type anything you want and it will return a response. Our added functionality is that every time the user asks something, it will register in an AWS BBDD so you could retrieve your logs anytime you want.  
The default endpoint will receive the question and give *ChatGPT*'s answer. The endpoint */list* will show all the logged questions.

### Future Improvements
-------------
- Improve the interface.
- Add a functionality that shows the previous logs, without the need of another endpoint. In case of implementation, we would like to add another functionality that allows the user to create a new chat without records to start fresh.
- Integration in a web environment (ex. [*Pythonanywhere*](https://www.pythonanywhere.com)) or more *AWS* features ([Elastic Beanstalk](https://aws.amazon.com/en/elasticbeanstalk/)).

### Collaborators
-------------
- [Nicolás Eyzaguirre](https://github.com/NicolasEyzaguirre)
- [Enrique Moya](https://github.com/3Moya)
- [Javier López](https://github.com/javlopsan)
- [Kyung Min Ohn](https://github.com/exAdun)  

### Sources
-------------
Project made with:
- Python 3.7.4 
- OpenAI
- AWS
- Docker