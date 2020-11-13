# Usefull

Cleaning of docker

```shell script
docker system prune -f
docker rmi $(docker images -f "dangling=true" -q)
docker rmi $(docker images -a -q)
docker rm $(docker ps --filter=status=exited --filter=status=created -q)

```

Entering into frontend docker for building of it

```shell script
docker run --rm -it -v {PATH_TO_PROJECT}/frontend/:/usr/src/frontend node:15.2.0-alpine /bin/sh
```


Change permissions

```shell script
sudo chown -R $USER:$USER .
```

## Development

Making dev script executable

```shell script
sudo chmod +x backend/scripts/start.dev.sh
```


Removing of docker-compose.dev.yml session

```shell script
docker-compose -f docker-compose.dev.yml down -v --remove-orphans
```


Start of docker-compose.dev.yml session (first run will take a time)

```shell script
docker-compose -f docker-compose.dev.yml up --build
```


Entering to backend console in dev

```shell script
docker exec -it backend-dev /bin/sh
```

Entering to frontend console in dev

```shell script
docker exec -it frontend-dev /bin/sh
```
