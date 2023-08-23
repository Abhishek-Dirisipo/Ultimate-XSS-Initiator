fn="parameters2 copy.txt"

p_size=2 # parameter size
with open(fn, 'r') as fp:
    Lines1 = fp.readlines()
    param_len=len(Lines1)

for i in range(0,param_len,p_size):
    with open(fn, 'r') as fp:
        Lines1 = fp.readlines()
        m=i   # main
        c=0
        line2=""
        n=4
        for line in Lines1:
            if "?" not in line:
                line="?"+line+"="
            c+=1
            if c==1+m:
                line2=line.replace("?","*").replace("\n","")+"FUZZ"
            if c>1+m:
                line2=line2+(line.replace("\n","").replace("?","&"))+"FUZZ"
            if c==p_size+m: 
                break
        print(line2.replace("*","?"))
