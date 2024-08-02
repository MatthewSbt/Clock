### Network Speedtest Web Application

**Descrizione**
Questa applicazione web permette di eseguire un test di velocità della rete (download, upload e ping) e visualizzare i risultati in tempo reale. Utilizza un server backend basato su Flask che esegue i test di velocità utilizzando la libreria speedtest-cli, e un frontend HTML/CSS/JavaScript che recupera e visualizza i risultati.
![brave_I6LTpkcyXC](https://github.com/user-attachments/assets/cfb9479f-66d7-4b4d-a76b-34ad328320d6)
**Funzionalità**
Test di Velocità della Rete: Misura la velocità di download e upload e il tempo di ping della connessione Internet.
Visualizzazione dei Risultati: Mostra i risultati del test in una pagina web con un'animazione di caricamento.
Aggiornamenti Automatici: I risultati vengono aggiornati automaticamente ogni 60 secondi.
Gestione degli Errori: Gestione dei possibili errori di rete e di fetch per garantire un'esperienza utente fluida.
Tecnologie Utilizzate
Backend: Python, Flask, speedtest-cli
Frontend: HTML, CSS, JavaScript
CORS: Flask-CORS per gestire le richieste cross-origin
Installazione
Prerequisiti
Python 3.x
Node.js (per servire i file statici se necessario)
Pip (gestore di pacchetti per Python)
Passaggi
Clona il Repository

bash
Copy code

> git clone https://github.com/<tuo-utente>/<tuo-repo>.git
> cd <tuo-repo>

Installa le Dipendenze Python

Crea un ambiente virtuale e installa le dipendenze:

bash
Copy code

> python -m venv venv
> source venv/bin/activate  # Su Windows usa: venv\Scripts\activate
> pip install -r requirements.txt
> requirements.txt:

Copy code

> Flask
> flask-cors
> speedtest-cli
> Avvia il Server Backend

bash
Copy code

> python speedtest_server.py

**Il server verrà avviato su** http://127.0.0.1:5000.

Servi i File Statici

Se hai bisogno di servire i file statici (HTML, CSS, JS), puoi utilizzare un server statico come http-server (Node.js) o configurare Flask per servire i file statici.

Se usi http-server, installa e avvia il server:

bash
Copy code

> npm install -g http-server
> http-server ./ --port 8080

Accedi alla tua applicazione su http://localhost:8080.

**Uso**
Accesso alla Pagina: Apri il browser e vai su http://localhost:8080 (o su un'altra porta se hai configurato diversamente).
Visualizzazione dei Risultati: I risultati del test di velocità saranno visualizzati automaticamente dopo il caricamento della pagina e verranno aggiornati ogni 60 secondi.
Contribuire
Se desideri contribuire al progetto, segui questi passaggi:

Fork del Repository
Crea un Branch: git checkout -b nome-del-tuo-branch
Fai le tue Modifiche
Commit e Push: git commit -am 'Aggiungi nuova funzionalità' e git push origin nome-del-tuo-branch
Crea una Pull Request
Assicurati di seguire le linee guida per il contributo e di testare le tue modifiche.

Licenza
Distribuito sotto la Licenza MIT. Vedi LICENSE per ulteriori dettagli.

Contatti
Per domande o suggerimenti, contattami su  aggiornamentiutilita@protonmail.com
