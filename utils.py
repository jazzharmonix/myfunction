"""
작성일자 : 2023/10/06
작성자 : KDH
코드이름 : utils.py
목적 : 유용한 함수 저장하여 사용하기 위함
"""


def factorial(x) :
    if x<=1:
        return 1
    return x* factorial(x-1)

def gugudan(x):
    for i in range(9):
        print(x, "x", (i + 1), "=", (i + 1) * x)

