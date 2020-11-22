# n = 2
# #print(n)
# while n < 100:
#     print(n)
#     n = n + 2
#     continue
#--------
# for i in range(1,50):
#     print(i*2)
a=0
i=0
for i in range (0,100):
    if a%10 == 0 or '3' in str(i):
        a += 1
    else:
        print(a)
        a += 1
    i += 1
    
# for i in range (1,100):
#     if i %10 and '3' not in str(i):
#         print(i)