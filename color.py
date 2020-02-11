'''
@Author: your name
@Date: 2020-02-09 11:51:06
@LastEditTime : 2020-02-10 21:49:45
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /vscode_scripts/home/echo/learngit/color.py
'''
"""
#  \033[显示方式;前景色；背景色m需要显示的文字\033[0m
1、显示方式：
0（默认）、1（高亮）、22（非粗体）、4（下划线）、24（非下划线）、 5（闪烁）、25（非闪烁）、7（反显）、27（非反显）
2、前景色：
30（黑色）、31（红色）、32（绿色）、 33（棕色）、34（蓝色）、35（洋 红）、36（青色）、37（白色）
3、背景色:
40（黑色）、41（红色）、42（绿色）、 43（棕色）、44（蓝色）、45（洋 红）、46（青色）、47（白色）


print("\033[5;33;40m helloworld! \033[0m")
print("\033[1;32;47m helloworld \033[0m")

python3 install tkinter method:
sudo apt-get install python3-tk
"""
import os
import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
from pystrich.ean13 import EAN13Encoder
path = r"/home/echo/learngit/codepull/codeauto.mri"
root = tk.Tk()
file_path = tk.filedialog.askopenfilename(filetypes=[("Text file", "*.mri")], title=u"请选择要处理的文件", initialdir=(os.path.expanduser(path)))
with open(file_path,'r') as f:
    file_list = f.read()
#file_list = openfile(file_path)

code_list = file_list.split("\n")
print(code_list)


s = "9301028183401"
encode = EAN13Encoder(s)
encode.save(s + ".png")

sstr = ['239232323.png','282930232.png','234923943.png']
file = r"/home/echo/test"
def filename_trans(sstr, file):
    if not os.path.exists(file):
        os.mkdir(file)
    for root,dirs,files in os.walk(file):
        flist = files
    print(flist)

def main():
    filename_trans(sstr, file)

if __name__ == "__main__":
    main()
