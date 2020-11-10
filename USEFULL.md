Cleaning of docker

```shell script
docker system prune -f
docker rmi $(docker images -f "dangling=true" -q)
docker rmi $(docker images -a -q)
docker rm $(docker ps --filter=status=exited --filter=status=created -q)

```

```shell script
docker run --rm -it -v /home/michael/PycharmProjects/EasyB/frontend/:/code node:14.14.0-alpine /bin/sh
```


Change permissions

```shell script
sudo chown -R $USER:$USER .
```


Making script executable

```shell script
sudo chmod +x backend/scripts/start.dev.sh
```


Removing of docker-compose.dev.yml session

```shell script
docker-compose -f docker-compose.dev.yml down -v --remove-orphans
```


Start of docker-compose.dev,yml session (first run will take a time)

```shell script
docker-compose -f docker-compose.dev.yml up --build
```


Entering to server console

```shell script
docker exec -it server /bin/sh
```

```shell script
npm audit fix
npm audit
```

