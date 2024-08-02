### Speedtest Web Application

Questo progetto è una semplice applicazione web che esegue un test di velocità della connessione Internet e visualizza i risultati in un'interfaccia utente accattivante. Utilizza un backend in Python con Flask per eseguire il test e un frontend in HTML, CSS e JavaScript per mostrare i risultati.
![brave_I6LTpkcyXC](https://github.com/user-attachments/assets/cfb9479f-66d7-4b4d-a76b-34ad328320d6)
**Funzionalità**

- Test di Velocità: Esegue test di velocità di download, upload e ping.
- Interfaccia Utente Dinamica: Visualizza i risultati del test e offre un'opzione per scaricarli in formato PDF.
- Tema Scuro e Chiaro: Permette di passare tra modalità chiara e scura.
- Aggiornamenti Automatici: I risultati vengono aggiornati automaticamente ogni 60 secondi.
- Animazioni e Stili: Include effetti visivi come animazioni LED e gocce d'acqua.
- Struttura del Progetto

**LICENSE**: 

> File di licenza del progetto. Specifica la licenza utilizzata.

**README.md**: 

> Questo file, con le istruzioni e la documentazione del progetto.

fetchSpeedtest.js: Script JavaScript che gestisce la logica per aggiornare i risultati del test di velocità e gestire le interazioni dell'utente.
**index.html**: 

> Pagina HTML principale con l'interfaccia utente per visualizzare i risultati del test e le animazioni.

**speedtest_server.py**:

>  Script Python che esegue il test di velocità e restituisce i risultati in formato JSON tramite un'API RESTful.

**_Come Usare_**
Configura l'Ambiente:

Assicurati di avere Python e Flask installati.
Installa le dipendenze necessarie con pip install flask speedtest-cli flask-cors.
Esegui il Server:

Avvia il server Python eseguendo python speedtest_server.py.
Il server sarà in ascolto su http://127.0.0.1:5000.
Accedi all'Applicazione:

### Apri index.html

- [ ] nel tuo browser per visualizzare l'interfaccia utente e i risultati del test di velocità.
- [ ] Scarica i Risultati:
- [ ] Clicca sul pulsante "Download PDF" per scaricare i risultati del test in formato PDF.

**Licenza**
Questo progetto è concesso in licenza sotto la Licenza MIT - vedi il file LICENSE per i dettagli.
