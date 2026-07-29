import sys
# stałą zawierająca ścieżkę do pliku txt
TXT_FILE = r'server_logs.txt'

# pusta lista na zapytania zakończone sukcesem
successful = []

# pusta lista na zapytania zakończone błędem
errors = []

# otwarcie pliku i wyświetlenie go w konsoli
try:
    with open(TXT_FILE, 'r', newline='', encoding='utf-8') as file:
        content = file.readlines()
        for line in content:
            print(line)

        # Ile było zapytań?
        total_lines = len(content)
        print(total_lines)

        # Ile zapytań zakończyło się sukcesem, a ile błędem?
        # - otrzymanie od razu kodu statusu, a pominięcie pozostałych kolumn
        for line in content:
            status_code = int(line.strip('\n').split()[-1])
            if status_code > 400:
                errors.append(status_code)
            elif 200 <= status_code < 300:
                successful.append(status_code)

        # zapisanie udanych zapytań do zmiennej
        total_successful = len(successful)
        print(total_successful)

        # zapisanie nieudanych zapytań do zmiennej
        total_errors = len(errors)
        print(total_errors)
except FileNotFoundError:
    print("Nie znaleziono pliku.")
    sys.exit()

# zapis wyników do pliku analysis_results.txt

try:
    with open('analysis_results.txt', 'w+', newline='\n', encoding='utf-8') as file:
        file.write('Wyniki analizy:\n--------------\n')
        file.write('')
        file.write(f'Liczba zapytań: {total_lines}\n')
        file.write(f'Liczba udanych zapytań {total_successful}\n')
        file.write(f'Liczba nieudanych zapytań {total_errors}\n')
except NameError:
    print("Brak danych.")
    sys.exit()
