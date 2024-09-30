def nome_funzione(parametro1, parametro2):
    # corpo della funzione
    valore_di_ritorno = 1
    return valore_di_ritorno


# Crea un programma che gestisce un registro di studenti. Ogni studente avrà un
# nome e un punteggio. Implementa le seguenti funzionalità:

# Aggiungere un nuovo studente al registro.
# Restituire il punteggio di un dato studente.
# Calcolare la media dei punteggi degli studenti.
# Restituire un dizionario con i nomi degli studenti che hanno un punteggio
# superiore alla media.

# Specifiche
# Utilizza un dizionario per memorizzare i nomi degli studenti come chiavi e i
# loro punteggi come valori.
# Implementa una funzione per ciascuna delle funzionalità sopra menzionate.


# Dizionario per memorizzare gli studenti e i loro punteggi
registro_studenti = {}


def aggiungi_studente(nome, punteggio):
    """Aggiunge un nuovo studente al registro."""
    registro_studenti[nome] = punteggio


def get_punteggio(nome):
    """Restituisce il punteggio di un dato studente."""
    return registro_studenti.get(nome, "Studente non trovato")


def calcola_media():
    """Calcola la media dei punteggi degli studenti."""
    if not registro_studenti:
        return 0
    return sum(registro_studenti.values()) / len(registro_studenti)


def studenti_sopra_media():
    """Restituisce un dizionario con i nomi degli studenti sopra la media."""
    media = calcola_media()
    return {
        nome: punteggio
        for nome, punteggio in registro_studenti.items()
        if punteggio > media
    }


# Esempio di utilizzo
aggiungi_studente("Mario", 85)
aggiungi_studente("Luisa", 90)
aggiungi_studente("Giovanni", 78)

print(get_punteggio("Luisa"))  # Dovrebbe stampare 90
print(calcola_media())  # Dovrebbe stampare la media dei punteggi
print(studenti_sopra_media())  # Dovrebbe stampare i nomi degli studenti sopra la media
