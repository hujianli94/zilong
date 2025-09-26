# usage

```shell
# start zilong-api 
zilong-api --config-file /etc/zilong/zilong.conf

# start zilong-worker
zilong-worker --config-file /etc/zilong/zilong.conf
```


api接口访问

```shell
# 获取API根信息
curl http://localhost:8181/

# 获取V1 API信息
curl http://localhost:8181/v1

# 获取Docker信息
curl http://localhost:8181/v1/docker

# 获取容器列表
curl http://localhost:8181/v1/docker/containers

# 获取镜像列表
curl http://localhost:8181/v1/docker/images

# 获取系统信息
curl http://localhost:8181/v1/docker/system
```
