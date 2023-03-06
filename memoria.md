# html
# Database
To create the database in AWS, we simply followed the steps in the class guide. The section in AWS to create a DDBB is RDS. There, the user can create a database clicking in the big orange button with just a few adjustments in the parameters. 
The main ones were:
- Changing the Engine options to **MySQL**.
- Changing the Templates to the free one.
- Optional: You can change the name in DB instance identifier.
- Change in the username and creation of the password.
- Optional: In the "Assign Storage" option, you can change the capacity.  

After waiting a few minutes to let the service create our database, we will need to change one thing to allow connectivity with our machine. We click in our DDBB and head into **Security>Entry Rules** to create a new line with IPv4 that allows any traffic with origin (0.0.0.0/0).  
![IPv4](/media/IPv4.png)  
After that, we are all set up to use our DDBB.
# flask

# DB

# openai

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