# BlogChain project

### Requirements

- Docker

- docker-compose

### Run

```shell script
docker-compose up --build
```

**it sholdnt be detached as emails sends to console**

### Stop

Ctrl+C and then run 

```shell script
docker-compose down -v --remove-orphans
```

##### P.S.

You'll probably need to make script executable.

If you on linux pun next from the project-root directory:

```shell script
sudo chmod +x backend/scripts/start.sh
```
