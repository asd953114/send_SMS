
#download twilio package
#twilio website get sid and token

from twilio.rest import Client

account_sid = "input your sid"

auth_token = "input your token"

client = Client(account_sid, auth_token)

message = client.messages.create(
	to="+88691234567",  # input the phone you want to send 
	from_="+12019039648", # the number twilio give you 
	body="Hello every one!"  # input what you want to send
	)

print(message.sid)