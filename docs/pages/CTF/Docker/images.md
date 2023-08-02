# Docker镜像的使用

## 查看镜像列表

可以通过指令查看本地主机上的镜像有关信息。

```bash
docker images
```

其中，每一列的含义如下：

+ REPOSITORY：表示镜像的仓库源
+ TAG：镜像的标签
+ IMAGE ID：镜像ID
+ CREATED：镜像创建时间
+ SIZE：镜像大小

## 拉取镜像

当我们在本地主机上使用一个不存在的镜像时 Docker 就会自动下载这个镜像。如果我们想预先下载这个镜像，我们可以使用 docker pull 命令来下载它。

```bash
docker pull [image name]
```

当一个仓库中有多个镜像时，我们可以通过标签来指定具体是哪个镜像。例如，我们可以通过下面的命令来下载 Ubuntu 18.04 版本的镜像：

```bash
docker pull ubuntu:18.04
```

## 查找镜像

可以通过指令在[Docker Hub](https://hub.docker.com/) 上查找镜像。

```bash
docker search [image name]
```

## 删除镜像

可以通过指令删掉本地拉取的镜像。

```bash
docker rmi [image id]
```

## 构造镜像流程

当仓库中的镜像无法满足要求，可以通过下面两种方式来构造镜像：

+ 从已经创建的容器中更新镜像，并且提交这个镜像
+ 使用 Dockerfile 指令来创建一个新的镜像

### 从容器中更新镜像

1. 启动容器

    ```bash
    docker run -it --name [container name] [image name] /bin/bash
    ```

    其中，`-i`表示以交互模式运行容器，`-t`表示容器启动后会进入其命令行。加入这两个参数后，容器创建就能登录进去。即分配一个伪终端。

2. 在容器中安装所需的软件包

    ```bash
    apt-get update
    apt-get install -y [package name]
    ```

3. 退出容器

    ```bash
    exit
    ```

4. 提交容器更新后的镜像

    ```bash
    docker commit [container name] [image name]
    ```

### 使用 Dockerfile 创建镜像

1. 编写 Dockerfile

    ```bash
    FROM [image name]
    RUN [command]
    ```

    其中，`FROM`指定基础镜像，`RUN`指定构建镜像时运行的命令。

2. 构建镜像

    ```bash
    docker build -t [image name] [Dockerfile path]
    ```

    其中，`-t`指定镜像的名称。

### 设置镜像标签

可以通过指令为镜像设置标签。

```bash
docker tag [image id] [image name]:[tag]
```
