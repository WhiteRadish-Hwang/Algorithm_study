n = int(input())
k = []
for i in range(n):
    k.append(int(input()))
def eureka_theory(eureka_sum):
    T1 = 0
    T2 = 0
    T3 = 0
    for i in range(1,45):
        t1 = (i*(i+1))/2
        for j in range(1,45):
            t2 = (j*(j+1))/2
            for m in range(1,45):
                t3 = (m*(m+1))/2
                if eureka_sum == t1 + t2 + t3:
                    return 1
    return 0

for idx in range(n):
    print(eureka_theory(k[idx]))