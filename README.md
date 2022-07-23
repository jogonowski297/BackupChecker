
# Backup Checker

Backup Checker to program służacy do sprawdzania kopii zapasowych np. Windows Server. Program przeznaczony jest dla firm zajmujacych się administracja oraz dla użytkowników chcacych mieć pełna kontrolę nad kopiami.


Aby uruchomić program:
- wprowadź odpowiednie dane w pliku main.py (pola oznaczone "XXX")
- wprowadź dane do pliku config.txt

Program używa bibliotek:
- smtplib (aby wysłać odpowiedni raport na podany adres e-mail)
- sqlite3 (aby utworzyć bazę danych z której może wnioskować czy dana kopia została wykonana)
- ssl (aby utworzyc nowy kontekst)