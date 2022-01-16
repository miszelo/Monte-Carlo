import random
import math

while True:
    try:
        r = float(input("Podaj promień r > 0 : "))
        if r > 0:
            break
    except:
        print("To musi być liczba!")
        continue
while True:
    try:
        number_of_shots = int(input("Podaj liczbę strzałów > 0 : "))
        if number_of_shots > 0:
            break
    except:
        print("To musi być liczba całkowita!")
        continue

circle = 0
square = 0

for _ in range(number_of_shots):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    distance = math.sqrt(x**2 + y**2)
    if distance <= r:
        circle += 1  # dodaje 1 do trafienia w tarcze koła, jezeli odległość trafienia od środka tarczy będzie mniejsza/rowna niż promien
    square += 1  # dodaje 1 do trafienia w tarcze kwadratu zawsze, ponieważ zawsze trafia się w tarcze kwadratu

pi = 4 * (circle / square) # rownie dobrze można napisac 4 * (circle/number_of_shots)
error = abs(pi-math.pi)/pi*100
print(f"""Na podstawie {number_of_shots} wartości losowych, dla figur w przedziale r równym: {r}, wyznaczono przybliżenie liczby pi, które wynosi: {pi}
Różnica pomiedzy wartością liczby pi wyznaczoną metodą Monte Carlo, a wartością rzeczywistą to: {error:.2f}%""")