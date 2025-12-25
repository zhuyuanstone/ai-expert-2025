# prep/refresher.py
# 基础自测题（Week 0 Step-4） 25 min 内完成，≥80 % 通关

import numpy as np
import time, functools

# 1. 矩阵乘法
# 设矩阵A=(a_{ij})_{m×n}和B=(b_{ij})_{n×s}，令C=(c_{ij})_{m×s}。
# 其中c_{ij}=∑_{k=1}^{n}a_{ik}b_{kj}(1≤i≤m,1≤j≤s)，那么矩阵C称为矩阵A与B的乘积，记为C=AB或C=A·B。
# 为方便，称被乘数A为左矩阵，乘数B为右矩阵。

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
# TODO：计算 A@B 并把结果赋给 C
C = np.dot(A, B)
print("C =\n", C)

# # 2. 求导  f(x)=x²+3x+2 在 x=2 处的导数
import sympy as sp
x = sp.Symbol('x')
f = x**2 + 3*x + 2
# TODO：求导并赋给 df
df = sp.diff(f, x)
print("f'(2) =", df.subs(x, 2))


# # 3. Python 装饰器：计时并打印运行时间
def print_runtime(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # TODO：补充计时逻辑
        start = time.time()
        func()
        end = time.time()
        print("start=", start, ", end=", end)
        print("Runtime: ", end - start, "s")

    return wrapper


@print_runtime
def test():
    print("----------test")
    time.sleep(0.5)


if __name__ == "__main__":
    test()          # 应打印运行时长