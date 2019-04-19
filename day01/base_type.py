def test1():
    print('wdx1')
def test2():
    print('wdx2')
def test3():
    print('wdx3')

def int_demo():
    #声明一个变量   "=" 前为变量名 ，"="后为变量值
    aint = 5
    print(aint)
    #type(aint):获取aint的变量类型
    #print(type(aint)):打印aint的变量类型
    print(type(aint))

def str_demo():
    astr = '5'
    print(astr)
    print(type(astr))

def float():
    afloat = 1.5
    print(afloat)
    print(type(afloat))

def type_zh():
    aint = 7
    print(type(aint))
    print(type( str(aint) ))
    print(type( int(aint) ))

def str_join():
    a=123
    b='嗨'
    c=3.1
    print(str(a)+','+b+','+str(c))
    print('a是%s b是%s c是%s'%(a,b,c))

def add_demo(a,b):
    print(a+b)
def sub_demo(a,b):
    c=a-b
    return c
if __name__ == '__main__':
    #test3()
    #test1()
    #test2()
    #int_demo()
    #str_demo()
    #float()
    #add_demo(31,72)
    # type_zh()
    # str_join()
    c=sub_demo(7,3)
    d=add_demo(7,3)\

    print(c)
    print(type(d))


# for i in range(1, 10):
#     for j in range(1, i+1):
#        print('{}x{}={}\t'.format(j, i, i*j), end='')
#     print()
# if __name__ == '__main__':
#     print()

