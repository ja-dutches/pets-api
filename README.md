### Remove stopped containers
```bash
$ docker-compose rm -f
```
### Remove "dangling images"
```bash
$ docker rmi -f $(docker images -qf dangling=true)
```
### docker-compose command for running web app
```bash
$ docker-compose run --service-ports web
```
