def prenota_concerto(utente_loggato, concerti_registrati, prenotazioni_effettuate):
    
    # Controllo concerti nella lista
    if len(concerti_registrati) == 0:
        print("Non ci sono concerti disponibili.")
        return
    # Stampa concerti se disponibili
    print("Concerti disponibili:")
    for i in range(len(concerti_registrati)):
        concerto = concerti_registrati[i]
        print(f"{i+1}. {concerto[0]} (Posti disponibili: {concerto[1]})")

    # Scelta posti
    indice = int(input("Scegli il numero del concerto: ")) - 1
    posti = int(input("Quanti posti vuoi prenotare? "))

    if concerti_registrati[indice][1] < posti:
        print("Posti insufficienti!")
        return

    concerti_registrati[indice][1] -= posti
    prenotazioni_effettuate.append([utente_loggato, concerti_registrati[indice][0], posti])
    print(f"Prenotazione effettuata per {posti} posto/i al concerto '{concerti_registrati[indice][0]}'!")
