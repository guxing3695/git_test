'''
@Author: your name
@Date: 2020-01-27 14:54:46
@LastEditTime : 2020-02-06 23:30:08
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /vscode_scripts/test.py
'''
import os
import sys
import re

filename = r"/home/echo/learngit/student.txt"

def menu():
    print(
        """
        #############################################################################################
        #####                                学生信息管理系统                                      #####
        #########################################功能菜单#############################################
        #                   1. insert student info
        #                   2. query  student info
        #                   3. delete student  info
        #                   4. modify student info
        #                   5. 排序
        #                   6. 统计学生总人数
        #                   7. 显示所有学生信息
        #                   0. 退出系统
        #############################################################################################
        说明：通过数字选择菜单
        """
          )

def save(studentlist):
    """save student info into local storage"""
    try:
        f = open(filename, "a")
    except Exception as e:
        f = open(filename, "w")
    for line in studentlist:
        f.write(str(line) + "\n")
    f.close()
    
def typeJudge(strName):
    if strName is not "":
        if strName.isalnum():
            typename = "alnum"    #typename 为数字和字符组成
        elif strName.isdigit():
            typename = "digit"    #typename由数字组成
        elif strName.isalpha():
            typename = "alpha"    #typename由字符组成
    else:
        typename="zero"  # strName is null        
    return typename
                
def insert():
    """
    新增学生信息
    """
    studentlist = []
    student_old = []
    mark = True
    modify_mark = True
    while mark:
        id = input("请输入学生id(如1001)： ")
        name = input("请输入学名姓名: ")
        english_score = input("请输入学生英语成绩: ")
        python_score = input("请输入学生python成绩: ")
        id = id.strip()
        name = name.strip()
        english_score = english_score.strip()
        python_score = python_score.strip()
        if not id or not name or not english_score or not python_score:
            print("学生相关信息不能为空!")
            continue
        if not id.isalnum() or not name.isalpha() or not english_score.isdigit() or not python_score.isdigit():
            print("学生信息要符合规范")
            continue
        for line in studentlist:
            if id == line['id']:
                modify_mark=False
                print("学生id号不能重复，请重新输入。")
                break
        with open(filename,'r') as f:
            students = f.readlines()
            for line in students:
                student_old.append(eval(line))
        for line in student_old:
            if id == line['id']:
                modify_mark=False
                print("学生id号不能重复，请重新输入。")
                break
        if modify_mark == True:
            student={"id": id,"name": name, "python": python_score, "english": english_score}
            studentlist.append(student)
        inputMark = input("是否继续输入(Y/N):")
        if inputMark == "y" or inputMark == "Y":
            mark = True
        else:
             mark = False
    save(studentlist)
    print("学生信息录入完毕!") 
        

def query():
    mark = True
    student_query = []
    while mark:
#        id = ""
#        name = ""
        if os.path.exists(filename):
            mode=input("按id查询请按1，按name查询请按2: ")
            if mode == "1":
                id = input("请输入学生id号: ")
            elif mode == "2":
                name = input("请输入学生姓名: ")
            else:
                print("输入错误，请重新输入！！！")
                query()
            with open(filename, "r") as f:
                student = f.readlines()
                for list in student:
                    d = dict(eval(list))
                    if id is not "":
                        if d['id'] == id:
                            student_query.append(d)
                    elif name is not "":
                        if d['name'] == name:
                            student_query.append(d)
            show_student(student_query)
            student_query.clear()
            inputMark = input("是否继续查询，请输入(Y/N):  ")
            if inputMark == 'y' or inputMark == 'Y':
                mark = True
            else:
                mark = False
        else:
            print("暂无保存任何数据信息.")
            return

def delete():
    '''delete student info by student id.'''
    mark = True  #circle mark
    student_delete = []
    while mark:
        studentId = input("请输入要删除的学生id: ")
        stype = typeJudge(studentId)
        if stype == "alnum":             
            #studentId字符类型为数字及字符    
            if os.path.exists(filename):
                with open(filename,'r') as rfile:
                    studentOld = rfile.readlines()
            else:
                studentId = []
            ifDel = False
            if studentOld:
                with open(filename, 'w') as wfile:
                    d = {}
                    for list in studentOld:
                        d = dict(eval(list))
                        if d['id'] != studentId:
                            wfile.write(str(d)+"\n")
                        else:
                            student_delete.append(eval(list))
                            ifDel = True
                print("下面为要删除的信息，请确认是否删除(y/n)")
                show_student(student_delete)
                del_mark = input("请确认是否需要删除(y/n):  ")
                if del_mark == 'y' or del_mark == 'Y':    
                    if ifDel:
                        print("学生ID为%s的学生信息已删除." % studentId)
                    else:
                        print("未找到学生ID为%s的学生信息." % studentId)
        elif stype == "zero":
            print("无学生信息!")
            break
        else:
            print("输入的信息为无效信息，请重新输入.")
            continue
        inputMark = input("是否继续删除学生(y/n)")
        if inputMark == 'y' or inputMark == 'Y':
            mark = True    # continue to delete
        else:
            mark = False    #stop to delete
            

