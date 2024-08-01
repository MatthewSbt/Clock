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
    ping_time = test.results.ping  # Usa il ping dal risultato del test

    results = {
        'download': download / 10**6,  # Converti in Mbps
        'upload': upload / 10**6,      # Converti in Mbps
        'ping': ping_time              # Ping in ms
    }

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
