import hello.fun_test
# 调用函数文件

hello.fun_test.multiple_table()
a=input("请输入a:")
b=input("请输入b:")
hello.fun_test.sum(int(a),int(b))
def first():
    print("hello")

first()
sum=hello.fun_test.sum(int(a),int(b))
# 函数的嵌套调用
def print_line(char,n):
    """
    打印字符
    :param char:分割字符
    :param n:重复次数
    :return:
    """
    print( char * n)

print_line('%',2)