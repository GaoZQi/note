# Docker容器的使用

## 构造容器流程

1. 拉取镜像

    在Docker Hub上搜索需要的镜像，如ubuntu:18.04，然后拉取镜像：

    ```bash
    docker pull ubuntu:18.04
    ```

2. 启动容器

    通过下面的命令，可以启动一个 ubuntu:18.04 镜像的容器：

    ```bash
    docker run -it --name ubuntu ubuntu:18.04 /bin/bash
    ```

    + `-i`：表示以交互模式运行容器
    + `-t`：表示容器启动后会进入其命令行。加入这两个参数后，容器创建就能登录进去。即分配一个伪终端。
    + `--name`：为创建的容器命名
    + `ubuntu:18.04`：表示用 ubuntu:18.04 镜像创建容器
    + `/bin/bash`：放在镜像名后的是命令，通过该命令可以开启交互式`shell`。

    如果是web应用，可以使用`docker port`命令来查看映射的端口：

    ```bash
    docker port [container id]
    ```

3. 退出容器

    如果要退出容器，可以直接在终端输入：

    ```bash
    exit
    ```

## 其他命令

### 查看所有容器

```bash
docker ps -a
```

### 启动已经停止的容器

```bash
docker start [container id]
```

### 进入容器

```bash
docker attach [container id]
```

### 停止容器

```bash
docker stop [container id]
```

### 删除容器

```bash
docker rm [container id]
```

### 导入与导出

```bash
docker export [container id] > [file name].tar
docker import [file name].tar [image name]
```

<link rel="stylesheet" href="../../../../css/CTF/custom.css">