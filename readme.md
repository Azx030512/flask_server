# readme

## build docker image

**构建docker时需要分别在前端和后端的目录下构建，/code/flask_server下有backend.dockerfile，mysql.dockerfile，mosquitto.dockerfile 3个文件需要构建**

```
docker build --file backend.dockerfile -t backend .

docker build --file mysql.dockerfile -t mysql .

docker build --file mosquitto.dockerfile -t mosquitto .
```



## single docker start up in turn

**依次运行4个docker镜像，确保先运行起mqtt broker和数据库后，再运行前端和后端代码，不然后端连接数据库时可能会出错**

### start database 

**可能本机的3306端口已经被本机数据库软件占用了，需要关闭本机的占用程序**

```
docker run mysql  
```

### start mosquitto(mqtt broker)

**可能本机的1883端口已经被本机数据库软件占用了，需要关闭本机的mqtt server**

```
docker run mosquitto 
```

### start backend(Flask)

```
docker run --network=host  backend
```

