import os
def start():
    while True:
        cl=input('$')
        if cl=='ls':
            cur_path=os.getcwd()
            for i in os.listdir(cur_path):
                print(i,end=' ')
            print()
        elif cl[0] == 'c' and cl[1] == 'd': 
            a = cl.split()
            b = []
            b=os.getcwd()
            if a[1] in os.listdir(os.getcwd()):
                    os.chdir(a[1])
                    
            else:
                print('file not found')

        if cl[0:4] == 'file':
            if cl[5:10] == 'touch':
                  open(cl[11:], x)
            elif cl[5:8] == 'vim':
                  edit = os.open('/Users/jennywu/Documents/用所选项目新建的文件夹/' + cl[9:], os.O_RDWR)
                  write = input('edit:')
                  print(type(write))
                  os.write(edit, write)
                  os.close(edit)
            elif cl[5:8] == 'cat':
                a = '/Users/jennywu/Documents/用所选项目新建的文件夹/'+ cl[9:]
                print(a)
                print(open(a).read())
                

            
#cd xxxxxx
#文件名，有就直接进入，没有就返回错误
#cp 源文件 目标路径
#history n ：列出历史n调命令
#touch xxx.txt:创建一个txt文件
#vim xxx.txt：编辑,往里面写东西
#cat xxx.txt:输出文件里面的东西a
start()


