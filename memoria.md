# Intro
The project started with the team splitting tasks between the members. Enrique and Javier took care of the main code, Nicolás was in charge of Docker and Kyung Min researched about the AWS DDBB and html.  

The first day of the project, we ended up having a functional code so we could focus on Docker and adding improvements the second day.
Docker proved to be a little bit more difficult since it had some compatibility issues while installing libraries. In the end, we made it by installing just the key libraries on an alpine environment.  
>openai==0.26.5
>Flask==2.2.2
>PyMySQL==1.0.2
>gunicorn==20.1.0
>setuptools==65.5.1  

In the final day, we focused on refining our Github and adding a proper memory and readme files.
We will explain in detail what we did in every section of this document.

# html
We started the project trying to make an interface similar to ChatGPT, that's why our main interface resembles their main page. Most of our team had little knowledge of html so we imported simple templates that gave us a decent look while giving us the flexibility to adapt our code to it.
The second html (list) was an added functionality in the last moment but it was simple enough to implement it on time. It's a simple display of all of our logs stored in our database.

# Database
To create the database in AWS, we simply followed the steps in the class guide. The section in AWS to create a DDBB is RDS. There, the user can create a database clicking in the big orange button with just a few adjustments in the parameters. 
The main ones were:
- Changing the Engine options to **MySQL**.
- Changing the Templates to the free one.
- Optional: You can change the name in DB instance identifier.
- Change in the username and creation of the password.
- Optional: In the "Assign Storage" option, you can change the capacity.  

After waiting a few minutes to let the service create our database, we will need to change one thing to allow connectivity with our machine. We click in our DDBB and head into **Security>Entry Rules** to create a new line with IPv4 that allows any traffic with origin (0.0.0.0/0).  
![IPv4](/media/ipv4.png)  
Once we have it running, we need to create a table to store our prompts. We decided to use dates as our index and primary keys, and all questions and answers as TEXT.
After that, we are all set up to use our DDBB.

# Flask


# OpenAI
The main logic was developed by OpenAI and we only accessed through their [API](https://openai.com/product). After login in, any user can get their own private key to use (make sure you copy it in a safe place). 
Our application uses ChatGPT's engine to give answers to the user questions, but keep in mind that the API key has it's limits and you could also change some parameters to improve the response.
We used the openai library and declared some constants:  

- ENGINE = We picked text-davinci-003 for efficiency/cost value.
- MAX_TOKENS = We toyed with this parameter for a while and decided that 2500 was good enough for our model.
- CONTEXT_SIZE = This parameter remembers previous questions and answers accordingly.
- PROMPT_ENGINEERING = This is additional information we give the AI so it gives us a more defined answer.  

The main function in openai.py is the one we use to create the connection between our application and OpenAI.

# Docker
- A new unprivileged user has been created as root access is not needed to run the application, and it increases security.

- There are two different Dockerfiles: one for production (`Dockerfile`) and another for development purposes (`Dockerfile_dev`). Both use different servers, with the production image using the built-in Flask development server and the production image using Gunicorn, a more suitable HTTP server for a production environment.

- Dockerfile commands have been ordered from least to most frequently changed to take advantage of caching and rebuild the images faster.

- Both images have been scanned with the command `docker scout cves`, and every vulnerability has been fixed by updating vulnerable packages to a safe version.

Once all Dockerfile parameters and commands have been established, the following commands are executed:

1. Build Docker Images:

```sh
docker build -t 3moya/gpt-answers .
```

```sh
docker build -t 3moya/gpt-answers:dev -f Dockerfile_dev .
```

2. Scanning for vulnerabilities:

```sh
docker scout cves 3moya/gpt-answers
```

```sh
docker scout cves 3moya/gpt-answers:dev
```

3. Push Docker Images to Docker Hub:

```sh
docker push 3moya/gpt-answers
```

```sh
docker push 3moya/gpt-answers:dev
```

4. Run Docker Containers:

```sh
docker run -d -t `
    --name gpt-answers `
    -p 5000:5000 `
    -e OPENAI_KEY=<openai-key> `
    -e DB_USERNAME=<db-username> `
    -e DB_PASSWORD=<db-password> `
    -e DB_HOST=<db-host> `
    3moya/gpt-answers
```

```sh
docker run -d -t `
    --name gpt-answers-dev `
    -p 5001:5000 `
    -e OPENAI_KEY=<openai-key> `
    -e DB_USERNAME=<db-username> `
    -e DB_PASSWORD=<db-password> `
    -e DB_HOST=<db-host> `
    3moya/gpt-answers:dev
```

We have employed the `-e` flag to define a series of essential environmental variables required for application functionality, thereby avoiding the inclusion of sensitive information within the Docker image.