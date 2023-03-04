# ChatGPT API

## An API to connect with ChatGPT

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
The objective of this project is to provide an application that connects directly with OpenAI and give answers to the questions of the user. 

### Initial Steps
-------------
To start with our application, you will need a few things first.
First of all, you will need an API key from OpenAI. You can get it from [OpenAI](https://openai.com/product).
After that, you could also save your questions and answers in a Cloud based database such as AWS. If you want that, you will also need to register in [AWS](https://aws.amazon.com/)
Once you register, you need to create a database in RDS and there, you will get a username, a chosen password, the BBDD host and port.
We eased it up so the user can enter all those keys in a .env file(You can find a template in sample.env) and our app will get the keys from there.  

And one last thing will be the use of Docker (in case you want a virtual environment). We also provide with a Docker file so you can launch our app there. The steps are quite simple. First, you will need to get the file.
```
docker pull 3moya/gpt3-answers
```
And after that, with the Docker Desktop app running, you will need to enter the following command.

PowerShell:
```sh
docker run -d -t `
    --name gpt-answers `
    -p 5000:5000 `
    -e "OPENAI_KEY=<openai-key>" `
    -e "DB_USERNAME=<db-username>" `
    -e "DB_PASSWORD=<db-password>" `
    -e "DB_HOST=<db-host>" `
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
The functionality of our app is similar to ChatGPT. You can type anything you want and it will return a response. Our added functionality is that every time the user asks something, it will register in an AWS BBDD so you could retrieve your logs anytime you want.  

### Future Improvements
-------------
- Improve the interface.
- Add a functionality that integrates XXX
- Integration in a web environment(ex. Pythonanywhere)

### Collaborators
-------------
- [Nicolás Eyzaguirre](https://github.com/NicolasEyzaguirre)
- [Enrique Moya](https://github.com/3Moya)
- [Javi López](https://github.com/javlopsan)
- [Kyung Min Ohn](https://github.com/exAdun)  

### Sources
-------------
Project made with:
- Python 3.7.4
- OpenAI
- AWS