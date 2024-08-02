document.addEventListener("DOMContentLoaded", function() {
    const downloadSpeedElem = document.getElementById('download-speed');
    const uploadSpeedElem = document.getElementById('upload-speed');
    const pingTimeElem = document.getElementById('ping-time');
    const spinnerElem = document.getElementById('spinner'); // Elemento spinner per indicare il caricamento

    // Funzione per aggiornare i risultati del test di velocità
    function updateSpeedtestResults() {
        // Mostra lo spinner di caricamento
        spinnerElem.style.display = 'block';
        downloadSpeedElem.textContent = 'Loading...';
        uploadSpeedElem.textContent = 'Loading...';
        pingTimeElem.textContent = 'Loading...';

        fetch('http://127.0.0.1:5000/speedtest')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // Nascondi lo spinner e aggiorna i risultati
                spinnerElem.style.display = 'none';
                downloadSpeedElem.textContent = `${data.download.toFixed(2)} Mbps`;
                uploadSpeedElem.textContent = `${data.upload.toFixed(2)} Mbps`;
                pingTimeElem.textContent = `${data.ping.toFixed(2)} ms`;
            })
            .catch(error => {
                // Nascondi lo spinner e mostra un messaggio di errore
                spinnerElem.style.display = 'none';
                downloadSpeedElem.textContent = 'Error';
                uploadSpeedElem.textContent = 'Error';
                pingTimeElem.textContent = 'Error';
                console.error('Error fetching speedtest results:', error);
            });
    }

    // Aggiorna i risultati al caricamento della pagina
    updateSpeedtestResults();

    // Aggiorna i risultati ogni 60 secondi
    setInterval(updateSpeedtestResults, 60000);
});