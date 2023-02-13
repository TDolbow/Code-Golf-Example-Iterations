#129 Characters (This is crazy!)

n='123456789';x=lambda a:a%10 if a<10 else 18-a;i=0;exec('l=" "*(abs(9-i))+n[:x(i)];l=l+l[:len(l)-1][::-1];print(l);i=i+1;'*18)
