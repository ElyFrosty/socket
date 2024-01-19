import socket
import json

#Configurazione del server
IP= "127.0.0.1"
PORTA= 65432
DIM_BUFFER= 1024


#Creazione della socket del server con il costrutto with
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:

    #Binding della socket alla porta specificata
    sock_server.bind((IP, PORTA))

    #Metti la socket in ascolto per le connessioni in ingersso
    sock_server.listen()

    print(f"Server in ascolto su {IP}:{PORTA}...")

    #Loop principale del server
    while True:
        #Accetta le connessioni
        sock_service, address_client=sock_server.accept()
        with sock_service as sock_client:
            while True:
                #Leggi i dati inviati dal client
                dati=sock_client.recv(DIM_BUFFER).decode()
                dati=json.loads(dati)
                primoNumero=dati['primoNumero']
                operazione=dati['operazione']
                secondoNumero=dati['secondoNumero']
                print(primoNumero, operazione, secondoNumero)
                if(operazione=="+"):
                    risultato= primoNumero+secondoNumero
                elif(operazione=="-"):
                    risultato= primoNumero-secondoNumero
                elif(operazione=="*"):
                    risultato= primoNumero*secondoNumero
                elif(operazione=="/"):
                    if(secondoNumero!=0):
                        risultato= primoNumero/secondoNumero
                    else:
                        risultato="impossibile"
                elif(operazione=="%"):
                    risultato= (primoNumero*secondoNumero)/100
                else:
                    print("operatore non valido")

                print(risultato)
                risultato=(str(risultato))
                sock_client.sendall(risultato.encode())