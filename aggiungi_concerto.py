# Aggiungere concerto
def crea_concerto(utente_loggato, concerti_registrati):
    
    # Richiede password segreta
    password = input("Inserisci la password segreta per aggiungere concerti: ")
    if password != "GHIBLI":
        print("Password segreta errata. Non puoi creare concerti.")
        return
    
    # Controllo se sono già 3 concerti registrati
    if len(concerti_registrati) >= 3:
        print("Hai già 3 concerti registrati. Non puoi aggiungerne altri.")
        return
    
    # Richiedo il nome del concerto
    nome_concerto = input("Inserisci il nome del concerto: ")
    
    # Inizialmente la sala è di 10 posti
    posti_disponibili = 10
    
    # Aggiungo alla lista dei concerti
    concerti_registrati.append([nome_concerto, posti_disponibili])
    print(f"Concerto '{nome_concerto}' creato con successo da {utente_loggato}!")
            
            
    
    