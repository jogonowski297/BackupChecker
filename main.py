import ssl
from datetime import datetime
import smtplib
from Errors import Errors
from Path import Path
from DataBase import DataBase

if __name__ == "__main__":
    port = 999
    smtp_server = "XXX"
    nadawca = "XXX"
    odbiorca = "XXX"
    haslo = "XXX"
    wiadomosc = ""
    katalogi = ""
    send = True

    ssl_pol = ssl.create_default_context()
    config = open('config.txt', 'r')
    main = [s.replace("\n", "").split(",,,") for s in config.readlines()]
    id_counter = 1
    table_number = 1
    Path = Path(main[1])
    Error = Errors()

    while True:
        try:
            DataBase = DataBase(table_number)
            break
        except:
            table_number += 1
            continue

    with smtplib.SMTP_SSL(smtp_server,port,context=ssl_pol) as serwer:
        serwer.login(nadawca,haslo)
        for m in main[3:]:
            size, date = Path.get_date_and_size(m[0])

            if table_number == 1:
                add, data = DataBase.first_add(id_counter, m, size, date)
                id_counter += 1
                send = False
            else:
                if float(DataBase.get_size(id_counter, table_number-1)) - float(size) < 2 and int(str(date)[8:10]) == int(str(datetime.now())[8:10]):
                    add, data = DataBase.other_add(id_counter, m, size, date, True)
                    katalogi += f'OK    | Kopia z katalogu: {m[0]}\n'
                else:
                    add, data = DataBase.other_add(id_counter, m, size, date, False)
                    katalogi += f'BLAD  | Kopia z katalogu: {m[0]}\n'
                    Error.add_error()
                id_counter += 1

            DataBase.add_to_db(add, data)

        if send:
            wiadomosc += f'Subject: Ilosc niepowodzen: {Error.get_errors()}\n\n' + katalogi
            serwer.sendmail(nadawca, odbiorca, wiadomosc)
            DataBase.conn.close()