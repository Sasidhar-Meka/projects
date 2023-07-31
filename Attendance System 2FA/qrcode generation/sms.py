#Code for sms which sends the QR code via sms
import os
from twilio.rest import Client
import schedule
import time

def gio():
 account_sid="AC2e49786f5cbb33fa2a405937718b41fe"
 auth_token="811c4954baa7becdb53ceaf4cfd149dc"
 client = Client(account_sid,auth_token)
 message=client.messages.create( 
 body="ಇದು ಇಂದಿನ ನಿಮ್ಮ QR CODE ಆಗಿದೆ  https://postimg.cc/CdzC3fQN",
 from_="+15674832675",
 to="+918147553087")

 message1=client.messages.create( 
 body="ಇದು ಇಂದಿನ ನಿಮ್ಮ QR CODE ಆಗಿದೆ  https://postimg.cc/kV2XJq3k",
 from_="+15674832675",
 to="+919035177411")

 print(message.sid)
 print(message1.sid)

schedule.every(5).seconds.do(gio)
while True:
    schedule.run_pending()
    time.sleep(1)


#The "twilio.rest" module is imported, which provides the client class needed to interact with the Twilio API.
#The "os" module is imported, which provides a way to interact with the operating system, such as accessing environment variables or running system commands.
#The "Client" class is imported from the "twilio.rest" module, and is used to create a client object that can interact with the Twilio API using your account credentials.
#The "auth_token" is a secret key that authenticates requests made to the Twilio API on behalf of your account. It can also be found on the Twilio Console dashboard.
#The "Client" constructor takes in the "account_sid" and "auth_token" variables as arguments to authenticate the client object.
#Overall, these lines of code establish a connection to the Twilio API using your Twilio account credentials, which is required to send SMS messages or make phone calls using Twilio services.