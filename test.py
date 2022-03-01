la = [1,1,2,3,3]
lb = [3,3,4,5,5]
lc = []
for i in la[:]:
    if i in lb:
        lc.append(i)
        lb.remove(i)

print(lc)
print(la+lb)