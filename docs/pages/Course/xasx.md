# 信息安全数学基础

## 整除

1. 概念

    设 $\forall a,b \in \mathbb{Z}$ 若 $\exists q$ 使得 $a=bq$ 则称 $a$ 能被 $b$ 整除，记作 $b|a$，$a$ 是 $b$ 的倍数，$b$ 是 $a$ 的约数。

2. 性质

    若设 $a,b,c \in \mathbb{Z}$，其中 $c|a, c|b$ ，则 $c|ax+by, ( x,y\in \mathbb{{Z}} )$.

## 素数

通常用 $p$ 表示素数$p \in \mathbb{Z}$.

1. 定理
    1. 设$n\in\mathbb{Z}$，则$n$的大于$1$的最小正因子必为素数$p$且$p\le \sqrt{n}$

    !!! note "证明"
        ① 假设$p$为非素数，则$\exists q \in \mathbb{Z} p|q,p|n\Rightarrow q|n$矛盾.

        ② 假设$p>\sqrt{n}$，则$\frac{n}{p}<\sqrt{n}<p$

   1. 设$p$为素数，$a,b\in\mathbb{Z}$，则$p|ab\Rightarrow p|a$或$p|b$

2. 素数有无穷多个

## 最大公因数 gcd

!!! note "简记"
    $\forall a,b\in \mathbb{Z},gcd(a,b)$简记作$(a,b)$.

1. 定义

    设$a,b\in\mathbb{Z}$，若$d|a,d|b$，则称$d$为$a,b$的公因数，记作$d|(a,b)$，其中$d\in\mathbb{Z}$，且$d>0$，若$(a,b)$中最大的正整数为$d$，则称$d$为$a,b$的最大公因数，记作$d=gcd(a,b)$

    !!! note "带余除法"
        $\forall a,b \in \mathbb{Z}$必定$\exists q,r \in \mathbb{Z}$使得$a=qb+r$

        $\exists q \in \mathbb{Z}，使得qb\le a<(q+1)b.$

        令$r=a-qb\Rightarrow a= qb+r (0\le r<b)$

## 代数基本定理

$$
\forall n \in \mathbb{Z}, n=p_1p_2\cdots p_k
$$

## Euclid 算法

$\forall a,b \in \mathbb{Z}$则$a=qb+r$

$\Rightarrow gcd(a,b)=gcd(b,r), (0\le r<b)$

设$d_1=gcd(a,b) d_2=gcd(b,r)$

则$d_1|a,d_1|b_1 \Rightarrow d_1|r \Rightarrow d_1\le d_2$

同理可证$d_2\le d_1$
