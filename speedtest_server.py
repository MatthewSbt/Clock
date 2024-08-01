from flask import Flask, jsonify
import speedtest
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/speedtest')
def speedtest_results():
    test = speedtest.Speedtest()
    test.get_best_server()  # Seleziona il miglior server
    download = test.download()
    upload = test.upload()
    test_results = test.results  # Ottieni i risultati del test
    
    # Usa i risultati per ottenere i valori di download, upload e ping
    results = {
        'download': test_results.download / 10**6,  # Converti in Mbps
        'upload': test_results.upload / 10**6,      # Converti in Mbps
        'ping': test_results.ping                   # Ping in ms
    }

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
