filename = 'student.txt'
import time


def main():
    while True:
        menu()
        try:
            choice = int(input("请选择"))
        except BaseException:
            print('输入字符不能为空，请重新输入')
            continue
        else:
            if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
                if choice == 0:
                    answer = input("您确定要退出系统吗？y/n")
                    if answer == 'y' or answer == 'Y':
                        print("谢谢您的使用")
                        break
                    else:
                        continue
                elif choice == 1:
                    insert()
                elif choice == 2:
                    search()
                elif choice == 3:
                    delete()
                elif choice == 4:
                    modify()
                elif choice == 5:
                    sort()
                elif choice == 6:
                    total()
                elif choice == 7:
                    show()
            else:
                print("输入错误，请重新输入")


def read(str):
    file = open(str, 'r')
    lst = file.readlines()
    new_list = []
    for item in lst[1:]:
        new_list.append(item.split())
    file.close()
    return new_list


# 这个函数用于返回一个列表，存储了文件的数据，每一行的内容都是一个列表，父列表的元素依旧是存储了每一行内容的子列表

def modify_insert():
    while True:
        '''这里我们输入学生信息，我都采用这种方法，这有两个好处：
                1.首先我们知道类型转换只能大转小，所以我们利用try和except方法，一旦用户输入的内容不合规矩，比如我们需要整数ID,用户输入小数或者字符串，就会引发异常机制
                2.这样我们还可以输入无数次，直到用户输入正确位置
        '''
        name = input("请输入学生姓名")
        if name == ' ':
            print("输入不能为空，请重新输入")
            name = input("请输入学生姓名")
        while True:
            try:
                ID = int(input("请输入学生ID："))
                flag = 0
                f = open('student.txt', 'r')
                lst = f.readlines()
                for item in lst[1:]:
                    lst1 = item.split()
                    if ID == int(lst1[1]):  # 这个地方很坑，lst[1]是一个字符串，我没意识到,拿它和整数在比，导致一直返回false
                        # int()可以转换数字串为整数，不能转换字符串，这里int()转换lst[1]或者str转换id都可以
                        flag = 1
                if flag == 1:
                    print("ID重复，请重新输入")
                    continue
                else:
                    break
            except ValueError:
                print("无效的输入，请重新输入正确的ID。")
        # 在此之后可以使用变量ID对学生ID进行操作，确保它是一个有效的整数值。
        while True:
            try:
                score1 = float(input("请输入学生英语成绩："))
                break
            except ValueError:
                print("无效的输入，请重新输入正确的成绩。")
        while True:
            try:
                score2 = float(input("请输入学生python成绩："))
                break
            except ValueError:
                print("无效的输入，请重新输入正确的成绩。")
        while True:
            try:
                score3 = float(input("请输入学生Java成绩："))
                break
            except ValueError:
                print("无效的输入，请重新输入正确的成绩。")
        lst = [name, ID, score1, score2, score3]
        break
    return lst


def menu():
    print("=====================学生信息管理系统==========================")
    print("------------------------功能菜单------------------------------")
    print('\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t5.排序')
    print('\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t0.退出')
    print('-------------------------------------------------------------')


def insert():
    file = open(filename, 'a+')
    import os.path
    if not os.path.getsize(filename):
        file.write('学生姓名'.ljust(15) + '学生ID'.ljust(15) + '英语成绩'.ljust(15) + 'python成绩'.ljust(
            15) + 'Java成绩'.ljust(15) + '\n')
    else:
        file.write('\n')  # 由于a+是从文件末尾开始写内容的，这里我判断文件内容是否为空，
        # 如果为空，写上我们的标题，如果不为空，则添加换行符，便于从另一行开始写我们的文件内容
    while True:
        lst = modify_insert()
        for item in lst:
            file.write(str(item).ljust(17))
        flag1 = input("请问要继续输入吗y/n")
        if flag1 == 'y' or flag1 == 'Y':
            file.write('\n')
            continue
        else:
            file.close()
            break


def search():
    try:
        while True:
            a = input("请输入学生ID,查找学生信息")
            flag = 0
            file1 = open(filename, 'r')
            Lst = file1.readlines()
            for item in Lst[1:]:
                lst = item.split()
                #    print('--------{0}-------'.format(lst[1]))
                if a == lst[1]:
                    print(lst)
                    flag = 1
                    break
                else:
                    continue
            if flag == 0:
                print("未找到学生信息，请重新输入")
                continue
            else:
                answer = input("请问你需要继续查找吗？y/n")
                if answer == 'y' or answer == 'Y':
                    continue
                else:
                    print("查询完成，感谢您的使用")
                    file1.close()
                    break

    except IOError:
        print("文件不存在，请先录入学生信息")


