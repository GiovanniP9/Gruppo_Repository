from Registrazione_utente import registra_utente, login_utente
from aggiungi_concerto import crea_concerto
from prenota import prenota_concerto, visualizza_prenotazioni

def menu():
      # Controllo per utente loggato
      utente_loggato = None
      # Scelta menu
      while True:
            print("\n Gestione concerti")
            print("1. Registrazione utente")
            print("2. Login utente")
            print("3. Registrazione concerto (richiede login)")
            print("4. Prenotazione concerto (richiede login)")
            print("5. Visualizza prenotazioni (richiede login)")
            print("6. Esci")

            scelta = input("Scegli un'opzione: ")

            match scelta:
                  case "1":
                        registra_utente()

                  case "2":
                        utente_loggato = login_utente()

                  case "3":
                        if utente_loggato is not None:
                              crea_concerto()
                        else:
                              print("Devi prima effettuare il login.")

                  case "4":
                        if utente_loggato is not None:
                              prenota_concerto(utente_loggato)
                        else:
                              print("Devi prima effettuare il login.")

                  case "5":
                        if utente_loggato is not None:
                              visualizza_prenotazioni()
                        else:
                              print("Devi prima effettuare il login.")

                  case "6":
                        print("Arrivederci!")
                        break

                  case _:
                        print("Scelta non valida!")
                        
menu()