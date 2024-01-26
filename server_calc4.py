import socket, json
from threading import Thread

SERVER_ADDRESS= '127.0.0.1'
SERVER_PORT= 22224
DIM_BUFFER=1024

def ricevi_comandi(sock_service, addr_client):
    print("Connessione con ", addr_client)
    with sock_service as sock_client:
            while True:
                #Leggi i dati inviati dal client
                dati=sock_client.recv(DIM_BUFFER).decode()
                if not dati:
                    break
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
    print("\nConnessione chiusa con %s" %str(addr_client))
                

def ricevi_connessioni(sock_listen):
    while True:
        sock_service, addr_client = sock_listen.accept()
        print("\nConnessione ricevuta da %s" %str(addr_client))
        print("Creo un Thread per servire le richieste")
        try:
            Thread(target=ricevi_comandi, args=(sock_service, addr_client)).start()
        except:
            print("Il thread non si avvia")
            sock_listen.close()

def avvia_server(indirizzo, porta):
    try:
        #Creazione della socket del server con il costrutto with
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:

            #Binding della socket alla porta specificata
            sock_server.bind((indirizzo, porta))

            #Metti la socket in ascolto per le connessioni in ingersso
            sock_server.listen()
            
            ricevi_connessioni(sock_server)
    except socket.error as errore:
        print("Errore: ", errore)
    


if __name__ == '__main__':
    avvia_server(SERVER_ADDRESS, SERVER_PORT)

print("Termina")