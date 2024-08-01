document.addEventListener("DOMContentLoaded", function() {
    fetch('http://127.0.0.1:5000/speedtest')
        .then(response => response.json())
        .then(data => {
            document.getElementById('download-speed').textContent = data.download.toFixed(2);
            document.getElementById('upload-speed').textContent = data.upload.toFixed(2);
            document.getElementById('ping-time').textContent = data.ping.toFixed(2);
        })
        .catch(error => {
            console.error('Error fetching speedtest results:', error);
        });
});
