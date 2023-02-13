#259 Characters (We're getting there!)

num_string='123456789'
for i in range(0,18):
    if(i < 10):
        line=" "*(abs(9-i))+num_string[:i%10]
        line=line+line[:len(line)-1][::-1]
    else:
        line=" "*(abs(9-i))+num_string[:18-i]   
        line=line+line[:len(line)-1][::-1]
    print(line)