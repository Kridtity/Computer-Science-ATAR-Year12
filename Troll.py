import os
print("Do not enter anything.")

i = input("")
os.system(r'shutdown /s /d u:5:15 /f /t 10 /c "What did I say? Save your work in the 10 seconds left."')

i = input("").lower()
if "sorry" in i:
    os.system(r"shutdown /a")
else:
    print("Wrong answer.")
