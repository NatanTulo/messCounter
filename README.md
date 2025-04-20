# Analiza wiadomości

Program przetwarza pliki HTML oraz JSON zawierające dane wiadomości z Messengera. Działa w następujący sposób:
- Ładuje pliki HTML i JSON z katalogu `data`.
- Parsuje dane, wyodrębniając nadawców, treść wiadomości, liczbę słów, zdjęcia, filmy oraz daty wiadomości.
- Agreguje statystyki dotyczące liczby wiadomości, słów, zdjęć i filmów dla każdego nadawcy.
- Sortuje i filtruje nadawców według liczby wiadomości spełniających zadany próg.
- Wyświetla statystyki w postaci tabelki oraz generuje histogram liczby wiadomości.
- Mierzy i wyświetla czas przetwarzania plików.
- Przy uruchomieniu z parametrem `-s`, skrypt analizuje wpisy JSON, wyszukując w polu "uri" ścieżki do plików multimedialnych z katalogu `data\media` i przenosi je do folderów o nazwie odpowiadającej wartości z pola `senderName`.

## Źródła danych

- Pliki HTML oraz JSON można pozyskać ze strony:  
  https://accountscenter.facebook.com/info_and_permissions/dyi

- Pliki JSON z zaszyfrowanymi wiadomościami można uzyskać stąd:  
  https://www.facebook.com/secure_storage/dyi

# Instrukcja użycia

1. Umieść pliki HTML/JSON w katalogu `data`.
2. Umieść pliki multimedialne w katalogu `data\media` (powiązane z drugim źródłem - Bezpieczna pamięć).
3. Zainstaluj zależności poleceniem:  
   pip install -r requirements.txt
4. Uruchom program `messCounter.py`.
   - Aby przetworzyć jedynie dane wiadomości, uruchom:  
     python messCounter.py
   - Aby dodatkowo poukładać pliki multimedialne według nadawcy, uruchom:  
     python messCounter.py -s
5. Przejrzyj wygenerowane statystyki oraz histogram.

## Przykładowy output

Statystyki:
```
  Lp | Nadawca                  | Wiadomości | Zdjęcia | Wideo |    Słowa |  % udziału
--------------------------------------------------------------------------------------
  1  | Jan Kowalski             |         45 |      10 |     2 |      300 |   20.00%
  2  | Anna Nowak               |         32 |       8 |     1 |      250 |   16.67%
  3  | Piotr Wiśniewski         |         25 |       5 |     0 |      180 |   12.00%
```

Łączna liczba wiadomości: 102  
Łączna liczba słów: 730  
Pierwsza wiadomość: 2021-01-01 12:00:00  
Ostatnia wiadomość: 2021-12-31 18:30:00  
Czas między pierwszą a ostatnią wiadomością: 364 days, 6:30:00  

Przetworzono 3 plików w ciągu 0:00:12.345678
