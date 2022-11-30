import time
from datetime import datetime as dt

hosts_temp = "hosts"
# hosts_path = r"C:\Windows\System32\drivers\etc\hosts"                     when you want to run this script in background needs to run as in Administrative mode
redirect = "127.0.0.1"
website_list = ["www.pornhub.com","www.xnxx.com","www.pornhd3x.tv"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("working hours...")

        with open(hosts_temp,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        with open(hosts_temp,'r+') as file:
            content = file.readlines()
            file.seek(0)                                                        #make space after the writing the whole script again
            for line in content:
                if not any(website in line for website in website_list):        #comparing line array values and website array,if there is code in website on line,ignore and rewrite the other things 
                    file.write(line)
                file.truncate()                                                 #delete averything
        print("Fun hours...")
    time.sleep(5)

    #if you want to run this script everytime when you log in to your machine
    #then use task sheduler to to that
    #also need to save the script with " .pyw  "extention