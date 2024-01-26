import socket
import json
 
HOST= "127.0.0.1" #indirizzo del server
PORT= 65432 #porta usata dal server
DIM_BUFFER= 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
    sock_service.connect((HOST, PORT))
    while True:
        primoNumero=float(input("Inserisci primo numero: "))
        operazione=input("Inserisci l'operazione (+,-,*,/,%)")
        secondoNumero=float(input("Inserisci secondo numero: "))
        messaggio={'primoNumero': primoNumero,
                   'operazione': operazione,
                   'secondoNumero': secondoNumero}
        messaggio=json.dumps(messaggio)
        sock_service.sendall(messaggio.encode("UTF-8"))

        data=sock_service.recv(DIM_BUFFER)
        print("Risultato: ", data.decode())
        
        risposta=input("Vuoi continuare? s-n ")
        if(risposta=="n"):
            break
        

#a questo punto la socket è stata chiusa automaticamente