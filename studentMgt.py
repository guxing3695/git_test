'''
@Author: your name
@Date: 2020-01-27 14:54:46
@LastEditTime : 2020-02-08 11:21:22
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
            typename = "alpha"
        else:
            typename = "space"    #typename由字符组成
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
        s_type = typeJudge(studentId)
        if s_type == "alnum":             
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
                    if student_delete:
                        print("删除的信息如下：")
                        show_student(student_delete)
                        del_mark = input("请确认是否需要删除(y/n):  ")
                        if del_mark == 'y' or del_mark == 'Y':    
                            if ifDel:
                                print("学生ID为%s的学生信息已删除." % studentId)
                                student_delete.clear()
                            else:
                                print("未找到学生ID为%s的学生信息." % studentId)
                    else:
                        print("您输入的工号未查找到相关数据.")
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
        
'''        
def modify():
    """修改学生信息"""
    mark = True
    smark = True
    fmark = True
    while mark:
        studentId = input("请输入要修改的学生id: ")
        strtype = typeJudge(studentId)
        if strtype == "alnum":
            student_new = []
            with open(filename,'r') as fread:
                student_old = fread.readlines()
                if student_old is not "":
                    for line in student_old:
                        student=dict(eval(line))
                        student_new.append(student)
                else:
                    print("学生信息为空")
                    break
            for line in student_new:
                if studentId == line['id']:
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
                            line['id']=studentNewId
                            line['name']=studentName
                            line['english']=english_score_new
                            line['python']=python_score_new
                            smark=False
                    fmark=True
            if fmark:
                remark = input("是否继续修改学生的信息(y/n)")
                if remark == 'y' or remark == 'Y':
                    mark = True
                else:
                    mark = False
                    save(student_new)
'''

def modify():
    """
        根据输入的学生ID号修改该学生的信息,学生ID号为数字字符型，
    """
    mark=True
    ctrl=True
    f_mark=True
    while mark:
        studentId = input("请输入要修改的学生ID号:  ")
        s_type = typeJudge(studentId)
        if s_type == 'alnum':
            student_new = []
            with open(filename, 'r') as f:
                student_old = f.readlines()
                for line in student_old:
                    line = dict(eval(line))
                    student_new.append(line)
            for li in student_new:
                if li['id'] == studentId:
                    while ctrl:
                        judge = True
                        student_id_new = input("请输入修改后的学生ID:  ")
                        student_name = input("请输入修改后的学生姓名:  ")
                        python_new = input("请输入修改后的python成绩:  ")
                        english_new = input("请输入修改后的english成绩:  ")
                        if student_id_new.isalnum() and student_name.isalpha() and python_new.isdigit() and english_new.isdigit():
                            for line in student_new:
                                if student_id_new == line['id']:
                                    print("修改的学生id号已存在，请重新输入.")
                                    judge = False
                            if judge:
                                li['id'] = student_id_new
                                li['name'] = student_name
                                li['python'] = python_new
                                li['english'] = english_new
                                ctrl = False
                                f_mark = False 
                        else:
                            print("您所输入的内容格式不符合要求的，请检查后重新输入.")
                            continue
                if not f_mark:
                    break
            remark = input("是否需要继续修改学生信息(y/n):  ")
            if remark == 'y' or remark == 'Y':
                mark = True
            else:
                mark = False
                with open(filename, 'w') as f_write:
                    for line in student_new:
                        f_write.write(str(line) + '\n')
        elif studentId == 'q' or studentId == 'Q':
            mark = False
        else:
            print("学生ID号码不符合要求，请重新输入")
            continue
        
def sort():
    '''根据学生id,python,english等进行排序显示'''
    mark = True
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            student_old = f.readlines()
            student_new = []
        for list in student_old:
            d = dict(eval(list))
            student_new.append(d)
    else:
        return
    while mark:
        order = input("请选择排序方式(0：升序， 1：降序):  ")
        if order == '0':
            orderBool = False
        elif order == '1':
            orderBool = True
        else:
            print("您的输入有误，请重新输入.")
            sort()
        mode = input("请选择排序方式(1.按英语成绩 2.按python成绩 3.按总成绩 4.按学生id)")
        if mode == '1':
            student_sort = sorted(student_new, key=lambda x: x["english"], reverse=orderBool )
        elif mode == '2':
            student_sort = sorted(student_new, key=lambda x: x["python"], reverse=orderBool)
        elif mode == '3':
            student_sort = sorted(student_new, key=lambda x: x["english"] + x["python"], reverse=orderBool)
        elif mode == '4':
            student_sort = sorted(student_new, key=lambda x: x["id"], reverse=orderBool)
        else:
            print("您的输入有误，请重新输入.")
            sort()
        show_student(student_sort)   #display the result by sort
        re_mark = input("是否继续进行排序查询(y/n)?")
        if re_mark == 'y' or re_mark == 'Y':
            mark = True
        else:
            mark = False
            
def sumStudent():
    '''显示总的学生人数'''
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            student_old = f.readlines()
            if student_old is not "":
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
    """
    根据输入的数字，跳转到对应的功能，
    """
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
                back()
            elif option_int == 2:
                query()
                back()
            elif option_int == 3:
                delete()
                back()
            elif option_int == 4:
                modify()
                back()
            elif option_int == 5:
                sort()
                back()
            elif option_int == 6:
                sumStudent()
                back()
            elif option_int == 7:
                show()
                back()
def back():
    """返回主菜单，更人性化显示"""
    mark = input("是否返回主菜单(任意键返回主菜单，q/Q退出程序):   ")
    if mark == 'q' or mark == 'Q':
        exit()
        
if __name__ == "__main__":
    main()