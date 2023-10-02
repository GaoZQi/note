# Docker指令

??? info "全部指令预览："

        Usage |  docker [OPTIONS] COMMAND

        A self-sufficient runtime for containers

        Common Commands |
        run         Create and run a new container from an image
        exec        Execute a command in a running container
        ps          List containers
        build       Build an image from a Dockerfile
        pull        Download an image from a registry
        push        Upload an image to a registry
        images      List images
        login       Log in to a registry
        logout      Log out from a registry
        search      Search Docker Hub for images
        version     Show the Docker version information
        info        Display system-wide information

        Management Commands |
        builder     Manage builds
        buildx*     Docker Buildx (Docker Inc., v0.11.0)
        compose*    Docker Compose (Docker Inc., v2.19.1)
        container   Manage containers
        context     Manage contexts
        dev*        Docker Dev Environments (Docker Inc., v0.1.0)
        extension*  Manages Docker extensions (Docker Inc., v0.2.20)
        image       Manage images
        init*       Creates Docker-related starter files for your project (Docker Inc., v0.1.0-beta.6)
        manifest    Manage Docker image manifests and manifest lists
        network     Manage networks
        plugin      Manage plugins
        sbom*       View the packaged-based Software Bill Of Materials (SBOM) for an image (Anchore Inc., 0.6.0)
        scan*       Docker Scan (Docker Inc., v0.26.0)
        scout*      Command line tool for Docker Scout (Docker Inc., 0.16.1)
        system      Manage Docker
        trust       Manage trust on Docker images
        volume      Manage volumes

        Swarm Commands |
        swarm       Manage Swarm

        Commands |
        attach      Attach local standard input, output, and error streams to a running container
        commit      Create a new image from a container's changes
        cp          Copy files/folders between a container and the local filesystem
        create      Create a new container
        diff        Inspect changes to files or directories on a container's filesystem
        events      Get real time events from the server
        export      Export a container's filesystem as a tar archive
        history     Show the history of an image
        import      Import the contents from a tarball to create a filesystem image
        inspect     Return low-level information on Docker objects
        kill        Kill one or more running containers
        load        Load an image from a tar archive or STDIN
        logs        Fetch the logs of a container
        pause       Pause all processes within one or more containers
        port        List port mappings or a specific mapping for the container
        rename      Rename a container
        restart     Restart one or more containers
        rm          Remove one or more containers
        rmi         Remove one or more images
        save        Save one or more images to a tar archive (streamed to STDOUT by default)
        start       Start one or more stopped containers
        stats       Display a live stream of container(s) resource usage statistics
        stop        Stop one or more running containers
        tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE
        top         Display the running processes of a container
        unpause     Unpause all processes within one or more containers
        update      Update configuration of one or more containers
        wait        Block until one or more containers stop, then print their exit codes

        Global Options |
            --config string      Location of client config files (default "/home/gaozqi/.docker")
        -c, --context string     Name of the context to use to connect to the daemon (overrides DOCKER_HOST env var and
                                default context set with "docker context use")
        -D, --debug              Enable debug mode
        -H, --host list          Daemon socket to connect to
        -l, --log-level string   Set the logging level ("debug", "info", "warn", "error", "fatal") (default "info")
            --tls                Use TLS; implied by --tlsverify
            --tlscacert string   Trust certs signed only by this CA (default "/home/gaozqi/.docker/ca.pem")
            --tlscert string     Path to TLS certificate file (default "/home/gaozqi/.docker/cert.pem")
            --tlskey string      Path to TLS key file (default "/home/gaozqi/.docker/key.pem")
            --tlsverify          Use TLS and verify the remote
        -v, --version            Print version information and quit

        Run 'docker COMMAND --help' for more information on a command.

        For more help on how to use Docker, head to https |//docs.docker.com/go/guides/

## 容器生命周期管理

### run

创建一个新的容器并运行一个命令

