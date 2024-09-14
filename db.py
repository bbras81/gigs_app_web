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
               morada TEXT,
               nif INTEGER NOT NULL UNIQUE,
               email TEXT NOT NULL,
               recibo TEXT NOT NULL
            )""")

if __name__ == "__main__":
    main()