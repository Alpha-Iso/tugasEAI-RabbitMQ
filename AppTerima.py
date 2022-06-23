import pika
import sys
import os


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    antrian=input("\nMasukkan Queue Pesan : ")
    channel.queue_declare(queue=antrian)

    def callback(ch, method, properties, body):
        print("[x] Menerima Pesan %r" % body)

    channel.basic_consume(
        queue=antrian, on_message_callback=callback, auto_ack=True)

    print(' [*] Menunggu Pesan dari Queue',antrian,'...')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
