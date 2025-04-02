# Lista per memorizzare gli utenti
utenti_registrati = []

def registra_utente():
    nome = input("Inserisci il tuo nome utente: ")

    # Controllo se l'utente esiste già
    for utente in utenti_registrati:
        if utente[0] == nome:
            print("Errore: Questo nome utente è già registrato. Scegli un altro nome.")
            return

    password = input("Inserisci la tua password: ")

    # Salvo l'utente in lista
    utenti_registrati.append([nome, password])
    print("Registrazione completata con successo!")

def login_utente(): # Verifica se l'utente è registrato e se la password è corretta
    nome = input("Inserisci il tuo nome utente: ")
    password = input("Inserisci la tua password: ")

    for utente in utenti_registrati: # ciclo tutti gli utenti
        if utente[0] == nome and utente[1] == password:
            print("Login eseguito con successo!")
            return nome  

    print("Nome utente o password non validi.")
    return None

