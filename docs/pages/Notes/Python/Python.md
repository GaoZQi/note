# Python

## 配置环境

### 安装Python

+ 下载地址：[Python 官网](https://www.python.org/)

+ Add Python to PATH

+ 查看Python安装地址：

  ```
  where python
  ```

+ 在终端中运行Python：

   ```shell
    python
  ```

### 安装VSCode

+ 下载地址：[Visual Studio Code - Code Editing. Redefined](https://code.visualstudio.com/)

  > 国内镜像源地址：<u>vscode.cdn.azure.cn</u>

+ 安装插件：[Python - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## 变量和简单数据类型

### 变量的命名和使用

+ 变量名只能包含字母、数字和下划线。变量名能以字母或下划线打头，但不能以数字打头。
+ 变量名不能包含空格，但能用下划线来分隔其中的单词。
+ 不能将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊作用的单词，如`print`。
+ 变量名应及简短又具有描述性。
+ 慎用小写字母`l`和大写字母`O`，因为他们可能被人看错成数字`1`和`0`。

### 字符串

**字符串**就是一系列字符。在Python中，用引号括起的都是字符串，其中引号可以是单引号，也可以是双引号。

```python
"This is a string."
'This is also a string.'
```

在字符串中如果又有引号或者撇号可以这样处理：

```python
'I tolt my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."
```

#### 使用方法修改字符串的大小写

+ 首字母大写

  ```python
  name = "ada lovelace"
  print(name.title())
  ---
  Ada Lovelace
  ```

+ 全部大写

  ```python
  name = "ada lovelace"
  print(name.upper())
  ---
  ADA LOVELACE
  ```

+ 全部大写

  ```py
  name = "ada lovelace"
  print(name.lower())
  ---
  ada lovelace
  ```

#### 在字符串中使用变量

在字符串中插入变量的值，可在引号前加上字符`f`，再将要插入的变量放在花括号内。这样，当Python显示字符串时，将把每个变量都替换为其值。

```py
first_name = "ada"
last_name = "lobelace"
full_name = f"{first_name} {last_name}"
---
ada lovelace
```

这种字符串名**f字符串**。f是format（设置格式）的简写。

```py
first_name = "ada"
last_name = "lobelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")
---
Ada Lovelace
```

#### 使用制表符和换行符添加空白

##### 制表符`\t`

```py
>>> print("\tPython")
	Python
```

##### 换行符`\n`

```py
>>> print("Languages:\nPython\nC\nJavaScript")
Languages:
Python
C
JavaScript
```

#### 删除空白

##### 去除末尾空格`rstrip()`

```py
>>> favorite_language = 'python '
>>> favorite_language
'python '

>>> favorite_languages.rstrip()
'python'

>>> favorite_language
'python '
```

##### **去除开头空格`lstrip()`**

```py
>>> favorite_language = ' python'
>>> favorite_language
' python'

>>> favorite_languages.rstrip()
'python'

>>> favorite_language
' python'
```

##### **去除两边空格`strip()`**

```py
>>> favorite_language = ' python '
>>> favorite_language
' python '

>>> favorite_languages.strip()
'python'

>>> favorite_language
' python '
```

### 数

#### 整数

##### 加 减 乘 除 乘方

```py
>>> 2 + 3
5
>>> 2 - 3
-1
>>> 2 * 3
6
>>> 3 / 2
1.5
>>> 2 ** 3
8
```

#### 浮点数

```

```

##### 数字中的下划线

##### 多变量赋值

#### 常量

#### 注释

