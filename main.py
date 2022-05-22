from Path import Path
from Errors import Errors
from datetime import datetime

if __name__ == "__main__":
    config = open('config.txt', 'r')
    main = [s.replace("\n", "").split(",,,") for s in config.readlines()]


    Path = Path()
    Error = Errors()

    for m in main[1:]:
        size, date = Path.get_date_and_size(m[0])
        today = datetime.now().day
        default_size = m[1]
        default_date = m[2]

        if((float(default_size[1:-1])-float(size))<=3 and (int(today)-int(date[8:10]))<=int(default_date[1:-1])):
            print(f"Kopia z katalogu: {m[0]} zostala zrobiona.")
        else:
            Error.add_error()
    print(f"Ilosc bledow: {Error.print_errors()}")
