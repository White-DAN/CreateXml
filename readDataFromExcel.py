import xlrd
from xlrd import xldate_as_tuple
import datetime

import numpy as np
import matplotlib.pyplot as plt
import xml.dom.minidom as Dom

'''
xlrd中单元格的数据类型
数字一律按浮点型输出，日期输出成一串小数，布尔型输出0或1，所以我们必须在程序中做判断处理转换
成我们想要的数据类型
0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
'''


class ExcelData:
    # 初始化方法
    def __init__(self, data_path, sheetname):
        # 定义一个属性接收文件路径
        self.data_path = data_path
        # 定义一个属性接收工作表名称
        self.sheetname = sheetname
        # 使用xlrd模块打开excel表读取数据
        self.data = xlrd.open_workbook(self.data_path)
        # 根据工作表的名称获取工作表中的内容（方式①）
        self.table = self.data.sheet_by_name(self.sheetname)
        # 根据工作表的索引获取工作表的内容（方式②）
        # self.table = self.data.sheet_by_name(0)
        # 获取第一行所有内容,如果括号中1就是第二行，这点跟列表索引类似
        # self.keys = self.table.row_values(0)
        # 获取工作表的有效行数
        self.rowNum = self.table.nrows + 1
        # 获取工作表的有效列数
        self.colNum = self.table.ncols

    # 定义一个读取excel表的方法
    def readExcel(self):
        # 定义一个空列表
        datas = []
        for i in range(1, self.rowNum):
            # 定义一个空字典
            sheet_data = {}
            for j in range(self.colNum):
                # 获取单元格数据类型
                c_type = self.table.cell(i - 1, j).ctype
                # 获取单元格数据
                c_cell = self.table.cell_value(i - 1, j)
                if c_type == 2 and c_cell % 1 == 0:  # 如果是整形
                    c_cell = int(c_cell)
                elif c_type == 3:
                    # 转成datetime对象
                    date = datetime.datetime(*xldate_as_tuple(c_cell, 0))
                    c_cell = date.strftime('%Y/%d/%m %H:%M:%S')
                elif c_type == 4:
                    c_cell = True if c_cell == 1 else False
                sheet_data[j] = c_cell
                # 循环每一个有效的单元格，将字段与值对应存储到字典中
                # 字典的key就是excel表中每列第一行的字段
                # sheet_data[self.keys[j]] = self.table.row_values(i)[j]
            # 再将字典追加到列表中
            datas.append(sheet_data)
            # 返回从excel中获取到的数据：以列表存字典的形式返回
        return datas

    def plotChart(self):
        # 基础温度
        baseTemperature = 22
        datas = self.readExcel()
        X = []
        Y = []
        #
        for i in range(len(datas)):
            sheet_data = datas[i]
            for j in sheet_data.keys():
                if j == 0:
                    X.append(round(sheet_data[j], 1))
                else:
                    Y.append(round(sheet_data[j], 3) + baseTemperature)
        newX = []
        newY = []
        newX.append(X[0])
        newY.append(Y[0])

        # 1表示斜率大于等于0  -1表示小于0 转向的时候改变
        flag = 1
        for i in range(len(X) - 1):
            speed = abs((Y[i + 1] - Y[i]) / (X[i + 1] - X[i]))
            # 从正斜率到负斜率
            if flag == 1 and Y[i + 1] < Y[i] and speed < 0.02:
                newX.append(X[i])
                newY.append(Y[i])
                flag = -1
            elif flag == -1 and Y[i + 1] > Y[i] and speed < 0.02:
                newX.append(X[i])
                newY.append(Y[i])
                flag = 1
            elif speed > 0.02:
                newX.append(X[i])
                newY.append(Y[i])
            else:
                continue
        newX.append(X[len(X) - 1])
        newY.append(Y[len(X) - 1])
        # for i in range(len(newX)):
        #     print(newX[i], end=' ')
        # print()
        # for i in range(len(newY)):
        #     print(newY[i], end=' ')
        # print()
        # for i in range(len(Y)):
        #     print(Y[i], end=' ')
        # plt.subplot(2, 2, 1)
        # print(X)
        # print(Y)
        print(newX)
        print(newY)
        plt.plot(X, Y, marker='o')
        plt.plot(newX, newY, marker='*')
        plt.show()

        # 新的数组节点存入原数组
        X = newX
        Y = newY

        # 根据数据创建xml文件
        doc = Dom.Document()
        # 根节点
        root = doc.createElement("DocumentElement")
        doc.appendChild(root)
        # 第一个打开开关的节点
        child1 = doc.createElement("Table_Script")
        Addr_node = doc.createElement("Addr")
        Addr_value = doc.createTextNode("0")
        Addr_node.appendChild(Addr_value)
        child1.appendChild(Addr_node)
        #
        ModuleName_node = doc.createElement("ModuleName")
        ModuleName_value = doc.createTextNode("TC1")
        ModuleName_node.appendChild(ModuleName_value)
        child1.appendChild(ModuleName_node)
        #
        ParamName_node = doc.createElement("ParamName")
        ParamName_value = doc.createTextNode("TCSW")
        ParamName_node.appendChild(ParamName_value)
        child1.appendChild(ParamName_node)
        #
        ParamText_node = doc.createElement("ParamText")
        ParamText_value = doc.createTextNode("开关")
        ParamText_node.appendChild(ParamText_value)
        child1.appendChild(ParamText_node)
        #
        Cmd_node = doc.createElement("Cmd")
        Cmd_value = doc.createTextNode("=")
        Cmd_node.appendChild(Cmd_value)
        child1.appendChild(Cmd_node)
        #
        ValueText_node = doc.createElement("ValueText")
        ValueText_value = doc.createTextNode("1")
        ValueText_node.appendChild(ValueText_value)
        child1.appendChild(ValueText_node)
        #
        Var_node = doc.createElement("Var")
        Var_value = doc.createTextNode("1")
        Var_node.appendChild(Var_value)
        child1.appendChild(Var_node)
        #
        Count_node = doc.createElement("Count")
        Count_value = doc.createTextNode("0")
        Count_node.appendChild(Count_value)
        child1.appendChild(Count_node)
        #
        Reg_node = doc.createElement("Reg")
        Reg_value = doc.createTextNode("-1")
        Reg_node.appendChild(Reg_value)
        child1.appendChild(Reg_node)

        root.appendChild(child1)
        # 设置到达基础温度的限速
        child00 = doc.createElement("Table_Script")
        Addr_node00 = doc.createElement("Addr")
        Addr_value00 = doc.createTextNode("0")
        Addr_node00.appendChild(Addr_value00)
        child00.appendChild(Addr_node00)
        #
        ModuleName_node00 = doc.createElement("ModuleName")
        ModuleName_value00 = doc.createTextNode("TC1")
        ModuleName_node00.appendChild(ModuleName_value00)
        child00.appendChild(ModuleName_node00)
        #
        ParamName_node00 = doc.createElement("ParamName")
        ParamName_value00 = doc.createTextNode("TCRAMPSPEED")
        ParamName_node00.appendChild(ParamName_value00)
        child00.appendChild(ParamName_node00)
        #
        ParamText_node00 = doc.createElement("ParamText")
        ParamText_value00 = doc.createTextNode("温度限速")
        ParamText_node00.appendChild(ParamText_value00)
        child00.appendChild(ParamText_node00)
        #
        Cmd_node00 = doc.createElement("Cmd")
        Cmd_value00 = doc.createTextNode("=")
        Cmd_node00.appendChild(Cmd_value00)
        child00.appendChild(Cmd_node00)
        #
        ValueText_node00 = doc.createElement("ValueText")
        ValueText_value00 = doc.createTextNode("0.001")
        ValueText_node00.appendChild(ValueText_value00)
        child00.appendChild(ValueText_node00)
        #
        Var_node00 = doc.createElement("Var")
        Var_value00 = doc.createTextNode("1")
        Var_node00.appendChild(Var_value00)
        child00.appendChild(Var_node00)
        #
        Count_node00 = doc.createElement("Count")
        Count_value00 = doc.createTextNode("0")
        Count_node00.appendChild(Count_value00)
        child00.appendChild(Count_node00)
        #
        Reg_node00 = doc.createElement("Reg")
        Reg_value00 = doc.createTextNode("-1")
        Reg_node00.appendChild(Reg_value00)
        child00.appendChild(Reg_node00)

        root.appendChild(child00)
        # 设置基础温度的第一个节点
        child0 = doc.createElement("Table_Script")
        Addr_node0 = doc.createElement("Addr")
        Addr_value0 = doc.createTextNode("0")
        Addr_node0.appendChild(Addr_value0)
        child0.appendChild(Addr_node0)
        #
        ModuleName_node0 = doc.createElement("ModuleName")
        ModuleName_value0 = doc.createTextNode("TC1")
        ModuleName_node0.appendChild(ModuleName_value0)
        child0.appendChild(ModuleName_node0)
        #
        ParamName_node0 = doc.createElement("ParamName")
        ParamName_value0 = doc.createTextNode("TCADJUSTTEMP")
        ParamName_node0.appendChild(ParamName_value0)
        child0.appendChild(ParamName_node0)
        #
        ParamText_node0 = doc.createElement("ParamText")
        ParamText_value0 = doc.createTextNode("调节温度")
        ParamText_node0.appendChild(ParamText_value0)
        child0.appendChild(ParamText_node0)
        #
        Cmd_node0 = doc.createElement("Cmd")
        Cmd_value0 = doc.createTextNode("=")
        Cmd_node0.appendChild(Cmd_value0)
        child0.appendChild(Cmd_node0)
        #
        ValueText_node0 = doc.createElement("ValueText")
        ValueText_value0 = doc.createTextNode(str(baseTemperature))
        ValueText_node0.appendChild(ValueText_value0)
        child0.appendChild(ValueText_node0)
        #
        Var_node0 = doc.createElement("Var")
        Var_value0 = doc.createTextNode("1")
        Var_node0.appendChild(Var_value0)
        child0.appendChild(Var_node0)
        #
        Count_node0 = doc.createElement("Count")
        Count_value0 = doc.createTextNode("0")
        Count_node0.appendChild(Count_value0)
        child0.appendChild(Count_node0)
        #
        Reg_node0 = doc.createElement("Reg")
        Reg_value0 = doc.createTextNode("-1")
        Reg_node0.appendChild(Reg_value0)
        child0.appendChild(Reg_node0)

        root.appendChild(child0)
        # 判断实际温度是否到达基础温度
        # 设置基础温度的实际温度
        child01 = doc.createElement("Table_Script")
        Addr_node01 = doc.createElement("Addr")
        Addr_value01 = doc.createTextNode("0")
        Addr_node01.appendChild(Addr_value01)
        child01.appendChild(Addr_node01)
        #
        ModuleName_node01 = doc.createElement("ModuleName")
        ModuleName_value01 = doc.createTextNode("TC1")
        ModuleName_node01.appendChild(ModuleName_value01)
        child01.appendChild(ModuleName_node01)
        #
        ParamName_node01 = doc.createElement("ParamName")
        ParamName_value01 = doc.createTextNode("TCACTUALTEMP")
        ParamName_node01.appendChild(ParamName_value01)
        child01.appendChild(ParamName_node01)
        #
        ParamText_node01 = doc.createElement("ParamText")
        ParamText_value01 = doc.createTextNode("实际温度")
        ParamText_node01.appendChild(ParamText_value01)
        child01.appendChild(ParamText_node01)
        #
        Cmd_node01 = doc.createElement("Cmd")
        Cmd_value01 = doc.createTextNode("?")
        Cmd_node01.appendChild(Cmd_value01)
        child01.appendChild(Cmd_node01)
        #
        ValueText_node01 = doc.createElement("ValueText")
        ValueText_value01 = doc.createTextNode(str(baseTemperature))
        ValueText_node01.appendChild(ValueText_value01)
        child01.appendChild(ValueText_node01)
        #
        Var_node01 = doc.createElement("Var")
        Var_value01 = doc.createTextNode("0.001")
        Var_node01.appendChild(Var_value01)
        child01.appendChild(Var_node01)
        #
        Count_node01 = doc.createElement("Count")
        Count_value01 = doc.createTextNode("0")
        Count_node01.appendChild(Count_value01)
        child01.appendChild(Count_node01)
        #
        Reg_node01 = doc.createElement("Reg")
        Reg_value01 = doc.createTextNode("-1")
        Reg_node01.appendChild(Reg_value01)
        child01.appendChild(Reg_node01)

        root.appendChild(child01)
        index = 0
        length = len(X)
        maxSpeed = 0
        maxTime = 0
        minTime = 100000000
        count = 0
        sum1 = 0
        # while True:
        #     x = X[index]
        #     y = Y[index]
        #     # 需要设定的温度
        #     curTem = baseTemperature + y
        #     if index == length - 1:
        #         break
        #     # 平行的线用延时处理
        #     while index < length-1 & Y[index] == Y[index + 1]:
        #         index += 1
        for index in range(length - 1):
            curTem = Y[index]
            nextTem = Y[index + 1]
            K = (nextTem - curTem) / (X[index + 1] - X[index])
            speed = round(abs(K), 4)
            print(speed, end='  ')
            sum1 += 1
            if Y[index] == Y[index + 1] or speed == 0:
                count += 1
                # 延时处理
                # 第一个开始节点
                child5 = doc.createElement("Table_Script")
                Addr_node = doc.createElement("Addr")
                Addr_value = doc.createTextNode("0")
                Addr_node.appendChild(Addr_value)
                child5.appendChild(Addr_node)
                #
                ModuleName_node = doc.createElement("ModuleName")
                ModuleName_value = doc.createTextNode("TC1")
                ModuleName_node.appendChild(ModuleName_value)
                child5.appendChild(ModuleName_node)
                #
                ParamName_node = doc.createElement("ParamName")
                ParamName_value = doc.createTextNode("SCRIPTDELAY")
                ParamName_node.appendChild(ParamName_value)
                child5.appendChild(ParamName_node)
                #
                ParamText_node = doc.createElement("ParamText")
                ParamText_value = doc.createTextNode("延时")
                ParamText_node.appendChild(ParamText_value)
                child5.appendChild(ParamText_node)
                # TRAN_Cmd
                Cmd_node = doc.createElement("Cmd")
                Cmd_value = doc.createTextNode("=")
                Cmd_node.appendChild(Cmd_value)
                child5.appendChild(Cmd_node)
                # 延时时间
                time = round(X[index + 1] - X[index], 3)
                ValueText_node = doc.createElement("ValueText")
                ValueText_value = doc.createTextNode(str(time))
                ValueText_node.appendChild(ValueText_value)
                child5.appendChild(ValueText_node)
                #
                Var_node = doc.createElement("Var")
                Var_value = doc.createTextNode("1")
                Var_node.appendChild(Var_value)
                child5.appendChild(Var_node)
                #
                Count_node = doc.createElement("Count")
                Count_value = doc.createTextNode("0")
                Count_node.appendChild(Count_value)
                child5.appendChild(Count_node)
                #
                Reg_node = doc.createElement("Reg")
                Reg_value = doc.createTextNode("-1")
                Reg_node.appendChild(Reg_value)
                child5.appendChild(Reg_node)

                root.appendChild(child5)
            else:
                if speed < 0.005:
                    count += 1
                maxSpeed = max(maxSpeed, speed)
                child2 = doc.createElement("Table_Script")
                child3 = doc.createElement("Table_Script")
                # 子节点温度限速
                Addr_node2 = doc.createElement("Addr")
                Addr_value2 = doc.createTextNode("0")
                Addr_node2.appendChild(Addr_value2)
                child2.appendChild(Addr_node2)
                #
                ModuleName_node2 = doc.createElement("ModuleName")
                ModuleName_value2 = doc.createTextNode("TC1")
                ModuleName_node2.appendChild(ModuleName_value2)
                child2.appendChild(ModuleName_node2)
                #
                ParamName_node2 = doc.createElement("ParamName")
                ParamName_value2 = doc.createTextNode("TCRAMPSPEED")
                ParamName_node2.appendChild(ParamName_value2)
                child2.appendChild(ParamName_node2)
                # BUSS_SEQ_NO
                ParamText_node2 = doc.createElement("ParamText")
                ParamText_value2 = doc.createTextNode("温度限速")
                ParamText_node2.appendChild(ParamText_value2)
                child2.appendChild(ParamText_node2)
                #
                Cmd_node2 = doc.createElement("Cmd")
                Cmd_value2 = doc.createTextNode("=")
                Cmd_node2.appendChild(Cmd_value2)
                child2.appendChild(Cmd_node2)
                #
                ValueText_node2 = doc.createElement("ValueText")
                ValueText_value2 = doc.createTextNode(str(speed))
                ValueText_node2.appendChild(ValueText_value2)
                child2.appendChild(ValueText_node2)
                #
                Var_node2 = doc.createElement("Var")
                Var_value2 = doc.createTextNode("1")
                Var_node2.appendChild(Var_value2)
                child2.appendChild(Var_node2)
                #
                Count_node2 = doc.createElement("Count")
                Count_value2 = doc.createTextNode("0")
                Count_node2.appendChild(Count_value2)
                child2.appendChild(Count_node2)
                #
                Reg_node2 = doc.createElement("Reg")
                Reg_value2 = doc.createTextNode("-1")
                Reg_node2.appendChild(Reg_value2)
                child2.appendChild(Reg_node2)

                # 子节点3-需要设定的温度
                Addr_node3 = doc.createElement("Addr")
                Addr_value3 = doc.createTextNode("0")
                Addr_node3.appendChild(Addr_value3)
                child3.appendChild(Addr_node3)
                #
                ModuleName_node3 = doc.createElement("ModuleName")
                ModuleName_value3 = doc.createTextNode("TC1")
                ModuleName_node3.appendChild(ModuleName_value3)
                child3.appendChild(ModuleName_node3)
                #
                ParamName_node3 = doc.createElement("ParamName")
                ParamName_value3 = doc.createTextNode("TCADJUSTTEMP")
                ParamName_node3.appendChild(ParamName_value3)
                child3.appendChild(ParamName_node3)
                #
                ParamText_node3 = doc.createElement("ParamText")
                ParamText_value3 = doc.createTextNode("调节温度")
                ParamText_node3.appendChild(ParamText_value3)
                child3.appendChild(ParamText_node3)
                #
                Cmd_node3 = doc.createElement("Cmd")
                Cmd_value3 = doc.createTextNode("=")
                Cmd_node3.appendChild(Cmd_value3)
                child3.appendChild(Cmd_node3)
                #
                # 如果速度斜率大于0.05则减少以该速度变化的时间，降低温控器无法迅速反应导致超过设定温度
                if K < -0.05:
                    nextTem = round(curTem - speed * (X[index + 1] - X[index] - 14), 3)
                elif K > 0.05:
                    nextTem = round(curTem + speed * (X[index + 1] - X[index] - 13), 3)
                ValueText_node3 = doc.createElement("ValueText")
                ValueText_value3 = doc.createTextNode(str(nextTem))
                ValueText_node3.appendChild(ValueText_value3)
                child3.appendChild(ValueText_node3)
                #
                Var_node3 = doc.createElement("Var")
                Var_value3 = doc.createTextNode("1")
                Var_node3.appendChild(Var_value3)
                child3.appendChild(Var_node3)
                #
                Count_node3 = doc.createElement("Count")
                Count_value3 = doc.createTextNode("0")
                Count_node3.appendChild(Count_value3)
                child3.appendChild(Count_node3)
                #
                Reg_node3 = doc.createElement("Reg")
                Reg_value3 = doc.createTextNode("-1")
                Reg_node3.appendChild(Reg_value3)
                child3.appendChild(Reg_node3)

                # 判断是否到达指定温度的节点
                child4 = doc.createElement("Table_Script")
                Addr_node4 = doc.createElement("Addr")
                Addr_value4 = doc.createTextNode("0")
                Addr_node4.appendChild(Addr_value4)
                child4.appendChild(Addr_node4)
                #
                ModuleName_node4 = doc.createElement("ModuleName")
                ModuleName_value4 = doc.createTextNode("TC1")
                ModuleName_node4.appendChild(ModuleName_value4)
                child4.appendChild(ModuleName_node4)
                #
                ParamName_node4 = doc.createElement("ParamName")
                ParamName_value4 = doc.createTextNode("TCACTUALTEMP")
                ParamName_node4.appendChild(ParamName_value4)
                child4.appendChild(ParamName_node4)
                #
                ParamText_node4 = doc.createElement("ParamText")
                ParamText_value4 = doc.createTextNode("实际温度")
                ParamText_node4.appendChild(ParamText_value4)
                child4.appendChild(ParamText_node4)
                #
                Cmd_node4 = doc.createElement("Cmd")
                Cmd_value4 = doc.createTextNode("?")
                Cmd_node4.appendChild(Cmd_value4)
                child4.appendChild(Cmd_node4)
                #
                ValueText_node4 = doc.createElement("ValueText")
                ValueText_value4 = doc.createTextNode(str(nextTem))
                ValueText_node4.appendChild(ValueText_value4)
                child4.appendChild(ValueText_node4)
                #
                Var_node4 = doc.createElement("Var")
                Var_value4 = doc.createTextNode("0.001")
                Var_node4.appendChild(Var_value4)
                child4.appendChild(Var_node4)
                #
                Count_node4 = doc.createElement("Count")
                Count_value4 = doc.createTextNode("0")
                Count_node4.appendChild(Count_value4)
                child4.appendChild(Count_node4)
                #
                Reg_node4 = doc.createElement("Reg")
                Reg_value4 = doc.createTextNode("-1")
                Reg_node4.appendChild(Reg_value4)
                child4.appendChild(Reg_node4)

                root.appendChild(child2)
                root.appendChild(child3)
                root.appendChild(child4)
            maxTime = round(max(maxTime, X[index + 1] - X[index]), 3)
            minTime = round(min(minTime, X[index + 1] - X[index]), 3)

        # 最后一个关闭开关的节点
        child9 = doc.createElement("Table_Script")
        Addr_node9 = doc.createElement("Addr")
        Addr_value9 = doc.createTextNode("0")
        Addr_node9.appendChild(Addr_value9)
        child9.appendChild(Addr_node9)
        #
        ModuleName_node9 = doc.createElement("ModuleName")
        ModuleName_value9 = doc.createTextNode("TC1")
        ModuleName_node9.appendChild(ModuleName_value9)
        child9.appendChild(ModuleName_node9)
        #
        ParamName_node9 = doc.createElement("ParamName")
        ParamName_value9 = doc.createTextNode("TCSW")
        ParamName_node9.appendChild(ParamName_value9)
        child9.appendChild(ParamName_node9)
        #
        ParamText_node9 = doc.createElement("ParamText")
        ParamText_value9 = doc.createTextNode("开关")
        ParamText_node9.appendChild(ParamText_value9)
        child9.appendChild(ParamText_node9)
        #
        Cmd_node9 = doc.createElement("Cmd")
        Cmd_value9 = doc.createTextNode("=")
        Cmd_node9.appendChild(Cmd_value9)
        child9.appendChild(Cmd_node9)
        #
        ValueText_node9 = doc.createElement("ValueText")
        ValueText_value9 = doc.createTextNode("0")
        ValueText_node9.appendChild(ValueText_value9)
        child9.appendChild(ValueText_node9)
        #
        Var_node9 = doc.createElement("Var")
        Var_value9 = doc.createTextNode("1")
        Var_node9.appendChild(Var_value9)
        child9.appendChild(Var_node9)
        #
        Count_node9 = doc.createElement("Count")
        Count_value9 = doc.createTextNode("0")
        Count_node9.appendChild(Count_value9)
        child9.appendChild(Count_node9)
        #
        Reg_node9 = doc.createElement("Reg")
        Reg_value9 = doc.createTextNode("-1")
        Reg_node9.appendChild(Reg_value9)
        child9.appendChild(Reg_node9)

        root.appendChild(child9)

        f = open("data.xml", "wb")
        f.write(doc.toprettyxml(indent="\t", newl="\n", encoding="utf-8"))
        f.close()
        return maxSpeed, maxTime, minTime, count, sum1

    # 读取温度测量数据txt
    def readDatas(self):
        # f = open(r"data/test09-01测量数据.txt")
        # f = open(r"data/test10-01测量数据(0.1精度) - 数据1txt")
        # f = open(r"data/test10-01测量数据(0.1精度) - 数据4.txt")
        # f = open(r"newData/装置搭建好脚本test09-01温度数据(1度).txt")
        f = open(r"newData/装置搭建好脚本test10-01温度数据(0.1度).txt")
        line = f.readline()
        data_list = []
        while line:
            num = list(map(str, line.split()))
            data_list.append(num)
            line = f.readline()
        f.close()
        data_array = np.array(data_list)
        # print(data_array)
        # print(data_array.shape)
        return data_array

    # 提取测量数据以及画图
    def plotData(self):

        # 基础温度
        baseTemperature = 25
        datas = self.readExcel()
        X0 = []
        Y0 = []
        #
        for i in range(len(datas)):
            sheet_data = datas[i]
            for j in sheet_data.keys():
                if j == 0:
                    X0.append(round(sheet_data[j], 3))
                else:
                    Y0.append(round(sheet_data[j], 3) + baseTemperature)
        # plt.subplot(2, 2, 1)
        plt.figure(1)
        plt.plot(X0, Y0)

        data_array = self.readDatas()
        tu = data_array.shape
        rows = tu[0]
        # cols = tu[1]
        X = []
        Y1 = []
        Y2 = []
        Y3 = []
        row1 = data_array[0]
        timeStr = row1[2]
        h, m, s = timeStr.split(':')
        baseTime = int(h) * 3600 + int(m) * 60 + int(s[0:2])
        X.append(0)
        Y1.append(float(row1[3]))
        Y2.append(float(row1[4]))
        Y3.append(float(row1[5]))
        for i in range(1, rows):
            row = data_array[i]
            # print(len(row))
            h1, m1, s1 = row[2].split(':')
            curTime = int(h1) * 3600 + int(m1) * 60 + int(s1[0:2])
            X.append(curTime - baseTime)
            Y1.append(float(row[3]))
            Y2.append(float(row[4]))
            Y3.append(float(row[5]))
        # plt.plot(X, Y1)
        # plt.subplot(2, 2, 2)
        # 测量曲线拐点处与理论曲线平移到一起
        for i in range(0, len(X)):
            X[i] = X[i] + 100

        plt.figure(1)
        plt.plot(X, Y2)
        # plt.plot(X, Y3)
        plt.show()

    # 根据测量曲线重写原始曲线
    def youHuaData(self):
        # 基础温度
        baseTemperature = 22
        datas = self.readExcel()
        X = []
        Y = []
        #
        for i in range(len(datas)):
            sheet_data = datas[i]
            for j in sheet_data.keys():
                if j == 0:
                    X.append(round(sheet_data[j], 3))
                else:
                    Y.append(round(sheet_data[j], 3) + baseTemperature)
        newX = []
        newY = []
        newX.append(X[0])
        newY.append(Y[0])

        # 1表示斜率大于等于0  -1表示小于0 转向的时候改变
        flag = 1
        for i in range(len(X) - 1):
            speed = abs((Y[i + 1] - Y[i]) / (X[i + 1] - X[i]))
            # 从正斜率到负斜率
            if flag == 1 and Y[i + 1] < Y[i] and speed < 0.02:
                newX.append(X[i])
                newY.append(Y[i])
                flag = -1
            elif flag == -1 and Y[i + 1] > Y[i] and speed < 0.02:
                newX.append(X[i])
                newY.append(Y[i])
                flag = 1
            elif speed > 0.02:
                newX.append(X[i])
                newY.append(Y[i])
            else:
                continue
        newX.append(X[len(X) - 1])
        newY.append(Y[len(X) - 1])
        # plt.plot(X, Y)
        # plt.plot(newX, newY)
        # plt.show()
        print(newX)
        print(newY)
        # 解决时延问题
        youX = []
        youY = []
        youX.append(newX[0])
        youY.append(newY[0])
        youX.append(newX[1] - 5)
        youY.append(newY[1])
        k = (newY[2] - newY[1]) / (newX[2] - newX[1])
        print(k)
        # 斜率过大两点之间时间间隔的三分之一
        diff = (newX[2] - newX[1]) / 3
        print(diff)
        youX.append(youX[1] + 2 * diff)
        youY.append(youY[1] + 2 * diff * k)
        # youX数组索引
        i = 3
        youX.append(youX[i - 1] + diff)
        youY.append(youY[i - 1])
        index = 3
        i = 4
        while index < 14:
            # 后面一条斜率较高的曲线
            if index == 10:
                index += 1
            else:
                k = (newY[index + 1] - newY[index]) / (newX[index + 1] - newX[index])
                nextX = youX[i - 1] + (newX[index + 1] - newX[index])
                nextY = youY[i - 1] + k * (newX[index + 1] - newX[index])
                youX.append(nextX)
                youY.append(nextY)
                index += 1
                i += 1
        plt.plot(X, Y)
        plt.plot(newX, newY, marker='*')
        plt.plot(youX, youY)
        plt.show()


if __name__ == "__main__":
    # data_path = "原始曲线\\Te_1.xlsx"  # 1度原始数据
    data_path = "原始曲线/Te-0.1.xlsx"  # 0.1度原始数据
    sheetname = "Sheet1"
    get_data = ExcelData(data_path, sheetname)
    datas = get_data.readExcel()
    # # nums = get_data.toArrays()
    # print(datas)
    # # print(type(datas))
    # # print(len(datas))
    # # print(nums)
    # maxData = get_data.plotChart()
    # print(maxData[0])
    # print(maxData[1])
    # print(maxData[2])
    # print(maxData[3])
    # print(maxData[4])
    get_data.plotData()
    # get_data.youHuaData()
