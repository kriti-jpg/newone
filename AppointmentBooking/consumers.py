from email import message
import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
      def connect(self):
          print('connected')
          self.accept() 
          self.send(text_data=json.dumps({
                'message': 'Hello world'
          }))

      
      def disconnect(self, code):
          pass

      def receive(self, text_data=None, bytes_data=None):
          text_data_json = json.load(text_data)
          message = text_data_json['message']
      
          self.send(text_data=json.dumps({
                'message': 'Hello world'
          }))


