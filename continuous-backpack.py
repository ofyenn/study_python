"""

Задача на программирование: непрерывный рюкзак

Первая строка содержит количество предметов 1≤n≤103 1 \le n \le 10^3 1≤n≤103
и вместимость рюкзака 0≤W≤2⋅106 0 \le W \le 2 \cdot 10^6 0≤W≤2⋅106. Каждая из
следующих n n n строк задаёт стоимость 0≤ci≤2⋅106 0 \le c_i \le 2\cdot 10^6
0≤ci​≤2⋅106 и объём 0<wi≤2⋅106 0 \lt w_i \le 2\cdot 10^6 0<wi​≤2⋅106 предмета 
(n n n, W W W, ci c_i ci​, wi w_i wi​ — целые числа). Выведите максимальную
стоимость частей предметов (от каждого предмета можно отделить любую часть,
стоимость и объём при этом пропорционально уменьшатся), помещающихся в данный
рюкзак, с точностью не менее трёх знаков после запятой.

"""

N_V = input().split()
N = int(N_V[0])
V = int(N_V[1])
massiv = []
for i in range(N):
    massiv.append([int(x) for x in input().split()])
    massiv[i].append(massiv[i][0] / massiv[i][1])
massiv = sorted(massiv, key=lambda x: x[2], reverse=True)
answer = []
for i in range(len(massiv)):
    if massiv[i][1] <= V:
        answer.append(massiv[i][0])
    else:
        answer.append(massiv[i][0] / massiv[i][1] * V)
    V -= massiv[i][1]
    if V <= 0:
        break
print(f"{sum(answer):.3f}")



