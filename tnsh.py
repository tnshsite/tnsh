import time as t
import os as o

print("Hello!")

while True:
    cmd = input("neko.>>>")

    if cmd == "exit":
        break
    else:
        try:
            o.system(cmd)
        except:
            print("command not found")
