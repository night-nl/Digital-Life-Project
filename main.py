from model import LM  
LM.init()
#LM.send("你好啊")
while True:
    print()
    msg = input(">>> ")
    if msg == "exit":
        break
    LM.send(msg)
#print(model.LM.history)