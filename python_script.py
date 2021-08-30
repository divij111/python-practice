import os
import datetime
time = datetime.datetime.now()
now = int(time.strftime("%H"))
if now>=0 and now<=11:
    print("Hello Good Morning!")
elif now>=12 and now<=15:
    print("Hello Good Afternoon!")
elif now>=16 and now<=19:
    print("Hello Good Evening!")
else:
    print("Hello Good Night!")
print(os.getcwd())