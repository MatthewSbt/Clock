import speedtest

test = speedtest.Speedtest()
test.get_best_server()  # Prepara il test
print(dir(test))  # Mostra tutti gli attributi e i metodi disponibili
