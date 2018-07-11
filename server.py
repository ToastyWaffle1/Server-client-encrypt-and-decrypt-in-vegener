# first of all import the socket library
# message = list name [0]
#key = list name [1]
port = 12345 
import socket               
import sys
from _thread import *
from vignare import *

def do_something(text, key): 
    f = open("no_need_toworry.txt", "w")
    encrypted = encrypt(text,key)
    f.write("Encrypted data goes here " + encrypted)
    f.close()
    return encrypted
    

def client_thread(conn, ip, port, MAX_BUFFER_SIZE = 12345):
    input_from_client_bytes = conn.recv(MAX_BUFFER_SIZE)
    import sys
    siz = sys.getsizeof(input_from_client_bytes)
    if  siz >= MAX_BUFFER_SIZE:
        print("The length of input is probably too long: {}".format(siz))

    input_from_client = input_from_client_bytes.decode("utf8").rstrip()
    mylist = input_from_client.split(',')
    message = mylist[0]
    key = mylist[1]
    
    res = do_something(message, key)
    print("Result of processing {} is: {}".format(input_from_client, res))
# next create a socket object        
    print ("Socket successfully created")
    vysl = res.encode("utf8")  # encode the result string
    conn.sendall(vysl)  # send it to client
    conn.close()  # close connection
    print('Connection ' + ip + ':' + port + " ended")

def start_server():
# reserve a port on your computer in our
# case it is 12345 but it can be anything               
    import socket
    s = socket.socket() 
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this is for easy starting/killing the app
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('Socket created')

    try:
        soc.bind(("127.0.0.1", 12345))
        print('Socket bind complete')
    except socket.error as msg:
        import sys
        print('Bind failed. Error : ' + str(sys.exc_info()))
        sys.exit()
    soc.listen(10)
    print('Socket now listening')

    from threading import Thread

    while True:
        conn, addr = soc.accept()
        ip, port = str(addr[0]), str(addr[1])
        print('Accepting connection from ' + ip + ':' + port)
        try:
            Thread(target=client_thread, args=(conn, ip, port)).start()
        except:
            print("Terible error!")
            import traceback
            traceback.print_exc()
    soc.close()

start_server()  
f = open("no_need_toworry.txt", "w")
f.write("Encrypted data goes here ")
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests 
# coming from other computers on the network
s = socket.socket()
s.bind(('127.0.0.1', port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)     
print ("socket is listening") 

def clientthread(conn):
    conn.send("Welcome to the server. Type something and hit enter\n")         
    while True:
        data = conn.recv(1024)
        reply = "OK..." + data
        if not data:
            break
        conn.sendall(reply)
    conn.close()

# a forever loop until we interrupt it or 
# an error occurs
while True:
 
    # Establish connection with client.
    conn, addr = s.accept()
    print ('Connected with ' + addr[0] + ':' + str(addr[1]))
    
    # send a thank you message to the client. 
    conn.send(b'Thank you for connecting')

    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
    # Close the connection with the client
    conn.close()
