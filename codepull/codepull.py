'''
@Author: your name
@Date: 2020-02-08 15:24:09
@LastEditTime : 2020-02-10 17:22:40
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /vscode_scripts/home/echo/learngit/codepull/codepull.py
'''
import os
import time
import random
from string import digits
import qrcode
import tkinter
from pystrich.ean13 import EAN13Encoder
import tkinter.messagebox
import tkinter.filedialog
import tkinter as tk

root = tk.Tk()
number = "1234567890"
letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
allis = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"
codepath = r"/home/echo/learngit/codepull/codepath"
codeadd = r"/home/echo/learngit/codepull/codeadd"
barcode = r"/home/echo/learngit/codepull/barcode"
qrcode = r"/home/echo/learngit/codepull/qrcode"
i = 0 

randstr = []
randfir = ""
randsec = ""
randthr = ""
userinput = ""


def mkdir(path):
    """ 判断文件夹是否存在，不存在则创建该资料夹"""
    is_exists = os.path.exists(path)
    if not is_exists:
        os.mkdir(path)
        
def openfile(filename):
    with open(filename, 'r') as f:
        f_list = f.read()
        return f_list
    
def inputbox(showstr, showorder, length):
    """
    判断输入的string格式是否符合要求和长度要求，
    showstr:提示用户输入的信息
    showorder: 验证方式 1-大于0的整数   2-字母，长度由length决定   3-数字，长度由length决定
    length: 指定string的长度
    """
    instr = input(showstr)
    if len(instr) != 0:
        if showorder == 1:
            if instr.isdigit():
                if instr == 0:
                    print("\033[1;31;40 输入的数字不可为0，请重新输入! \033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40 输入的内容要为数字，请重新输入!\033[0m")
                return "0"
        elif showorder == 2:
            if instr.isalpha():
                if len(instr) != length:
                    print("\033[1;31;40 输入的字符长度不符合要求，请重新输入!\033[0m")
                    return "0"
                else:
                    return instr
            else:
                print("\033[1;31;40 输入的内容要为字母，不符合要求，请重新输入!\033[0m")
                return "0"
        elif showorder == 3:
            if instr.isdigit():
                if len(instr) != length:
                    print("\033[1;31;40 您输入的数字长度不符合要求，请重新输入!\033[0m")
                    return "0"
                else:
                    retrun instr
            else:
                print("\033[1;31;40 您输入的内容不是数字，请重新输入!\033[0m")
                return "0"
    else:
        print("\033[1;31;40 输入的内容不可为空，请重新输入\033[0m")
        return "0"

