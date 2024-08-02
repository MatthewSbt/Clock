from flask import Flask, jsonify
import speedtest
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/speedtest')
def speedtest_results():
    """
    Endpoint per eseguire un test di velocità e restituire i risultati in formato JSON.
    """
    try:
        # Crea un'istanza dell'oggetto Speedtest
        test = speedtest.Speedtest()
        
        # Seleziona il miglior server
        test.get_best_server()

        # Esegue il test di velocità
        download = test.download()
        upload = test.upload()
        ping_time = test.results.ping

        # Crea un dizionario con i risultati
        results = {
            'download': round(download / 1_000_000, 2),  # Converti in Mbps e arrotonda a 2 decimali
            'upload': round(upload / 1_000_000, 2),      # Converti in Mbps e arrotonda a 2 decimali
            'ping': round(ping_time, 2)                   # Arrotonda il ping a 2 decimali
        }

        # Restituisce i risultati in formato JSON
        return jsonify(results)

    except speedtest.SpeedtestException as e:
        # Gestione delle eccezioni specifiche di speedtest-cli
        return jsonify({'error': 'Errore durante il test di velocità', 'message': str(e)}), 500
    except Exception as e:
        # Gestione delle eccezioni generali
        return jsonify({'error': 'Errore interno del server', 'message': str(e)}), 500

if __name__ == '__main__':
    # Esegui l'app in modalità debug solo in fase di sviluppo
    # Usa 'host="0.0.0.0"' per consentire accesso esterno se necessario
    app.run(debug=True, host='0.0.0.0', port=5000)
