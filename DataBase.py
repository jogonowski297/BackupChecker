import sqlite3

class DataBase:
    def __init__(self, nr_tabeli):
        self.nr_tabeli = nr_tabeli
        self.conn = sqlite3.connect('archiwum.db')
        self.cur = self.conn.cursor()
        self.cur.execute('''CREATE TABLE [%s] 
                        (id   INTEGER,
                        nazwa  CHAR(250),
                        rozmiar CHAR(10),
                        data_   CHAR(20),
                        kopia   CHAR(5))''' % self.nr_tabeli)

    def first_add(self,id, nazwa, rozmiar, data):
        data = (int(id), str(nazwa[0]), str(rozmiar), str(data), "TRUE")
        add = ("INSERT INTO [%s] (id, nazwa, rozmiar, data_, kopia) VALUES (?, ?, ?, ?, ?)" % self.nr_tabeli)
        return add, data

    def other_add(self,id, nazwa, rozmiar, data, bool):
        if bool:
            data = (int(id), str(nazwa[0]), str(rozmiar), str(data), "TRUE")
        else:
            data = (int(id), str(nazwa[0]), str(rozmiar), str(data), "FALSE")

        add = ("INSERT INTO [%s] (id, nazwa, rozmiar, data_, kopia) VALUES (?, ?, ?, ?, ?)" % self.nr_tabeli)
        return add, data

    def get_size(self, id, tabela):
        size = self.cur.execute('SELECT rozmiar FROM [%s] WHERE id=?' % tabela, (id,))
        return size.fetchall()[0][0]

    def get_name(self, id, tabela):
        size = self.cur.execute('SELECT nazwa FROM [%s] WHERE id=?' % tabela, (id,))
        return size.fetchall()[0][0]

    def get_date(self, id, tabela):
        size = self.cur.execute('SELECT data_ FROM [%s] WHERE id=?' % tabela, (id,))

    def add_to_db(self, add, data):
        self.cur.execute(add, data)
        self.conn.commit()

    def get_last_row(self):
        return self.cur.execute('SELECT * FROM [%s] ORDER BY id DESC LIMIT 1' % self.nr_tabeli)
