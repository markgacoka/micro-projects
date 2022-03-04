from twilio.rest import Client

#testaccountSid = 'AC493a8129f20a252cf14bd490948c0b00'
#testAuthToken = '50a36dbec29da8d7ac44ab1cf9700b7d'
#client = Client(testaccountSid, testAuthToken)

accountSid = 'TWILIO ACCOUNT API ID'
authToken = 'TWILIO AUTH TOKEN'
client = Client(accountSid, authToken)

print("Sending message...")
myMessage = client.messages.create(body="CUSTOM MESSAGE", from_='NUMBER BY TWILIO', to='YOUR NUMBER')
#myMessage = client.messages.create(body="CUSTOM MESSAGE", from_='NUMBER BY TWILIO', to='YOUR NUMBER')
print("Sent message")