```bash
docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | -a stdin | 指定标准输入输出内容类型，可选 `STDIN/STDOUT/STDERR` 三项 |
    | `-d` | 后台运行容器，并返回容器ID |
    | `-i` | 以交互模式运行容器，通常与 `-t` 同时使用 |
    | `-P` | 随机端口映射，容器内部端口随机映射到主机的端口 |
    | `-p` | 指定端口映射，格式为：**主机(宿主)端口:容器端口** |
    | `-t` | 为容器重新分配一个伪输入终端，通常与 `-i` 同时使用 |
    | `--name="nginx-lb"` | 为容器指定一个名称 |
    | `--dns 8.8.8.8` | 指定容器使用的DNS服务器，默认和宿主一致 |
    | `--dns-search example.com` | 指定容器DNS搜索域名，默认和宿主一致 |
    | `-h "mars"` | 指定容器的hostname |
    | `-e username="ritchie"` | 设置环境变量 |
    | `--env-file=[]` | 从指定文件读入环境变量 |
    | `--cpuset="0-2" or --cpuset="0,1,2"` | 绑定容器到指定CPU运行 |
    | `-m ` |设置容器使用内存最大值 |
    | `--net="bridge"` | 指定容器的网络连接类型，支持 `bridge/host/none/container` 四种类型 |
    | `--link=[]` | 添加链接到另一个容器 |
    | `--expose=[]` | 开放一个端口或一组端口 |
    | `--volume , -v` | 绑定一个卷 |

### start

启动一个或多个已经被停止的容器

```bash
docker start [OPTIONS] CONTAINER [CONTAINER...]
```

### stop

停止一个运行中的容器
```bash

docker stop [OPTIONS] CONTAINER [CONTAINER...]
```

### restart

重启容器

```bash
docker restart [OPTIONS] CONTAINER [CONTAINER...]
```

### kill

杀掉一个运行中的容器。

```bash
docker kill [OPTIONS] CONTAINER [CONTAINER...]
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `-s` | 向容器发送一个信号 |

### rm

删除一个或多个容器。
```bash
docker rm [OPTIONS] CONTAINER [CONTAINER...]
```
??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `-f` | 强制删除一个运行中的容器 |
    | `-l` | 移除容器间的网络连接，而非容器本身 |
    | `-v` | 删除与容器关联的卷 |

### pause

暂停容器中所有的进程。

```bash
docker pause [OPTIONS] CONTAINER [CONTAINER...]
```

### unpause

恢复容器中所有的进程。

```bash
docker unpause [OPTIONS] CONTAINER [CONTAINER...]
```

### create

创建一个新的容器但不启动它。

```bash
docker create [OPTIONS] IMAGE [COMMAND] [ARG...]
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | -a stdin | 指定标准输入输出内容类型，可选 `STDIN/STDOUT/STDERR` 三项 |
    | `-d` | 后台运行容器，并返回容器ID |
    | `-i` | 以交互模式运行容器，通常与 `-t` 同时使用 |
    | `-P` | 随机端口映射，容器内部端口随机映射到主机的端口 |
    | `-p` | 指定端口映射，格式为：**主机(宿主)端口:容器端口** |
    | `-t` | 为容器重新分配一个伪输入终端，通常与 `-i` 同时使用 |
    | `--name="nginx-lb"` | 为容器指定一个名称 |
    | `--dns 8.8.8.8` | 指定容器使用的DNS服务器，默认和宿主一致 |
    | `--dns-search example.com` | 指定容器DNS搜索域名，默认和宿主一致 |
    | `-h "mars"` | 指定容器的hostname |
    | `-e username="ritchie"` | 设置环境变量 |
    | `--env-file=[]` | 从指定文件读入环境变量 |
    | `--cpuset="0-2" or --cpuset="0,1,2"` | 绑定容器到指定CPU运行 |
    | `-m ` |设置容器使用内存最大值 |
    | `--net="bridge"` | 指定容器的网络连接类型，支持 `bridge/host/none/container` 四种类型 |
    | `--link=[]` | 添加链接到另一个容器 |
    | `--expose=[]` | 开放一个端口或一组端口 |
    | `--volume , -v` | 绑定一个卷 |

### exec

在运行的容器中执行命令。

```bash
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `-d` | 分离模式: 在后台运行 |
    | `-i` | 即使没有附加也保持 STDIN 打开 |
    | `-t` | 分配一个伪终端 |

---

## 容器操作

### ps

列出容器

```bash
docker ps [OPTIONS]
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `-a` | 列出所有容器，包括未运行的 |
    | `-f` | 按条件过滤显示的内容 |
    | `-l` | 显示最近创建的容器 |
    | `-n` | 显示最近创建的n个容器 |
    | `--no-trunc` | 不截断输出 |
    | `-q` | 静默模式，只显示容器编号 |
    | `-s` | 显示总的文件大小 |
    | `--format` | 指定返回值的模板文件 |

??? note "输出详情介绍："

    | 项目 | 说明 |
    |:--|:--|
    CONTAINER ID | 容器 ID。
    IMAGE | 使用的镜像。
    COMMAND | 启动容器时运行的命令。
    CREATED | 容器的创建时间。
    STATUS | 容器状态。
    PORTS | 容器的端口信息和使用的连接类型（tcp\udp）。
    NAMES | 自动分配的容器名称。

    状态有7种：

    + created（已创建）
    + restarting（重启中）
    + running（运行中）
    + removing（迁移中）
    + paused（暂停）
    + exited（停止）
    + dead（死亡）


### inspect

显示一个或多个容器的详细信息

```bash
docker inspect [OPTIONS] CONTAINER [CONTAINER...]
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `-f` | 指定返回值的模板文件 |
    | `-s` | 显示总的文件大小 |
    | `--type` | 为指定类型返回JSON |

