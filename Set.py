# l=[1,2,3,4]
# setw=set(l)
# print(setw)
s=set()
s.add(1)
s.add(2)
# s1=s.union({1,2,3})
s1=s.intersection({1,2,3})
print(s,s1)
print(s.isdisjoint(s1))
print(len(s))
print(min(s))
s.remove(1)