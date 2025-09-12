weight=input()
num=float(weight[:-2])
unit=weight[-2:]
if unit=="kg":
    pound=round(num*2.2046,3)
    print(f"对应的英制重量为{pound}磅")
elif unit=="pd":
    kg = round(num*0.4535,3)
    print(f"对应的公制重量为{kg}公斤")
else:
    print("输入格式错误")
  
