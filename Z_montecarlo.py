import random
import math


def get_radius():
    while True:
        try:
            r = float(input("Podaj promień r > 0 : "))
            if r > 0:
                break
        except:
            print("To musi być liczba!")
            continue
    return r


def get_number_of_shots():
    while True:
        try:
            number_of_shots = int(input("Podaj liczbę strzałów > 0 : "))
            if number_of_shots > 0:
                break
        except:
            print("To musi być liczba całkowita!")
            continue
    return number_of_shots


def count_shots(radius, number_of_shots):
    shot_in_circle = 0
    for _ in range(number_of_shots):
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)
        distance = math.sqrt(x**2 + y**2)
        if distance <= radius:
            shot_in_circle += 1
    return shot_in_circle


if __name__ == "__main__":
    radius = get_radius()
    number_of_shots = get_number_of_shots()

    estimated_pi = 4 * (count_shots(radius, number_of_shots) / number_of_shots)

    deviation = abs(estimated_pi-math.pi)/estimated_pi*100

    print(f"Na podstawie {number_of_shots} wartości losowych, dla figur w przedziale r równym: {radius}, wyznaczono przybliżenie liczby pi, które wynosi: {estimated_pi}\nRóżnica pomiedzy wartością liczby pi wyznaczoną metodą Monte Carlo, a wartością rzeczywistą to: {deviation:.2f}%")
