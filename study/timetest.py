import time
mytimes=time.time()
print(mytimes)
print("自从1970年到现在过去了",int(mytimes),"秒")
seconds= int(mytimes)%60   # 秒
hours=int(mytimes)//3600  # 过去小时
mins=(int(mytimes)-int(mytimes)//3600*3600)
mins=(mins-seconds)//60
print("自从1970年到现在过去了",
      hours,"小时",
      mins,"分",
        seconds,"秒")