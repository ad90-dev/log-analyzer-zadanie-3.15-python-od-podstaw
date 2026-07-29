# stałą zawierająca ścieżkę do pliku txt
TXT_FILE = r'server_logs.txt'

# pusta lista na zapytania zakończone sukcesem
successful = []

# pusta lista na zapytania zakończone błędem
errors = []

# otwarcie pliku i wyświetlenie go w konsoli
with open(TXT_FILE, 'r', newline='', encoding='utf-8') as file:
    content = file.readlines()
    for line in content:
        print(line)

    # Ile było zapytań?
    total_lines = len(content)
    print(total_lines)

    # Ile zapytań zakończyło się sukcesem, a ile błędem?
    for line in content:
        inquiry = int(line.strip('\n').split(' ')[-1])
        if inquiry < 400:
            successful.append(inquiry)
        else:
            errors.append(inquiry)

    # zapisanie udanych zapytań do zmiennej
    total_successful = len(successful)
    print(total_successful)

    # zapisanie nieudanych zapytań do zmiennej
    total_errors = len(errors)
    print(total_errors)

# zapis wyników do pliku analysis_results.txt

with open('analysis_results.txt', 'w+', newline='\n', encoding='utf-8') as file:
    file.write('Wyniki analizy:\n--------------\n')
    file.write('')
    file.write(f'Liczba zapytań: {total_lines}\n')
    file.write(f'Liczba udanych zapytań {total_successful}\n')
    file.write(f'Liczba nieudanych zapytań {total_errors}\n')
