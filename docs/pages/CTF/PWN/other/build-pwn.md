# 利用Docker技术部署PWN题目

!!! quote "参考文章"

    [使用docker搭建pwn题靶机 :material-link:](https://www.jianshu.com/p/5afa84465125)

    [Docker的使用 :material-arrow-bottom-right-thick:](../../Docker/index.md)

## 制作Docker镜像

1. 拉取镜像

    ```bash
    docker pull ubuntu:16.04
    ```

2. 运行容器

    ```bash
    docker run -it ubuntu:16.04 /bin/bash #启动容器(1)
    ```

    1. `-it`：交互式运行容器
    
        `ubuntu:16.04`：镜像名字
        
        `/bin/bash`：容器启动后执行的命令

3. 安装工具

    ```bash
    sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.aliyun.com/g" /etc/apt/sources.list #将源替换为阿里云源
    apt-get update && apt-get -y dist-upgrade #更新源
    apt-get install -y lib32z1 xinetd build-essential python python-dev #安装工具
    ```

4. 退出容器

    ```bash
    exit
    ```

5. 提交容器

    ```bash
    docker commit CONTAINER_HASH pwn_server:16.04 #参数含义(1) 
    ```

    1. `CONTAINER_HASH`：容器的hash值

        `pwn_server:16.04`：镜像名字

## 部署PWN题目

1. 创建目录

    ```bash
    mkdir -p /home/pwn_server
    ```

    !!! note "目录结构"

        ```bash
        /home/pwn_server
        ├── pwn #binary文件(1)
        ├── pxi #xinetd脚本(2)
        ├── start.sh #启动脚本(3)
        └── flag #flag文件
        ```

        1. pwn题目的二进制文件

        2. 用于配置pwn题服务

        3. 启动container时运行的脚本

2. 创建flag文件

    ```bash
    echo "flag{test}" > /home/pwn_server/flag
    ```

3. 创建xinetd配置文件

    ```bash title="pxi"
    service pwn #服务名
    {
        disable = no #是否禁用
        socket_type = stream #socket类型
        protocol    = tcp #协议
        wait        = no #是否等待
        user        = root #运行用户
        type        = UNLISTED #类型
        port        = 8888 #端口
        bind        = 0.0.0.0 #绑定地址
        server      = /usr/sbin/chroot #服务程序
        server_args = --userspec=ctf:ctf / timeout 30 ./home/ctf/pwn #服务程序参数
        banner_fail = /etc/banner_fail #banner文件

        # safety options
        per_source    = 10 # the maximum instances of this service per source IP address
        rlimit_cpu    = 60 # the maximum number of CPU seconds that the service may use
        rlimit_as     = 1024M # the Address Space resource limit for the service
        #access_times = 2:00-9:00 12:00-24:00

        #Instances   = 20 #process limit
        #per_source  = 5 #link ip limit

        #log warning die
        log_on_success  = PID HOST EXIT DURATION    
        log_on_failure  = HOST ATTEMPT 
        log_type =FILE /var/log/myservice.log 8388608 15728640
    }
    ```

4. 创建启动脚本

    ```bash title="start.sh"
    #!/bin/sh
    useradd -m ctf  #创建用户
    sleep 2 #等待2秒
    chmod 555 -R /home/pwn_server  #修改权限(1)
    cp /home/pwn_server/pxi /etc/xinetd.d/pwn  #复制xinetd配置文件
    /etc/init.d/xinetd restart  #重启xinetd服务
    trap : TERM INT; sleep infinity & wait  #等待
    # /bin/sh
    ```

    1. `555`  `r -xr -xr -x` 所有组都是读取和执行权限


## 启动容器

1. 调试题目
    用来调试题目环境。启动container之后会有一个交互式的shell，可以用来进行多种后续操作。

    ```bash
    docker run -p $PORT:8888 -v `pwd`:/home/pwn_server -ti $IMAGE_NAME /bin/sh #参数含义(1)
    ```

    1. `$PORT` 为`host`端映射的端口，请自行修改

        `$IMAGE_NAME`为使用的`image`的名称

2. 启动题目

    用来部署题目环境。启动container之后会自动启动`xinetd`服务，监听`8888`端口。

    ```bash
    chmod 555 -R . && docker run --name $NAME -p $PORT:8888 -v `pwd`:/home/pwn_server -d $IMAGE_NAME /home/pwn_server/start.sh #参数含义(1)
    ```

    1. `$NAME` 为`container`的名称，请自行修改

        `$PORT` 为`host`端映射的端口，请自行修改

        `$IMAGE_NAME`为使用的`image`的名称