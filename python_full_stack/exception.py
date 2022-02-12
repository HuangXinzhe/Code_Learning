try:
    file = open("aaaa", 'r')
#     i = 1
except FileNotFoundError as e:  # 指定要捕获的异常
    print("发生异常了：文件没有发现，请检查")
    print(e)  # 打印异常内容
except ReferenceError as e:
    print("异常2")
except Exception:  
    print("发生异常了")
else:
    print("没有发生异常")
finally:
    print("这个无论如何都会被打印，也就是说这个代码无论如何都会被执行")