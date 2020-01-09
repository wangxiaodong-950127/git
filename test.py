def homework1():
    str="aaa你好，你好ajflajfalk你好"
    print (str.count("你好"))




def homework2():
    n=3
    while n>0:
        a = input("input:")
        if a == '1':
            print('Monday')
            break
        elif a == '2':
            print('Tuesday')
            break
        elif a == '3':
            print('Wednesday')
            break
        elif a == '4':
            print('Thursday')
            break
        elif a == '5':
            print('Friday')
            break
        elif a == '6':
            print('Saturday')
            break
        elif a == '7':
            print('Sunday')
            break
        else:
            print('错误的输入,请重新输入1-7之间的数字')
        n=n-1
        if(n==0):
            print('错误的输入超过3次，程序退出！')



def homework3():
    ll = [1, 2, 3, 4, 5]
    i = 0  # 数组下标
    count = ll.__len__() // 2  # 取整，循环的次数
    lasti= ll.__len__() - 1  # 列表最后一个元素坐标
    while count > 0:
        tmp = ll[i]
        ll[i] = ll[lasti]
        ll[lasti] = tmp
        lasti = lasti - 1
        count = count - 1
        i = i + 1
    else:
        print('over')
    print(ll)


def homework3_a(ll):
    i = 0  # 数组下标
    count = ll.__len__() // 2  # 取整，循环的次数
    lasti= ll.__len__() - 1  # 列表最后一个元素坐标
    while count > 0:
        tmp = ll[i]
        ll[i] = ll[lasti]
        ll[lasti] = tmp
        lasti = lasti - 1
        count = count - 1
        i = i + 1
    else:
        print('over')
    print(ll)

#homework1()
#homework3()

#homework3_a([1,2,3,4,5,6])

homework2()