### top

显示一个容器中运行的进程信息

```bash
docker top [OPTIONS] CONTAINER [CONTAINER...]
```

### attach

依附到一个运行的容器

```bash
docker attach [OPTIONS] CONTAINER
```

### events

从服务器获取实时事件

```bash
docker events [OPTIONS]
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `--since` | 从指定的时间戳后显示所有事件 |
    | `--until` | 浏览到指定的时间戳后显示所有事件 |
    | `-f` | 根据条件过滤事件 |

### logs

获取容器的日志

```bash
docker logs [OPTIONS] CONTAINER
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `-f` | 跟踪日志输出 |
    | `-t` | 显示时间戳 |
    | `--tail` | 仅列出最新N条容器日志 |
    | `--since` | 显示某个开始时间的所有日志 |

### wait

阻塞运行直到容器停止，然后打印出它的退出代码

```bash
docker wait [OPTIONS] CONTAINER [CONTAINER...]
```

### export

将文件系统作为一个tar归档文件导出到STDOUT

```bash
docker export [OPTIONS] CONTAINER
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `-o` | 将输入内容写入文件 |

### port

列出指定的容器的端口映射，或者查找将PRIVATE_PORT NAT到面向公众的端口

```bash
docker port [OPTIONS] CONTAINER [PRIVATE_PORT[/PROTO]]
```

### stats

显示容器的资源使用统计信息

```bash
docker stats [OPTIONS] [CONTAINER...]
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `--no-stream` | 只打印一次信息 |
    | `--no-trunc` | 不截断输出 |
    | `--format` | 指定返回值的模板文件 |
    | `--all, -a` | 显示所有容器，默认只显示运行中的容器 |

??? note "输出详情介绍："

    | 项目 | 说明 |
    |:--|:--|
    CONTAINER | 容器 ID
    CPU % | CPU 使用率
    MEM USAGE / LIMIT | 内存使用量 / 总内存
    MEM % | 内存使用率
    NET I/O | 网络 I/O，容器通过其网络接口发送和接收的数据量
    BLOCK I/O | 块 I/O，容器从主机上的块设备读取和写入的数据量
    PIDS | PID 总数，容器创建的进程或线程数
    NAME | 容器名

## 容器rootfs命令

### commit

从容器创建一个新的镜像

```bash
docker commit [OPTIONS] CONTAINER [REPOSITORY[:TAG]]
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `-a` | 提交的镜像作者 |
    | `-c` | 使用Dockerfile指令来创建镜像 |
    | `-m` | 提交时的说明文字 |
    | `-p` | 在commit时，将容器暂停 |

### cp

从容器里向外拷贝文件或目录到主机

```bash
docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH
docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `-L` | 跟随符号链接 |

### diff

检查容器里文件结构的更改

```bash
docker diff CONTAINER
```

## 镜像仓库

### login

登录到一个Docker镜像仓库，如果未指定镜像仓库地址，默认为Docker Hub

```bash
docker login [OPTIONS] [SERVER]
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `-u` | 用户名 |
    | `-p` | 密码 |

### logout

从一个Docker镜像仓库登出，如果未指定镜像仓库地址，默认为Docker Hub

```bash
docker logout [SERVER]
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `-u` | 用户名 |
    | `-p` | 密码 |

### pull

从一个Docker镜像仓库拉取镜像或仓库

```bash
docker pull [OPTIONS] NAME[:TAG|@DIGEST]
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | ` -a` | 拉取所有 tagged 镜像 |
    | `--disable-content-trust` | 跳过镜像验证，默认开启 |

### push

将本地的镜像上传到镜像仓库，如果未指定镜像仓库地址，默认为Docker Hub

```bash
docker push [OPTIONS] NAME[:TAG]
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `--disable-content-trust` | 跳过镜像验证，默认开启 |

### search

在Docker Hub中搜索镜像

