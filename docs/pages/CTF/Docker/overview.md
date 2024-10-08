# Docker简介

Docker 是一个用于开发、交付和运行应用程序的开放平台。Docker 使您能够将应用程序与基础架构分离，以便快速交付软件。借助 Docker，您可以像管理应用程序一样管理基础架构。通过利用 Docker 的快速交付、测试和部署代码的方法，您可以显著减少编写代码和在生产中运行代码之间的延迟。

## Docker架构

![docker](https://docs.docker.com/assets/images/architecture.svg)

## Docker仓库

Docker 仓库用于保存镜像，可以理解为代码控制中的代码仓库。Docker Hub 是一个公共的注册表，任何人都可以使用它来存储和检索镜像。Docker Hub 中的镜像可以由任何人创建，也可以由 Docker Inc. 创建。您可以使用 Docker Hub 作为公共注册表，也可以在本地主机上运行私有注册表。

## Docker对象

### 镜像Image

Docker 镜像是用于创建 Docker 容器的模板。Docker 镜像是一个只读的模板，包含了创建 Docker 容器的说明，例如要运行的容器是 Linux 还是 Windows，容器的环境变量、系统用户等等。镜像不包含任何动态数据，其内容在构建之后也不会被改变。

### 容器Containers

Docker 利用容器来运行应用。容器是从镜像创建的运行实例。可以将容器视为简易版的 Linux 环境（包括 root 用户权限、进程空间、用户空间和网络空间等）和运行在其中的应用程序。容器的底层实现利用 Linux 内核的功能，例如命名空间和控制组，以隔离进程和资源。容器与基础架构和应用程序无关，这意味着您可以轻松地将其从一个平台迁移到另一个平台。

<link rel="stylesheet" href="../../../../css/CTF/custom.css">