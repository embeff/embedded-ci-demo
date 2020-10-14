import pika
import uuid
from datetime import datetime


class RabbitRPC(object):
    def __init__(self, timeout_s, message_host=None, url=None):
        if url is not None:
            self.connection = pika.BlockingConnection(pika.URLParameters(url))
        else:
            cr = pika.PlainCredentials('node', 'node')
            self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=message_host,
                                                                            credentials=cr))
        self.channel = self.connection.channel()

        # queue.configure permissions (passivew=false)
        # Empty name given, the server will create a unique name!
        result = self.channel.queue_declare(queue="", exclusive=True)
        self.callback_queue = result.method.queue
        self.start_time = datetime.now()
        self.timeout_s = timeout_s

        # queue.read permission
        self.channel.basic_consume(on_message_callback=self.on_response, auto_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, target_queue, body_content):
        self.response = None
        self.corr_id = str(uuid.uuid4())

        # exchange.write
        self.channel.basic_publish(exchange='',
                                   routing_key=target_queue,
                                   properties=pika.BasicProperties(
                                       reply_to = self.callback_queue,
                                       correlation_id = self.corr_id,
                                   ),
                                   body=body_content)
        while self.response is None:
            elapsed = datetime.now() - self.start_time
            if elapsed.total_seconds() > self.timeout_s:
                self.connection.close()
                return None
            self.connection.process_data_events()
        return self.response
