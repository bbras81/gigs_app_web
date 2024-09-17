import sqlite3


def main():
    con = sqlite3.connect("gigs_app.db")

    cur = con.cursor()



    def db_execute(query:str): 
        db_answer = cur.execute(query)
        return db_answer
    
    db_execute("""CREATE TABLE IF NOT EXISTS clients(
               id_cliente INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
               nome_empresa TEXT NOT NULL, 
               nif INTEGER NOT NULL UNIQUE,
               morada TEXT NOT NULL,
               cp TEXT NOT NULL,
               localidade TEXT NOT NULL,
               email TEXT NOT NULL,
               telefone INTEGER,
               recibo TEXT NOT NULL
            )""")

if __name__ == "__main__":
    main()