from aggiungi_concerto import get_concerti

prenotazioni_effettuate = []

def prenota_concerto(utente_loggato):
    # Recupero la lista dei concerti
    concerti_registrati = get_concerti()

    if len(concerti_registrati) == 0:
        print("Non ci sono concerti disponibili.")
        return

    # Mostro tutti i concerti disponibili
    print("Concerti disponibili:")
    for i in range(len(concerti_registrati)):
        concerto = concerti_registrati[i]
        # concerto = [nome_concerto, data, luogo, posti]
        nome = concerto[0]
        data = concerto[1]
        luogo = concerto[2]
        posti_disponibili = concerto[3]
        print(f"{i+1}. {nome} - {data} - {luogo} (Posti disponibili: {posti_disponibili})")

    # L'utente sceglie il concerto
    scelta_concerto = int(input("Scegli il numero del concerto: ")) - 1

    # Verifica che la scelta sia valida
    if scelta_concerto < 0 or scelta_concerto >= len(concerti_registrati):
        print("Scelta non valida!")
        return

    # Prelevo il concerto scelto
    concerto_scelto = concerti_registrati[scelta_concerto]
    posti_disponibili = concerto_scelto[3]  # Indice 3 = posti

    # Richiedo quanti posti prenotare
    posti_prenotati = int(input("Quanti posti vuoi prenotare? (max 3) "))
    if posti_prenotati > 3:
        print("Puoi prenotare al massimo 3 posti.")
        return

    if posti_prenotati <= 0:
        print("Numero di posti non valido.")
        return

    # Controllo se ci sono posti disponibili
    if posti_prenotati > posti_disponibili:
        print("Posti insufficienti per questo concerto!")
        return

    # Aggiorno i posti
    concerto_scelto[3] = posti_disponibili - posti_prenotati

    # Registro la prenotazione: [nome_utente_loggato, nome_concerto, posti]
    prenotazioni_effettuate.append([utente_loggato, concerto_scelto[0], posti_prenotati])
    print(f"Prenotazione effettuata per {posti_prenotati} posto/i al concerto '{concerto_scelto[0]}'!")

def get_prenotazioni():
    return prenotazioni_effettuate

def visualizza_prenotazioni():
    if len(prenotazioni_effettuate) == 0:
        print("Nessuna prenotazione effettuata.")
        return

    print("Prenotazioni Effettuate")
    for pren in prenotazioni_effettuate:
        utente = pren[0]
        concerto = pren[1]
        posti = pren[2]
        print(f"Utente: {utente} | Concerto: {concerto} | Posti: {posti}")
