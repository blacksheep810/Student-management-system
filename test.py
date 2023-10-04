# print('学生姓名'.ljust(15) + '学生ID'.ljust(15) + '英语成绩'.ljust(15) + 'python成绩'.ljust(15) + 'Java成绩'.ljust(15) + '\n')
# print('gong'.ljust(17)+'2022'.ljust(17)+'98'.ljust(17)+'67'.ljust(17)+'97'.ljust(17))
# import os.path
# print(os.path.exists('student.txt'))
# dict = {'heihei':2022,'hello':2021}
# list=[]
# list.append(dict)
# print(list)
# file = open("student.txt",'r')
# lst = file.readlines()
# for item in lst[1:]:
#     # print(item,type(item))
#     lst= item.split()
#     print(lst)
# file1 = open('student.txt', 'r')
# Lst = file1.readlines()
# for item in Lst[1:]:
#     lst = item.split()
#     print(lst[1])
# while True:
#         a = input("请输入你要删除的学生的ID")
#         flag = -1
#         flag1 = -1
#         new_lst = []
#         file = open('student.txt','r')
#         lst = file.readlines()
#         for item in lst:
#             flag += 1
#             lst1 = item.split()
#             if a == lst1[1]:
#                 flag1 = flag
#         if flag1!= -1:
#             for i in range(0,flag1):
#                 new_lst.append(lst[i])
#             for i in range(flag1+1,flag+1):
#                 new_lst.append(lst[i])
#             file1 = open('student.txt','w')
#             for item in new_lst:
#                 file1.write(item)
#             answer = input('请问是否需要继续删除？y/n')
#             if answer == 'y' or answer == 'Y':
#                 continue
#             else:
#                 print("-----------------正在退出删除模块-----------------")
#                 break
#         else:
#             print('所输入的学生ID不存在，请重新输入')
#             continue
filename = 'student.txt'
# def read(filename):
#     file = open(filename,'r')
#     lst = file.readlines()
#     new_list = []
#     for item in lst[1:]:
#          new_list.append(item.split())
#     return new_list
# def insert():
#     file = open(filename, 'a+')
#     import os.path
#     if not os.path.getsize(filename):
#         file.write('学生姓名'.ljust(15) + '学生ID'.ljust(15) + '英语成绩'.ljust(15) + 'python成绩'.ljust(
#             15) + 'Java成绩'.ljust(15) + '\n')
#     else:
#         file.write('\n')  # 由于a+是从文件末尾开始写内容的，这里我判断文件内容是否为空，
#         # 如果为空，写上我们的标题，如果不为空，则添加换行符，便于从另一行开始写我们的文件内容
#
#     while True:
#         '''这里我们输入学生信息，我都采用这种方法，这有两个好处：
#                 1.首先我们知道类型转换只能大转小，所以我们利用try和except方法，一旦用户输入的内容不合规矩，比如我们需要整数ID,用户输入小数或者字符串，就会引发异常机制
#                 2.这样我们还可以输入无数次，直到用户输入正确位置
#         '''
#         name = input("请输入学生姓名")
#         if name == ' ':
#             print("输入不能为空，请重新输入")
#             name = input("请输入学生姓名")
#         while True:
#             try:
#                 ID = int(input("请输入学生ID："))
#                 flag = 0
#                 f = open('student.txt','r')
#                 lst = f.readlines()
#                 for item in lst[1:]:
#                     lst1 = item.split()
#                     if ID == int(lst1[1]):    # 这个地方很坑，lst[1]是一个字符串，我没意识到,拿它和整数在比，导致一直返回false
#                         # int()可以转换数字串为整数，不能转换字符串，这里int()转换lst[1]或者str转换id都可以
#                         flag = 1
#                 if flag == 1:
#                     print("ID重复，请重新输入")
#                     continue
#                 else:
#                     break
#             except ValueError:
#                 print("无效的输入，请重新输入正确的ID。")
#         # 在此之后可以使用变量ID对学生ID进行操作，确保它是一个有效的整数值。
#         while True:
#             try:
#                 score1 = float(input("请输入学生英语成绩："))
#                 break
#             except ValueError:
#                 print("无效的输入，请重新输入正确的成绩。")
#         while True:
#             try:
#                 score2 = float(input("请输入学生python成绩："))
#                 break
#             except ValueError:
#                 print("无效的输入，请重新输入正确的成绩。")
#         while True:
#             try:
#                 score3 = float(input("请输入学生Java成绩："))
#                 break
#             except ValueError:
#                 print("无效的输入，请重新输入正确的成绩。")
#         lst = [name, ID, score1, score2, score3]
#         for item in lst:
#             file.write(str(item).ljust(17))
#         flag1 = input("请问要继续输入吗y/n")
#         if flag1 == 'y' or flag1 == 'Y':
#             file.write('\n')
#             continue
#         else:
#             file.close()
#             break


# while 1:
#     a = input('输入id')
#     new_lst = []
#     for item in read('student.txt'):
#         new_lst.append(item)
#         if a==item[1]:
#             new_lst1 = []
# #             insert()
# lst =[]
# lst1=['ss',123]
# for item in lst1:
#     lst.append(item)
# print(lst)

# file = open('student.txt','r')
# lst = file.readlines()
# new_list = []
# for item in lst[1:]:
#     new_list.append(item.split())
# #print(new_list)
# for item in new_list:
#     print(str(item))

# file = open('student.txt', 'w')
# while 1:
#     a = input('请输入学生ID')
#     flag = 0
#     for item in main.read(filename):
#         if a == item[1]:
#             new_lst = []
#             for i in mainmodify_insert():
#                 new_lst.append(i)
#             flag = 1
#         else:
#             for i in item:
#                 new_lst.append(i)
#     if not flag:
#         print('输入的学生ID不存在')
#     else:
#         break
#
# file = open('student.txt','r')
# lst = file.readlines()
# print(lst)
# new_list = []
# for item in lst[1:]:
#     new_list.append(item.split())
# print(new_list)



