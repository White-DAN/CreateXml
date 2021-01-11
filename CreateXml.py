from xml.dom.minidom import Document
import xml.dom.minidom

import xml.dom.minidom as Dom
from xml.dom import minidom

from Type import Type


def writeXml():
    doc = Dom.Document()
    # 根节点
    root = doc.createElement("DocumentElement")
    doc.appendChild(root)
    # 子节点
    child1 = doc.createElement("Table_Script")
    child2 = doc.createElement("Table_Script")
    child3 = doc.createElement("Table_Script")
    child4 = doc.createElement("Table_Script")

    # 子节点1
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

    # BUSS_SEQ_NO
    ParamText_node = doc.createElement("ParamText")
    ParamText_value = doc.createTextNode("开关")
    ParamText_node.appendChild(ParamText_value)
    child1.appendChild(ParamText_node)

    # TRAN_Cmd
    Cmd_node = doc.createElement("Cmd")
    Cmd_value = doc.createTextNode("=")
    Cmd_node.appendChild(Cmd_value)
    child1.appendChild(Cmd_node)

    # TRAN_ValueText
    ValueText_node = doc.createElement("ValueText")
    ValueText_value = doc.createTextNode("1")
    ValueText_node.appendChild(ValueText_value)
    child1.appendChild(ValueText_node)

    # TRAN_VarSTAMP
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

    # 子节点2
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

    # TRAN_Cmd
    Cmd_node2 = doc.createElement("Cmd")
    Cmd_value2 = doc.createTextNode("=")
    Cmd_node2.appendChild(Cmd_value2)
    child2.appendChild(Cmd_node2)

    # TRAN_ValueText
    ValueText_node2 = doc.createElement("ValueText")
    ValueText_value2 = doc.createTextNode("0.01")
    ValueText_node2.appendChild(ValueText_value2)
    child2.appendChild(ValueText_node2)

    # TRAN_VarSTAMP
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

    # 子节点3
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

    # BUSS_SEQ_NO
    ParamText_node3 = doc.createElement("ParamText")
    ParamText_value3 = doc.createTextNode("调节温度")
    ParamText_node3.appendChild(ParamText_value3)
    child3.appendChild(ParamText_node3)

    # TRAN_Cmd
    Cmd_node3 = doc.createElement("Cmd")
    Cmd_value3 = doc.createTextNode("=")
    Cmd_node3.appendChild(Cmd_value3)
    child3.appendChild(Cmd_node3)

    # TRAN_ValueText
    ValueText_node3 = doc.createElement("ValueText")
    ValueText_value3 = doc.createTextNode("25")
    ValueText_node3.appendChild(ValueText_value3)
    child3.appendChild(ValueText_node3)

    # TRAN_VarSTAMP
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

    # 子节点4
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

    # BUSS_SEQ_NO
    ParamText_node4 = doc.createElement("ParamText")
    ParamText_value4 = doc.createTextNode("实际温度")
    ParamText_node4.appendChild(ParamText_value4)
    child4.appendChild(ParamText_node4)

    # TRAN_Cmd
    Cmd_node4 = doc.createElement("Cmd")
    Cmd_value4 = doc.createTextNode("?")
    Cmd_node4.appendChild(Cmd_value4)
    child4.appendChild(Cmd_node4)

    # TRAN_ValueText
    ValueText_node4 = doc.createElement("ValueText")
    ValueText_value4 = doc.createTextNode("25")
    ValueText_node4.appendChild(ValueText_value4)
    child4.appendChild(ValueText_node4)

    # TRAN_VarSTAMP
    Var_node4 = doc.createElement("Var")
    Var_value4 = doc.createTextNode("0.02")
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

    root.appendChild(child1)
    root.appendChild(child2)
    root.appendChild(child3)
    root.appendChild(child4)

    # print(doc.toxml("utf-8"))
    f = open("DocumentElement.xml", "wb")
    f.write(doc.toprettyxml(indent="\t", newl="\n", encoding="utf-8"))
    f.close()


def startNode():

    return


if __name__ == "__main__":
    writeXml()
