import os
while True:
    cl=input('$')
    if cl=='ls':
        cur_path=os.getcwd()
        for i in os.listdir(cur_path):
            print(i,end=' ')
        print()
    #cd xxxxxx
        #文件名，有就直接进入，没有就返回错误
    #cp 源文件 目标路径
    #history n ：列出历史n调命令
    #touch xxx.txt:创建一个txt文件
    #vim xxx.txt：编辑,往里面写东西
    #cat xxx.txt:输出文件里面的东西