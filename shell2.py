import os


def start():
    while True:
        cl = input('$').split()
        if cl[0] == 'ls':
            cur_path = os.getcwd()
            for i in os.listdir(cur_path):
                print(i, end=' ')
            print()

        elif cl[0] == 'cd':
            if os.path.exists(cl[1]):
                os.chdir(cl[1])
            else:
                print("file doesn't exist")

        if cl[0] == 'touch':
            a = open(cl[1], 'x')
            a.close()
        elif cl[0] == 'vim':
            with open(os.getcwd() + '/' + cl[1], 'a+') as edit:
                while True:
                    a = input(':')
                    if a == 'q':
                        break
                    edit.write(a)
            print('success')

        elif cl[0] == 'cat':
            a = cl[1]
            print(open(a).read())

        elif cl[0] == 'quit':
            quit()
#todo:对于每一个part，尽量以函数的形式编写

# cd xxxxxx
# 文件名，有就直接进入，没有就返回错误
# cp 源文件 目标路径
# history n ：列出历史n调命令
# touch xxx.txt:创建一个txt文件
# vim xxx.txt：编辑,往里面写东西
# cat xxx.txt:输出文件里面的东西a
start()



