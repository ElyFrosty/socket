import socket
import json

SERVER_IP= "127.0.0.1"
SERVER_PORT= 5005
BUFFER_SIZE= 1024

#creazione del socket
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    primoNumero=float(input("Inserisci primo numero: "))
    operazione=input("Inserisci l'operazione (+,-,*,/,%)")
    secondoNumero=float(input("Inserisci secondo numero: "))
    messaggio={'primoNumero': primoNumero,
               'operazione': operazione,
               'secondoNumero': secondoNumero}
    messaggio=json.dumps(messaggio)
    s.sendto(messaggio.encode("UTF-8"), (SERVER_IP,SERVER_PORT))

    data=s.recv(BUFFER_SIZE)
    print("Risultato: ", data.decode())

    risposta=input("Vuoi continuare? s-n ")
    if(risposta=="n"):
        break
 
s.close()
