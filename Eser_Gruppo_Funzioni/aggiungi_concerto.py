concerti_registrati = []

def crea_concerto():
    
    # Richiesta password
    password = input("Inserisci la password segreta per aggiungere concerti: ")
    if password != "GHIBLI":
        print("Password segreta errata. Non puoi creare concerti.")
        return

    # Dati del concerto
    nome_concerto = input("Inserisci il nome del concerto: ")
    data = input("Inserisci la data del concerto: ")
    luogo = input("Inserisci il luogo del concerto: ")
    posti = 10

    concerto = [nome_concerto, data, luogo, posti]
    concerti_registrati.append(concerto)
    print("Registrazione concerto avvenuta con successo!")

def get_concerti():
    # Restituisce la lista dei concerti registrati
    return concerti_registrati