```bash
docker search [OPTIONS] TERM
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `--automated` | 只列出 automated build 类型的镜像 |
    | `--no-trunc` | 不截断输出 |
    | `-f<过滤条件>` | 根据条件过滤输出 |

??? note "过滤条件说明："
    
    |参数|说明|
    |:--|:--|
    |`NAME`|镜像名称|
    |`DESCRIPTION`|镜像描述|
    |`STARS`|镜像的star数量|
    |`OFFICIAL`|是否官方镜像|
    |`AUTOMATED`|是否自动构建|

## 本地镜像管理

### images

列出本地镜像

```bash
docker images [OPTIONS] [REPOSITORY[:TAG]]
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `-a` | 列出所有镜像，默认只列出非中间层镜像 |
    | `-q` | 只显示镜像ID |
    | `--digests` | 显示镜像的摘要信息 |
    | `--no-trunc` | 不截断输出 |
    | `--format` | 指定返回值的模板文件 |
    | `-f` | 根据条件过滤输出 |

### rmi

删除本地一个或多少镜像

```bash
docker rmi [OPTIONS] IMAGE [IMAGE...]
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `-f` | 强制删除 |
    | `-no-prune` | 不移除该镜像的过程镜像，默认移除 |

### tag

给本地镜像打标签

```bash
docker tag [OPTIONS] IMAGE[:TAG] [REGISTRYHOST/][USERNAME/]NAME[:TAG]
```

### build

使用Dockerfile创建镜像

```bash
docker build [OPTIONS] PATH | URL | -
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `--tag, -t` | 指定要创建的目标镜像名。镜像的名字及标签，通常 name:tag 或者 name 格式；可以在一次构建中为一个镜像设置多个标签。 |
    | `--quiet, -q` | 不输出镜像构建过程 |
    | `--build-arg=[]` | 设置镜像创建时的变量 |
    | `--disable-content-trust` | 跳过镜像验证，默认开启 |
    | `--no-cache` | 创建镜像的过程不使用缓存 |
    | `--pull` | 尝试去更新镜像的新版本 |
    | `--rm` | 设置镜像成功后删除中间容器 |
    | `--force-rm` | 设置镜像过程中删除中间容器 |
    | `--memory-swap` | 设置Swap的最大值为内存+swap，"-1"表示不限swap |
    | `--ulimit` | Ulimit配置 |
    | `--cpu-shares` | 设置容器CPU权重，默认为0 |
    | `--cpu-period` | 限制CPU CFS周期 |
    | `--cpu-quota` | 限制CPU CFS配额 |
    | `--cpuset-cpus` | 设置容器可以使用哪些CPU，此参数可以用来容器独占CPU |
    | `--cpuset-mems` | 设置容器可以使用哪些内存，此参数可以用来容器独占内存 |
    | `--isolation` | 使用容器隔离技术 |
    | `--network` | 默认 default。在构建期间设置RUN指令的网络模式 |
    | `--label=[]` | 设置镜像使用的元数据 |
    | `--shm-size` | 设置/dev/shm的大小，默认值是64M |
    | `--squash` | 将 Dockerfile 中所有的操作压缩为一层 |
    | `--file , -f` | 指定要使用的Dockerfile路径 |
    | `-m` | 设置内存最大值 |

### history

显示一个镜像的历史

```bash
docker history [OPTIONS] IMAGE
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `--no-trunc` | 显示完整的提交记录 |
    | `-q` | 仅列出提交记录ID |
    | `-H` | 以可读的格式打印镜像大小和日期，默认为true |

### save

将一个或多个镜像保存成tar包到本地

```bash
docker save [OPTIONS] IMAGE [IMAGE...]
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `-o` | 输出到指定文件 |

### load

从tar包中加载一个或多个镜像

```bash
docker load [OPTIONS]
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `--input , -i` | 从指定文件中读入 |
    | `--quiet , -q` | 静默模式，不输出任何信息 |

### import

从归档文件中创建镜像

```bash
docker import [OPTIONS] file|URL|- [REPOSITORY[:TAG]]
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | ` -c` | 应用docker 指令创建镜像 |
    | `-m` | 提交时的说明文字 |

## 相关信息

### version

显示 Docker 版本信息。

```bash
docker version [OPTIONS]
```

??? tip "OPTIONS说明："

    | 选项 | 说明 |
    |:--|:--|
    | `-f` | 指定返回值的模板文件 |

### info

显示 Docker 系统信息，包括镜像和容器数。

```bash
docker info [OPTIONS]
```

<link rel="stylesheet" href="../../../../css/CTF/custom.css">