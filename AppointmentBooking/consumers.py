from email import message
import json
from channels.generic.websocket import WebsocketConsumer

class ChatConsumer(WebsocketConsumer):
      def connect(self):
          self.accept() 
          self.send(text_data=json.dumps({
                'message': 'Hi I am your bot assistant'
          }))

      
      def disconnect(self, code):
          pass

      def receive(self, text_data=None, bytes_data=None):
           x = {
               'hello':'Hello, How can I help you',
               'who':'I am your bot',
               'who are you':'I am your bot',
               'appointment':'available packages',
               'types':'Namaste,This is berry salon located in Durbarmarg Nepal.We have every hair cut here whatever you wished such Chopped Layers,Perfect V Shaped Hair Cut,Pixie cut,Feather Cut,etc And they are affordable for sure that for any hair cut it is Rs.500',
               'Where is this salon located':"Namaste,This is berry salon located in Durbarmarg Nepal.We have every hair cut here whatever you wished such Chopped Layers,Perfect V Shaped Hair Cut,Pixie cut,Feather Cut,etc And they are affordable for sure that for any hair cut it is Rs.500",
               'Services':'Hair-cut and styling,Body Massage, Bridal makeup,Tanning,Anti-aging services,Stretch mark removal,Threading and waxing,Manicure and predicure are the services provided here.Which of the services would you like to book?,The services provided here are Hair-cut and styling,Body Massage, Bridal makeup,Tanning,Anti-aging services,Stretch mark removal,Threading and waxing,Manicure and predicure ',
               'services':'Hair-cut and styling,Body Massage, Bridal makeup,Tanning,Anti-aging services,Stretch mark removal,Threading and waxing,Manicure and predicure are the services provided here.Which of the services would you like to book?,The services provided here are Hair-cut and styling,Body Massage, Bridal makeup,Tanning,Anti-aging services,Stretch mark removal,Threading and waxing,Manicure and predicure ',
               'Hair-cut & styling':'Namaste,This is berry salon located in Durbarmarg Nepal.We have every hair cut here whatever you wished such Chopped Layers,Perfect V Shaped Hair Cut,Pixie cut,Feather Cut,etc And they are affordable for sure that for any hair cut it is Rs.500',
               'Body Massage':'Massage:A sense of deep relaxation and serenity is one of the instant effects of massage. Massage causes the production of endorphins, which are brain chemicals (neurotransmitters) that induce sensations of happiness.It is done professionally with 100 percent comfortness on in Rs.1500.The types are head and shoulder with feet massage,Hotstone massage,soft massage',
               'Bridal makeup':'Bridal makeup is done to look extra beautiful during their special day to give a different glow during their marriage.The price starts with Rs.25,000 ',
               'Tanning':'Tanning is a browning of the skin caused by sun exposure. The majority of people desire a healthy glow so here we provide tanning solution start with Rs.800 only',
               'Anti-aging services':'The benefits of a good anti-aging skincare practice include maintaining the skin firmness, improving the skin tone, minimizing the appearance of fine lines and wrinkles, and boosting brightness and radiance start with Rs.1800 package',
               'Stretch mark removal':'Stretch marks are not physically unpleasant, but they can have a negative impact on a person self-esteem and confidence. The elimination of striae (stretch marks) by laser resurfacing is known as laser stretch mark removal. It helps to rebuild the overlaying skin by removing the outer layer of skin.The price for stretch mark removal is Rs 5000 only',
               'Threading and waxing':'Threading and waxing is done to look cleaner so that one can look confident.The price for it is different from hair and it is started with Rs.200',
               'Manicure and Predicure':'Manicures and pedicures increase blood flow, which aids in cellulite reduction, skin tightening, and muscle strengthening, all of which can improve the appearance of your hands and feet.So,the price is Rs.5000 for whole package.Thank you'
          }
           respoonse = "I am your bot"
           message= (json.loads(text_data))['message']
           for i in x:
               if(message == i):
                   respoonse = x[i]
          
           self.send(text_data=json.dumps({
                'message': respoonse
          }))


