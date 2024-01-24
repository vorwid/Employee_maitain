employees = []

def add_employee():
    employee = {}
    employee["imie"] = input("Podaj imię pracownika: ")
    employee["nazwisko"] = input("Podaj nazwisko pracownika: ")
    employee["stanowisko"] = input("Podaj stanowisko pracownika: ")
    employee["zarobki"] = float(input("Podaj zarobki pracownika: "))
    employees.append(employee)
    print("Pracownik dodany do bazy danych.")

def display_employees():
    if len(employees) == 0:
        print("Baza danych pracowników jest pusta.")
    else:
        print("Lista pracowników:")
        for employee in employees:
            print(f"Imię: {employee['imie']}")
            print(f"Nazwisko: {employee['nazwisko']}")
            print(f"Stanowisko: {employee['stanowisko']}")
            print(f"Zarobki: {employee['zarobki']}")
            print()

def search_employee():
    last_name = input("Podaj nazwisko pracownika do wyszukania: ")
    found = False
    for employee in employees:
        if employee["nazwisko"] == last_name:
            print("Znaleziono pracownika:")
            print(f"Imię: {employee['imie']}")
            print(f"Nazwisko: {employee['nazwisko']}")
            print(f"Stanowisko: {employee['stanowisko']}")
            print(f"Zarobki: {employee['zarobki']}")
            print()
            found = True
            break
    if not found:
        print("Nie znaleziono pracownika o podanym nazwisku.")

while True:
    print("Menu:")
    print("1. Dodaj pracownika")
    print("2. Wyświetl listę pracowników")
    print("3. Wyszukaj pracownika po nazwisku")
    print("4. Wyjście")

    choice = input("Wybierz opcję: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        display_employees()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        break
    else:
        print("Nieprawidłowy wybór. Spróbuj ponownie.")