def delete():
    while True:
        a = input("请输入你要删除的学生的ID")
        flag = -1
        flag1 = -1
        new_lst = []
        file = open('student.txt', 'r')
        lst = file.readlines()
        for item in lst:
            flag += 1
            lst1 = item.split()
            if a == lst1[1]:
                flag1 = flag
        if flag1 != -1:
            for i in range(0, flag1):
                new_lst.append(lst[i])
            for i in range(flag1 + 1, flag + 1):
                new_lst.append(lst[i])
            file1 = open('student.txt', 'w')
            for item in new_lst:
                file1.write(item)
            answer = input('请问是否需要继续删除？y/n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                print("-----------------正在退出删除模块-----------------")
                time.sleep(2)
                file.close()
                file1.close()
                break

        else:
            print('所输入的学生ID不存在，请重新输入')
            continue


def modify():
    while 1:
        a = input('请输入学生ID')
        flag = 0
        new_lst = []
        for item in read(filename):
            if a == item[1]:
                new_lst.append(modify_insert())
                flag = 1
            else:
                new_lst.append(item)
        # print(new_lst)
        file = open(filename, 'w')
        file.write('学生姓名'.ljust(15) + '学生ID'.ljust(15) + '英语成绩'.ljust(15) + 'python成绩'.ljust(
            15) + 'Java成绩'.ljust(15) + '\n')
        for item in new_lst:
            for i in item:
                file.write(str(i).ljust(17))
            file.write('\n')
        if not flag:
            print('输入的学生ID不存在')
        else:
            answer = input('请问你是否需要继续修改？y/n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                print('-------------------正在退出--------------------')
                time.sleep(2)  # 这段代码是停下来两秒钟在运行下部分代码
                file.close()
                break


def sort_index(a,lst):
    n = len(lst)
    indicate = list(range(len(lst)))  # 生成索引列表
    if a == 1:
        for i in range(0, n - 1):  # 这里为什么是n-1，因为冒泡排序只需要比较列表长度-1轮，最小的元素浮出水面后就不需要继续比较了
            for j in range(0, n - 1 - i):
                # 每一轮冒泡结束，都会有一个参与排序的数中的最大的数冒出来，因此，每次参与排序的数都会减少
                if float(lst[indicate[j]]) > float(lst[indicate[j+1]]):

                    indicate[j],indicate[j+1] = indicate[j+1],indicate[j]
    elif a==0:
        # 升序，大的值索引在前
        for i in range(0, n - 1):  # 这里为什么是n-1，因为冒泡排序只需要比较列表长度-1轮，最小的元素浮出水面后就不需要继续比较了
            for j in range(0, n - 1 - i):
                # 每一轮冒泡结束，都会有一个参与排序的数中的最大的数冒出来，因此，每次参与排序的数都会减少
                if float(lst[indicate[j]]) < float(lst[indicate[j+1]]):
                    indicate[j],indicate[j+1] = indicate[j+1],indicate[j]

    return indicate








def sort():
    show()
    lst = read(filename)
    while True:
        try:
            a = int(input('请选择排序方式（0升序，1降序）'))
            b = int(input('请选择排序标准：1.按英语成绩，2，按python成绩，3，按Java成绩，4，按总成绩'))
            if a in range(0,2) and b in range(1,5):
                break
            else:
                print('输入的值未按照要求，请重新输入')
                continue
        except ValueError:
            print('输入的值未按照要求，请重新输入')
            continue
    lst1 = []  # 英语成绩
    lst2 = []  # python成绩
    lst3 = []  # Java成绩
    lst4 = []  # 总成绩
    n = len(lst1)
    for item in lst:
        lst1.append(item[2])
        lst2.append(item[3])
        lst3.append(item[4])
        lst4.append(float(item[2]) + float(item[3]) + float(item[4]))
    # print(lst1, lst2, lst3, lst4)
    print('学生姓名'.ljust(17) + '学生ID'.ljust(17) + '英语成绩'.ljust(17) + 'python成绩'.ljust(17) + 'Java成绩'.ljust(
        17) + '\n')
    if b==1:
        for i in sort_index(a, lst1):
            for item in lst[i]:
                print(item.ljust(20),end='')
            print('\n')
    elif b==2:
        for i in sort_index(a, lst2):
            for item in lst[i]:
                print(item.ljust(20), end='')
            print('\n')
    elif b==3:
        for i in sort_index(a, lst3):
            for item in lst[i]:
                print(item.ljust(20), end='')
            print('\n')
    elif b==4:
        for i in sort_index(a, lst4):
            for item in lst[i]:
                print(item.ljust(20), end='')
            print('\n')




def total():
    print('--------------------正在进入查询模块-------------------------')
    print('共登记有学生{0}名'.format(len(read(filename))))


def show():
    lst = read(filename)
    print('学生姓名'.ljust(17) + '学生ID'.ljust(17) + '英语成绩'.ljust(17) + 'python成绩'.ljust(17) + 'Java成绩'.ljust(
        17) + '\n')
    for item in lst:
        for i in item:
            print(i.ljust(17), end='\t')
        print('\n')
    print('----------------查询完毕-----------------')
    time.sleep(2)


main()
