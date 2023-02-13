#172 Characters (Wow!)

num_string='123456789'
x = lambda a:a%10 if a<10 else 18-a
for i in range(0,18):
    line=" "*(abs(9-i))+num_string[:x(i)]
    line=line+line[:len(line)-1][::-1]
    print(line)