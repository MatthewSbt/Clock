function updateSpeedtestResults() {
    fetch('http://127.0.0.1:5000/speedtest')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('results').innerHTML = `
                <div>Download Speed: ${data.download.toFixed(2)} Mbps</div>
                <div>Upload Speed: ${data.upload.toFixed(2)} Mbps</div>
                <div>Ping Time: ${data.ping.toFixed(2)} ms</div>
            `;
            document.getElementById('spinner').style.display = 'none';
        })
        .catch(error => {
            document.getElementById('results').innerText = 'Error fetching speedtest results';
            console.error('Error fetching speedtest results:', error);
        });
}

// Update results on page load
updateSpeedtestResults();

// Update results every 60 seconds
setInterval(updateSpeedtestResults, 60000);
