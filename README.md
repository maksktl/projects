# How to deploy:

1. Clone git project:

$ git clone git@github.com:semenovsd/Fredbot.git
(Private repository requirement deploy key)

2. Create .env file by the example.env in base folder

3. Run bash script for install and settings Docker:

$ sudo bash entrypoint.sh

4. Build up docker containers:
$ docker-compose up --build

Done!
