# pwntools

## 引入模块

1. 全功优化后的pwn模块

    ```python
    import pwn
    from pwn import *
    ```

2. 普通的Python库

    ```python
    import pwnlib.util
    ```

## pwntools安装略

## 基础操作

### 连接程序

1. 本地程序
2. 远程TCP/UDP链接
3. SSH链接
4. 串行端口I/O

### 基础I/O

#### 接收数据

``` python
recv(n) # 接收任意数量的可用字节
recvline() # 接收数据，直到遇到换行符
recvuntil(delim) # 接收数据，直到找到分隔符
recvregex(pattern) # 接收数据，直到满足正则表达式模式
recvrepeat(timeout) # 继续接收数据，直到发生超时
clean() # 丢弃所有缓冲数据
```

### 发送数据

```python
send(data) # 发送数据
sendline(line) # 发送数据加换行符
```
<!-- NOTE 没看懂这个  -->
### 操作整数

+ `pack(int)` - 发送一个字大小的打包整数
+ `unpack()` - 接收和解压缩字大小的整数

### 连接流程

创造通道与进程对话前，需创建一个 process 对象并为其指定目标二进制文件的名称。

```python
from pwn import *

io = process('sh')
io.sendline('echo Hello, world')
io.recvline()
# 'Hello, world\n'
```
