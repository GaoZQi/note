# Matlab

## 矩阵

### 赋值运算符 和 等号运算符

```matlab
% 赋值运算符：=
a = 1；
b = 2;
c = a+b;
---
c = 3
```

```matlab
% 等号运算符： ==（逻辑运算符：返回0或1）
a == 1;
a == b;
---
ans = Logical
0
```

### 定义空矩阵

```matlab
m = [];
```

### 定义一个m*n的矩阵

```matlab
% m = 1, n = 1 一行一列
m = [1];
---
m = 1
```

```matlab
% m = 1 行矩阵
m = [1 2 3];
---
m = 1×3
	1 	2	 3
```

```matlab
% n = 1 列矩阵
m = [1;2;3]
---
m = 3×1
	1
	2
	3
```

```matlab
% m行n列的矩阵
m = [1,2,3; 4 5 6]
---
m = 2×3
	1	2	3
	4	5	6
```

### 使用 冒号运算符 生成矩阵

```matlab
% m = 初始值：步长：终值（默认步长为1）
1:10
---
ans = 1×10
	1	2	3	4	5	6	7	8	9	10
```

```matlab
1:0.5:10
---
ans = 1×19
	1.0000	1.5000	2.0000	2.5000	3.0000	3.5000	...
```

> **`linspace(x1,x2,n)`**
>
> x1 x2：点区间 数值标量对组
>
> n：点的数目（可选）100（默认）

```matlab
% m = linspace(初始值，终值，点数)
linspace(1, 10, 10)
---
ans = 1×10
	1	2	3	4	5	6	7	8	9	10
```

```matlab
linspace(1, 10, 100)
---
ans = 1×100
	1.0000	1.0909	1.1818	1.2727	1.3636	1.4545	...
```

### 拼凑和变形

```matlab
% 行拼接
m1 = [1,2,3];
m2 = [4,5,6];
[m1,m2];
---
ans = 1×6
	1	2	3	4	5	6
```

```matlab
% 列拼接
m1 = [1,2,3];
m2 = [4,5,6];
[m1;m2];
---
ans = 2×3
	1	2	3
	4	5	6
```

> **`reshape(A,sz)`** 
>
> A：向量，矩阵，多维数组
>
> sz：输出大小，有数组组成的行向量

```matlab
% 矩阵变形 reshape(矩阵，要变成的形状)
reshape(1:10,[2,5])
---
ans = 2×5
	1	2	3	4	5
	6	7	8	9	10
```

## 特殊矩阵和随机矩阵

### 特殊矩阵

#### 单位矩阵

> **`eye(n,m,classname)`**
>
> n为阶数

```matlab
% 单位矩阵
n = 3;
eye(n)
---
ans = 3×3
	1	0	0
	0	1	0
	0	0	1
```

#### 全0矩阵

> **`zeros(sz,classname)`**
>
> `zeros(n)`n阶数
>
> `zeros([m,n])`m为行数，n为列数

```matlab
% 全0矩阵
zeros(n);
zeros(3,5);
zeros([3,5]);
---
ans = 3×5
	0	0	0	0	0	
	0	0	0	0	0
	0	0	0	0	0
```

#### 全1矩阵

> **`ones(sz,classname)`**
>
> `ones(n)`n阶数
>
> `ones([m,n])`m为行数，n为列数

```matlab
% 全0矩阵
ones(n);
ones(3,5);
ones([3,5]);
---
ans = 3×5
	1	1	1	1	1	
	1	1	1	1	1
	1	1	1	1	1
```

#### 三维矩阵

> **[行，列，页]**
>
> 应用：彩色图像RGB通道

```matlab
ones([2,2,3])
---
ans = 
ans(:,:,1) = 
	1	1
	1	1
ans(:,:,2) = 
	1	1
	1	1
ans(:,:,3) = 
	1	1
	1	1
```

### 随机矩阵
