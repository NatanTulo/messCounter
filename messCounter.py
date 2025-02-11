import os
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Zastąpienie ręcznej listy plików dynamicznym wczytywaniem plików HTML z bieżącego katalogu
file = [f for f in os.listdir('.') if f.endswith('.html')]
names = {}
for f in file:
    page = open(f, "r", encoding="utf8")
    soup = BeautifulSoup(page, 'lxml')
    people = soup.find_all('div', class_='_2ph_ _a6-h _a6-i')
    for p in people:
        if p.text not in names:
            names[p.text] = 1
        else:
            names[p.text] += 1
sorted_names = dict(sorted(names.items(), key=lambda item: item[1], reverse=True))
# Filtruj wyniki, ignorując te o wartościach mniejszych niż 10
filtered_names = {k: v for k, v in sorted_names.items() if v >= 10}
i = 1
for n in filtered_names:
    print(str(i) + ". ", n + ': ' + str(filtered_names[n]))
    i += 1

# Dodaj histogram dla danych
plt.figure(figsize=(10, 6))
plt.bar(list(filtered_names.keys()), list(filtered_names.values()))
plt.ylabel('Liczba wiadomości')
plt.title('Histogram liczby wiadomości')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()