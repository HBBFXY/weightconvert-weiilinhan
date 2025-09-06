weight=input("请输入重量：")
num=float(weight[:-2])
uint=weight[-2:]
if unit==＇kg＇:
    pound=num*2.2046
    print(f"对应的英制重量为{pound}磅")
elif unit==＇pd＇:
    kg =num*0.4535
    print(f"对应的公制重量为{kg}公斤")
else:
    print("输入格式错误")
  
