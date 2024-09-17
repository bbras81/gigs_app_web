import sqlite3


def db_execute(query:str, params:list): 
    con = sqlite3.connect("gigs_app.db")
    cur = con.cursor()
    db_answer = cur.execute(query, params)
    con.commit()
    con.close()
    return db_answer



def main():


    
    db_execute("""CREATE TABLE IF NOT EXISTS clients(
               id_cliente INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
               nome_empresa TEXT NOT NULL, 
               nif INTEGER NOT NULL UNIQUE,
               morada TEXT NOT NULL,
               cp TEXT NOT NULL,
               localidade TEXT NOT NULL,
               email TEXT NOT NULL,
               telefone INTEGER,
               recibo TEXT
            )""",[])

if __name__ == "__main__":
    main()