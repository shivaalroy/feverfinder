# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
import pg8000

class Tool:
  def __init__(self,db,user):
    self.conn = pg8000.connect(database=db,username=user)
    self.cursor = self.conn.cursor()

  # Find these values at https://twilio.com/user/account
  def send_sms(self):
    account_sid = "ACa0c36a49660ad461c086aaab8b2b850e"
    auth_token = "b4e8e5e6986dedb1fd52572d2f63ab34"
    client = TwilioRestClient(account_sid, auth_token)

    message = client.messages.create(to="+14087868804", from_="+18312466221",
                                     body="ALERT! High temperature in bed 14.")

  def addTemperature(self,temp,time):
    self.cursor.execute("INSERT INTO temperatures (temperature, time) VALUES (" + str(temp) + ", " + str(time) + ")")
    self.conn.commit()