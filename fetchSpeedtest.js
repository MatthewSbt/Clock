// Function to update speedtest results
function updateSpeedtestResults() {
    // Show the spinner while loading
    const spinner = document.getElementById('spinner');
    const resultsContainer = document.getElementById('results');
    spinner.style.display = 'block';
    resultsContainer.innerHTML = ''; // Clear previous results

    fetch('http://127.0.0.1:5000/speedtest')
        .then(response => {
            // Check if the response is OK
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Log the fetched data for debugging
            console.log('Fetched data:', data);

            // Ensure data contains the expected properties and are numbers
            if (data && 
                typeof data.download === 'number' && 
                typeof data.upload === 'number' && 
                typeof data.ping === 'number') {
                
                // Update the results on the page
                resultsContainer.innerHTML = `
                    <div>Download Speed: <strong>${data.download.toFixed(2)} Mbps</strong></div>
                    <div>Upload Speed: <strong>${data.upload.toFixed(2)} Mbps</strong></div>
                    <div>Ping Time: <strong>${data.ping.toFixed(2)} ms</strong></div>
                `;
            } else {
                // Handle unexpected data format
                throw new Error('Invalid data format');
            }
        })
        .catch(error => {
            // Show error message in the results container
            resultsContainer.innerText = 'Error fetching speedtest results';
            console.error('Error fetching speedtest results:', error);
        })
        .finally(() => {
            // Hide the spinner after processing
            spinner.style.display = 'none';
        });
}

// Initial load of results on page load
updateSpeedtestResults();

// Set interval to update results every 60 seconds
setInterval(updateSpeedtestResults, 60000);
