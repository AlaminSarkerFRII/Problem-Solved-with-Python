import math
x1,y1 = list(map(float,input().split()))
x2,y2 = list(map(float,input().split()))
formula = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))

print(f'{formula:.4f}')