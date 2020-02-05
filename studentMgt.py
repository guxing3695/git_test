'''
@Author: your name
@Date: 2020-01-27 14:54:46
@LastEditTime : 2020-02-06 00:00:59
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /vscode_scripts/test.py
'''
import os
import sys
import re


menu():
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
        #                   8. 退出系统
        #############################################################################################
        说明：通过数字选择菜单
        """
          )

save():
    
    
insert():
    """
    新增学生信息
    """
    studentlist = []
    mark = True
    while mark:
        id = raw_input("请输入学生id(如1001)： ")
        name = raw_input("请输入学名姓名: ")
        english_score = raw_input("请输入学生英语成绩: ")
        python_score = raw_input("请输入学生python成绩: ")
        id = id.strip()
        name = name.strip()
        english_score = english_score.strip()
        python_score = python_score.strip()
        if not id or not name or not english_score or not python_score:
            print("学生相关信息不能为空!")
            continue
        if not id.isalnum() or not name.isalpha() or english_score.isdigit() or python_score.isdigit():
            print("学生信息要符合规范")
            continue
        student={"id": id,"name": name, "python": python_score, "english": english_score}
        studentlist.append(studnet)
        inputMark = raw_input("是否继续输入(Y/N):")
        if inputMark =="y" or inputMark ==“Y”:
            mark = True
        else:
            mark = False
    save(studentlist)
    print("学生信息录入完毕!") 
        


