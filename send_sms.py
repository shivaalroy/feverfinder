# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "ACa0c36a49660ad461c086aaab8b2b850e"
auth_token = "b4e8e5e6986dedb1fd52572d2f63ab34"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+14087868804", from_="+18312466221",
                                     body="High temperature!")