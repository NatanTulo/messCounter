import os
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

cut_off = 10  # Minimalna liczba wiadomości, aby zostać uwzględnionym w wynikach

# Funkcja pomocnicza do parsowania daty
def parse_date(date_str):
    # Wykryj, czy tekst zawiera frazy określające porę dnia
    is_afternoon = "po południu" in date_str
    is_morning = "rano" in date_str
    # Usuń te frazy z tekstu
    for marker in ["rano", "po południu"]:
        date_str = date_str.replace(marker, "")
    date_str = date_str.strip()
    parts = date_str.split()
    month_map = {
        "sty": 1, "lut": 2, "mar": 3, "kwi": 4,
        "maj": 5, "cze": 6, "lip": 7, "sie": 8,
        "wrz": 9, "paź": 10, "lis": 11, "gru": 12
    }
    mon = month_map.get(parts[0].lower(), 0)
    day = int(parts[1].replace(",", ""))
    year = int(parts[2])
    time_parts = parts[3].split(":")
    hour = int(time_parts[0])
    minute = int(time_parts[1])
    second = int(time_parts[2])
    if is_afternoon and hour < 12:
        hour += 12
    return datetime(year, mon, day, hour, minute, second)

# Dynamiczne pobieranie plików HTML z bieżącego katalogu
file = [f for f in os.listdir('.') if f.endswith('.html')]
names = {}
total_words = 0
words_per_sender = {}  # Nowy słownik dla liczby słów per nadawca
first_date = None
last_date = None

for f in file:
    with open(f, "r", encoding="utf8") as page:
        soup = BeautifulSoup(page, 'lxml')
    # Iteruj po kontenerach wiadomości
    messages = soup.find_all('div', class_='_a6-g')
    for m in messages:
        # Pobranie nadawcy
        sender_tag = m.find('div', class_='_2ph_ _a6-h _a6-i')
        if not sender_tag:
            continue
        sender = sender_tag.text.strip()
        names[sender] = names.get(sender, 0) + 1

        # Pobranie treści wiadomości i liczba słów
        content_tag = m.find('div', class_='_2ph_ _a6-p')
        if content_tag:
            content = content_tag.text.strip()
            word_count = len(content.split())
            total_words += word_count
            words_per_sender[sender] = words_per_sender.get(sender, 0) + word_count

        # Pobranie daty wiadomości
        date_tag = m.find('div', class_='_a72d')
        if date_tag:
            try:
                msg_date = parse_date(date_tag.text.strip())
                if first_date is None or msg_date < first_date:
                    first_date = msg_date
                if last_date is None or msg_date > last_date:
                    last_date = msg_date
            except Exception as e:
                pass  # ignoruj nieparsowalne daty

# Sortowanie i filtrowanie nadawców
sorted_names = dict(sorted(names.items(), key=lambda item: item[1], reverse=True))
# Filtruj wyniki, ignorując te o wartościach mniejszych niż cut_off
filtered_names = {k: v for k, v in sorted_names.items() if v >= cut_off}

# Po filtrowaniu danych usuń poprzednie wydruki i dodaj: 
print("\nStatystyki:")
sorted_senders = sorted(filtered_names.keys(), key=lambda s: words_per_sender.get(s, 0), reverse=True)
i = 1
for sender in sorted_senders:
    msgs = filtered_names[sender]
    sender_words = words_per_sender.get(sender, 0)
    percentage = (sender_words / total_words * 100) if total_words > 0 else 0
    print(f"{i}. {sender}: {msgs} wiadomości, słowa: {sender_words}, czyli {percentage:.2f} % udziału")
    i += 1

# Wyświetl licznik słów oraz informacje o datach wiadomości
print("\nŁączna liczba słów:", total_words)
if first_date and last_date:
    print("Pierwsza wiadomość:", first_date.strftime('%Y-%m-%d %H:%M:%S'))
    print("Ostatnia wiadomość:", last_date.strftime('%Y-%m-%d %H:%M:%S'))
    diff = last_date - first_date
    print("Czas między pierwszą a ostatnią wiadomością:", diff)

# Dodaj histogram dla danych
plt.figure(figsize=(10, 6))
plt.bar(list(filtered_names.keys()), list(filtered_names.values()))
plt.ylabel('Liczba wiadomości')
plt.title('Histogram liczby wiadomości')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()