def show_student(querylist):
    '''显示查询到的学生信息'''
    if not querylist:
        print("None data info")
        return
    format_title = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}"
    print(format_title.format("id", "name", "english_score", "python_score", "total"))
    format_data = "{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}"
    for line in querylist:
        id=line['id']
        name=line['name']
        python_score=line['python']
        english_score=line['english']
        sum_score=int(python_score)+int(english_score)
        print(format_data.format(id,name,english_score,python_score,sum_score))
        
def modify_student():
    '''修改学生信息'''
    mark = True
    smark = True
    while mark:
        studentId = input("请输入要修改的学生id: ")
        strtype = typeJudge(studentId)
        if strtype == "alnum":
            d = []
            with open(filename,'r') as fread:
                studentMod = fread.readlines
                if studentMod is not "":
                    for line in studentMod:
                        student=dict(eval(line))
                        d.append(student)
                else:
                    print("无学生信息")
                    break
            while smark:
                studentNewId = input("请输入修改的学生id: ")
                studentName = input("请输入修改的学生姓名: ")
                english_score_new = input("请输入修改的英语成绩: ")
                python_score_new = input("请输入修改的python成绩: ")
            if not studentNewId or not studentName or not english_score_new or not python_score_new:
                print("您输入的信息含有空的数据，请重新输入.")
                smark = True
                continue
            elif studentNewId.isalnum() and studentName.isalpha() and english_score_new.isdigit() and python_score_new.isdigit():
                for line in d:
                    if line['id'] == studentId:
                        line['id']=studentNewId
                        line['name']=studentName
                        line['english_score']=english_score_new
                        line['python_score']=python_score_new
                    else:
                        print("未查询到该学生的信息.请确认学生的id号是否正确.")
            remark = input("是否继续修改学生的信息(y/n)")
            if remark == 'y' or remark == 'Y':
                mark = True
            else:
                mark = Fale
                save(d)    

def sort():
    '''排序显示'''
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            student_old = f.readlines()
            student_new = []
        for list in student_old:
            d = dict(eval(list))
            student_new.append(d)
    else:
        return
    order = input("请选择排序方式(0：升序， 1：降序):  ")
    if order == 0:
        orderBool = False
    elif order == 1:
        orderBool = True
    else:
        print("您的输入有误，请重新输入.")
        sort()
    mode = input("请选择排序方式(1.按英语成绩 2.按python成绩 3.按总成绩 4.按学生id)")
    if mode == "1": 
        sorted(student_new, key=lambda x: x["english_score"], reverse=orderBool )
    elif mode == "2":
        sorted(student_new, key=lambda x: x["python_score"], reverse=orderBool)
    elif mode == "3":
        sorted(student_new, key=lambda x: x["english_score"] + x["python_score"], reverse=orderBool)
    elif mode == "4":
        sorted(student_new, key=lambda x: x["id"], reverse=orderBool)
    else:
        print("您的输入有误，请重新输入.")
        sort()
    show_student(student_new)   #display the result by sort
    
def sumStudent():
    '''显示总的学生人数'''
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            student_old = f.readlines()
            if studentlist is not "":
                totalStudent = len(student_old)
                print("一共有%d名学生。" % totalStudent)
            else:
                print("无学生信息.")
                
def show():
    '''显示总的学生详细信息'''
    student_new = []
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            student_old = f.readlines()
            for line in student_old:
                student_new.append(eval(line))
            if student_new:
                show_student(student_new)
    else:
        print("暂未保存数据信息")
        
def main():
    ctrl = True
    while ctrl:
        menu()
        option = input("请选择功能菜单:  ")
        option_str = re.sub("\D", "", option)
#        optionType = typeJudge(option)
#        if optionType == "alpha":
        if option in ['0','1','2','3','4','5','6','7']:
            option_int=int(option)
            if option_int == 0:
                print("您已退出学生管理系统.")
                ctrl = False
            elif option_int == 1:
                insert()
            elif option_int == 2:
                query()
            elif option_int == 3:
                delete()
            elif option_int == 4:
                modify()
            elif option_int == 5:
                sort()
            elif option_int == 6:
                sumStudent()
            elif option_int == 7:
                show()
                    
if __name__ == "__main__":
    main()