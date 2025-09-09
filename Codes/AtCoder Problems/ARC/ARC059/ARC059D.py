c=input()
if c[0]==c[1]:r=[1,2]
else:
    r=[-1]*2
    for s in range(len(c)-2):
        if c[s]==c[s+1] or c[s]==c[s+2] or c[s+1]==c[s+2]:
            r=[s+1,s+3]
            break
print(*r)