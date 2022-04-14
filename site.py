import socket,random


TCP_IP = '0.0.0.0'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(5)

while 1:
    s2 = s.accept()
    conn, addr = s2
    print('Connection address:', addr)

    data = conn.recv(BUFFER_SIZE)
    if len(data)!=0:
        print ("received data:", data)
        if data[:3] == b"inf":
            HumidityA = "%.2f" % (random.random()*100)
            HumidityG = "%.2f" % (random.random() * 100)
            temperature = "%.2f" % (random.random() * 30)
            Waterlvl = "%.2f" % (random.random() * 100)
            inf = "Air Humidity: " +str(HumidityA) + "% \nSoil Humidity: " +str(HumidityG) +"% \nTemperature: "+str(temperature) +"\nWater LVL: "+ str(Waterlvl)+"%"
            conn.send(inf.encode())
            print("sent inf", inf)
        else:
            conn.send(data)  # echo
conn.close()