def wfile(sstr, sfile, typeis, smsg, datapath,count):
    """
    在特定的资料夹内将列表内的内容写入到对应的文件内，写入完成后后显示条形码的内容
    并且在对话框中显示已完成
    sstr: 含有条形码的列表
    sfile: 待写入条形码的文件名
    typeis: "":表示显示完成的对话框，"no": 不显示完成的对话框
    smsg: 对话框提示的内容
    datapath: 写入条形码对应的文件路径
    count: 生成验证码的数量
    """
    mkdir(datapath)
    file = datapath + '/' + sfile
    with open(file, 'a+') as f:
        wrlist = sstr
        pdata = ""
        for i in range(len(wrlist)):
            f.write(str(wrlist[i] + "\n"))
            pdata += str(wrlist[i])
    print("\033[1;31m" + pdata +  "\033[0m"）
    if typeis != "no":
        tk.messagebox.showinfo("提示", smsg + str(len(wrlist)) + "\n 防伪码存放位置: " + filename)
        root.withdraw()

def scompare(sstr,file):
    """
        比较验证码是否有重复，无重复就返回该验证码，否则返回"0"
        sstr:  验证码
        file:  验证码保存文件的列表
    """
    if os.path.exists(file):
        with open(file, 'r') as f:
            mark = True
            for i in f:
                if i == sstr:
                    mark = False
                    break
        if mark == False:
            return "0"
        else:
            return sstr
    else:
        return sstr

def scode1(schoice):
    """生成6位数防伪码"""
    counter = 0
    file = "scode" + schoice + ".txt"
    in_count = inputbox("\033[1;31m 请输入需要生成6位验证码的数量:  \033[0m", 1, 0)
    while int(in_count) == 0:
        in_count = inputbox("\033[1;31m 请输入需要生成6位验证码的数量:  \033[0m", 1, 0)
    randstr.clear()
    while int(in_count) >= counter:
        randfir = ""
        for i in range(6):
            randfir += random.choice(number)
        if scompare(randfir, file) != "0":
            randstr.append(randfir)
            counter += 1
    smsg = "已生成6位验证码共计: "
    wfile(randstr, file, "", smsg, codepath)
    
def scode2(schoice):
    """生成9位防伪码，前三位为产品系列码."""
    counter = 0
    file = "scode" + schoice + ".txt"
    smsg = "已生成的9位验证码数量为: "
    code_start = inputbox("\033[1; 31m 请输入产品系列的数字起始码(3位): \033[0m", 1, 3) 
    while int(code_start) == 0:
        code_start = inputbox("\033[1; 31m 请输入产品系列的数字起始码(3位): \033[0m", 1, 3)
    in_count = inputbox("\033[1;31m 请输入需要生成9位验证码的数量:  \033[0m", 1, 0)
    while int(in_count) == 0:
        in_count = inputbox("\033[1;31m 请输入需要生成9位验证码的数量:  \033[0m", 1, 0)
    randstr.clear()
    while (int(in_count)) >= counter:
        randfir = ''
        for i in range(6):
            randfir += random.choice(number)
        randfir = code_start + randfir
        if scompare(randfir, file) != "0"
            counter += 1
            randstr.append(randfir)
    wfile(randstr, file, "", smsg, codepath)
    
def scode3(schoice):
    """生成25位字母数字组成的验证码"""
    counter = 0
    file = "scode" + schoice + ".txt"
    smsg = "已生成的25位防伪码数量为:  "
    in_count = inputbox("\033[1;31m 请输入需要生成25位验证码的数量:  \033[0m", 1, 0)
    while int(in_count) == 0:
        in_count = inputbox("\033[1;31m 请输入需要生成25位验证码的数量:  \033[0m", 1, 0)
    randstr.clear()
    while int(in_count) >= counter:
        randfir = ''
        for i in range(25):
            randfir += random.choice(letter)
        randsec = randfir[0:5] + '-' + randfir[5:10] + '-' + randfir[10:15] + '-' + randfir[15:20] + '-' + randfir[20:25]
        if scompare(randsec, file) != "0":
            randstr.append(randsec)
            counter += 1
    wfile(randstr, file, "", smsg, codepath)
    
def scode4(schoice):
    """
    生成12位智能数据验证码，其中3位为字母,字母位置随机
    字母第一位:地区
    字母第二位:颜色
    字母第三位:级别
    """
    counter = 0
    in_type = inputbox("\033[1;31m 请输入3位数据分析验证码的值(ex:abc):  \033[0m", 2, 3)
    while len(in_type) != 3:
        in_type = inputbox("\033[1;31m 请输入3位数据分析验证码的值(ex:abc):  \033[0m", 2, 3)
    in_count = inputbox("\033[1;31m 请输入需要生成12位智能数据验证码的数量:  \033[0m", 1, 0)
    while int(in_count) == 0:
        in_count = inputbox("\033[1;31m 请输入需要生成12位智能数据验证码的数量:  \033[0m", 1, 0)
    ff_code(in_type, in_count)
    
ff_code(in_type, in_count, schoice):
    """
    根据字母验证码及验证码的数量，生成12位的智能数据分析验证码
    in_type: 验证码智能验证的值，共三位，第一位代表地区，第二位代表颜色，第三位代表产品级别，字母位置随机
    in_count:验证码生成的数量
    """
    counter = 0
    file = 'scode' + schoice + ".txt"
    smsg = "已生成的12为智能数据验证码的数量为:  "
    randstr.clear()
    first = in_type[0].upper()
    second = in_type[1].upper()
    third = in_type[2].upper()
    position = random.sample(number, 3)
    while int(in_count) >= counter:
        randfir = ''
        for i in range(9):
            randfir += random.choice(number)
        randsec = randfir[0:int(position[0])] + first + randfir[int(position[0]):int(positon[1])] + second + randfir[int(position[1]):int(position[2])] + third + randfir[int(position[2]:9)]
        if scompare(randsec, file) != "0":
            randstr.append(randsec)
            counter += 1
    wfile(randstr, file, "", smsg, codepath)

def scode5(schoice):
    default_file = r"/home/echo/learngit/collpull/mrsoft.mri"
    file_path = tk.filedialog.askopenfile(filetypes=[("Text file", "*.mri")],title=u"请选择自动防伪码智能批处理文件:  ", initialdir=(os.path.expanduser(default_file))
    codelist = openfile(file_path)
    for item in codelist:
        itema = item.split()[0]
        itemb = item.split()[1]
        ff_code(itema, itemb, schoice="4")

def scode6(schoice):
    """
        根据输入的国家代码，企业代码及数量生成EAN13条形码
    """
    counter = 0    
    file = scode + schoice + ".txt"       
    smsg = "EAN13条形码生成的数量为:  "                 
    country_code = inputbox("请输入EAN13条形码的国家代码:  ", 3, 3)
    while country_code == "0":
        country_code = inputbox("请输入EAN13条形码的国家代码:  ", 3, 3)
    corp_code = inputbox("请输入EAN13条形码的企业代码:  ", 3, 4)
    while corp_code == "0":
        corp_code = inputbox("请输入EAN13条形码的企业代码:  ", 3, 3)
    quantity = inputbox("请输入生成EAN13条形码的数量:  ", 1, 0)
    while quantity == "0":
        quantity = inputbox("请输入生成EAN13条形码的数量:  ", 1, 0)
    randstr.clear()
    while quantity >= counter:
        randfir = ""
        for i in range(5):
            randfir += random.choice(number)
        randfir = country_code + corp_code + randfir
        evennum = int(randfir[1]) + int(randfir[3]) + int(randfir[5]) + int(randfir[7]) + int(randfir[9]) + int(randfir[11])
        oddnum = int(randfir[0]) + int(randfir[2]) + int(randfir[4]) + int(randfir[6]) + int(randfir[8]) + int(randfir[10])   
        checkbit = (10 - ((oddnum*3 + evennum)%10)%10)
        randfir += str(checkbit)
        if barcode_check(randfir, barcode) != "0":
            bar_code = EAN13Encoder(randfir)
            bar_code.save(barcode + '/' + 'randfir' + ".png")
            
def barcode_check(sstr, barcode):
    mkdir(barcode)
    mark = True
    for root,dirs,files in os.walk(barcode):
        filenames = files
    for fname in filenames:
        fname = fname.split('.')[0]
            if fname == sstr:
                mark = False
                break
    if mark == False:
        return "0"
    else:
        return sstr
                
                

def scode7(schoice):
    """
    生成qrcode,并保存到固定的路径.
    """
    counter = 0
    in_count = inputbox("请输入qrcode二维码的国家代码:  ", 3, 3)
    while in_count == "0":
        in_count = inputbox("请输入qrcode二维码的国家代码:  ", 3, 3)
    mkdir(qrcode)
    while int(in_count) >= counter:
        strone = ''
        for i in range(12):
            strone += random.choice(number)
        if barcode_check(strone, qrcode) != "0":
            encoder = qrcode.make(strone)
            encoder.save(qrcode + '/' + 'strone' + '.png')

def lottery():
    file = r"lottery.ini"
    file_path = tk.filedialog.askopenfilename(filetypes=[("Ini file", "*.ini")], title=u"请选择包含抽奖号码的文件: ", initialdir=(os.path.expanduser(file)))
    codelist = openfile(file_path)
    
            
def menu():
    """
    ----------------------------------------------------------------------------------------------------
    ---------------------                    企业编码生成系统                       ----------------------
    |
    |                            1.生成6位数字防伪码(ex:213456)
    |                            2.生成9位系列产品数字防伪码(ex:23682392)
    |                            3.生成25位混合产品序列号(xxxxx-xxxxx-xxxxx-xxxxx-xxxxx)
    |                            4.生成含数据分析功能的防伪码(ex:234U23S999I2)
    |                            5.智能批量生成含数据分析功能的防伪码(ex:234U23S999I2)
    |                            6.EAN-13条形码批量生成
    |                            7.二维码批量输出
    |                            8.企业粉丝抽奖
    |                            0.退出系统
    |---------------------------------------------------------------------------------------------------
    """
        