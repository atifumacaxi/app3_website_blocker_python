import time
from datetime import datetime as dt

hosts_temp="hosts" #just for test
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com", "facebook.com", "youtube.com", "www.youtube.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print("Time to work!")
        with open(hosts_path, 'r+') as arch:
            content = arch.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    arch.write(redirect+" "+ website+"\n")

    else:
        with open(hosts_path, 'r+') as arch:
            content = arch.readlines()
            arch.seek(0) #The pointer will go to the zero position
            for line in content:
                if not any(website in line for website in website_list):
                    arch.write(line)
            arch.truncate() #Erases everything below the pointer
        print("Fun HOUR!!!")
    time.sleep(5)
