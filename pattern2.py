# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1

for i in range(1,6):
    for j in range(6-i):
        print(6-i,end=" ")

    print(" ")

# 5 5 5 5 5
# 5 5 5 5
# 5 5 5
# 5 5
# 5

n = 1
for row in range(1,6):
    for col in range(6-row):
        print(5,end=" ")
    
    print(" ")
