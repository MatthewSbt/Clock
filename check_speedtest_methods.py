import speedtest

def run_speedtest():
    """
    Esegue un test di velocità della rete e stampa i risultati.
    """
    try:
        # Crea un'istanza dell'oggetto Speedtest
        test = speedtest.Speedtest()

        # Trova il miglior server per il test
        print("Selezionando il miglior server...")
        test.get_best_server()
        best_server = test.best
        print(f"Miglior server selezionato: {best_server['host']} ({best_server['name']}, {best_server['country']})")

        # Test della velocità di download
        print("Esecuzione del test di velocità di download...")
        download_speed = test.download() / 1_000_000  # Converti da bit/s a Mbit/s
        print(f"Velocità di download: {download_speed:.2f} Mbps")

        # Test della velocità di upload
        print("Esecuzione del test di velocità di upload...")
        upload_speed = test.upload() / 1_000_000  # Converti da bit/s a Mbit/s
        print(f"Velocità di upload: {upload_speed:.2f} Mbps")

        # Test del ping
        print("Esecuzione del test del ping...")
        ping = test.results.ping
        print(f"Ping: {ping} ms")

        # Mostra i risultati del test
        print("\nRisultati del test:")
        print(f"Server: {best_server['host']} ({best_server['name']}, {best_server['country']})")
        print(f"Velocità di download: {download_speed:.2f} Mbps")
        print(f"Velocità di upload: {upload_speed:.2f} Mbps")
        print(f"Ping: {ping} ms")

    except speedtest.SpeedtestException as e:
        # Gestione delle eccezioni specifiche di speedtest-cli
        print("Errore specifico di speedtest-cli:", e)
    except Exception as e:
        # Gestione delle eccezioni generali
        print("Si è verificato un errore durante il test di velocità:", e)

# Esegui il test di velocità
if __name__ == "__main__":
    run_speedtest()