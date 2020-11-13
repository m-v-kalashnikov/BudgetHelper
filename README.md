# BudgetHelper project

### Requirements

- Docker

- docker-compose

### Run

##### Dev mode

```shell script
docker-compose -f docker-compose.dev.yml up --build
```

**it shouldn't be detached as emails sends to console**

##### Prod mode

```shell script
docker-compose -f docker-compose.prod.yml up -d --build
```

### Stop

##### Dev mode

Ctrl+C and then run 

```shell script
docker-compose -f docker-compose.dev.yml down -v --remove-orphans
```

##### Prod mode

```shell script
docker-compose -f docker-compose.prod.yml down -v --remove-orphans
```

##### P.S.

You'll probably need to make script executable.

If you on linux run next from the project-root directory:

###### Dev mode

```shell script
sudo chmod +x backend/scripts/start.dev.sh
```

###### Prod mode

```shell script
sudo chmod +x backend/scripts/start.prod.sh
```
