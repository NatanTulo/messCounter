# Analiza wiadomości

Ten program przetwarza pliki HTML oraz JSON zawierające dane wiadomości z Facebooka i Messengera. Działa w następujący sposób:
- Ładuje pliki HTML i JSON z bieżącego katalogu.
- Parsuje dane, wyodrębniając nadawców, treść wiadomości, liczbę słów, zdjęcia, filmy oraz daty wiadomości.
- Agreguje statystyki dotyczące liczby wiadomości, słów, zdjęć i filmów dla każdego nadawcy.
- Sortuje i filtruje nadawców według liczby wiadomości spełniających zadany próg.
- Wyświetla statystyki w postaci tabelki oraz generuje histogram liczby wiadomości.
- Mierzy i wyświetla czas przetwarzania plików.

## Źródła danych

- Pliki HTML oraz JSON można pozyskać ze strony:  
https://accountscenter.facebook.com/info_and_permissions/dyi

- Drugi typ JSONa, zawierający zaszyfrowane wiadomości, jest dostępny stąd:  
https://www.messenger.com/secure_storage/dyi

# Instrukcja użycia

1. Umieść pliki HTML/JSON w katalogu projektu.
2. Uruchom program `messCounter.py`.
3. Przejrzyj wygenerowane statystyki oraz histogram.

## Przykładowy output

Statystyki:
```
  Lp | Nadawca                  | Wiadomości |    Słowa | Zdjęcia | Wideo |  % udziału
--------------------------------------------------------------------------------------
  1  | Jan Kowalski             |         45 |      300 |      10 |     2 |   20.00%
  2  | Anna Nowak               |         32 |      250 |       8 |     1 |   16.67%
  3  | Piotr Wiśniewski         |         25 |      180 |       5 |     0 |   12.00%
```

Łączna liczba wiadomości: 102  
Łączna liczba słów: 730  
Pierwsza wiadomość: 2021-01-01 12:00:00  
Ostatnia wiadomość: 2021-12-31 18:30:00  
Czas między pierwszą a ostatnią wiadomością: 364 days, 6:30:00  

Przetworzono 3 plików w ciągu 0:00:12.345678
