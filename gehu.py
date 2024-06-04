s="School Of Computing"
print(s[0],end='')
sp1=len(s.split())-1
sp2=0
for x in range(1,len(s)):
    if (s[x]==" "and sp2!=sp1):
        print(".",end='')
        print(s[x+1],end='')
        sp2=sp2+1
    # if(sp2==sp1):
#         break
# for y in range (x+2,len(s)):
#     print(s[y],end='')