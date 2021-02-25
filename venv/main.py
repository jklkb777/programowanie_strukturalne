#zad2
user_choice = 0

def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnożenie(x, y):
    return x * y

def dzielenie(x, y):
    return x / y

while user_choice != 5:
    if user_choice == 1:
        dodawanie()
    elif user_choice == 2:
        odejmowanie()
    elif user_choice == 3:
        mnożenie()
    elif user_choice == 4:
        dzielenie()
    elif user_choice == 5:
        break


print()
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
print("5. Koniec")

user_choice = int(input("Wybierz liczbę: "))
print()