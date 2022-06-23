import pika

print("\n",pika.__version__)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

antrian=input("Masukkan nama Queue Pesan : ")
channel.queue_declare(queue=antrian)

pesan=input("Masukkan Pesan : ")
channel.basic_publish(exchange='', routing_key=antrian, body=pesan)
print("[x] Mengirim Pesan = ",pesan,'=> ke Queue =',antrian)
connection.close()
