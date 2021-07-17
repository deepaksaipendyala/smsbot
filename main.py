from twilio.rest import Client 
 
account_sid = 'ACd341aa3138996a1dddb1be6422976fe4' 
auth_token = 'secret key' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MGdf36c51ac8631585e10c6f44e9e6302e', 
                              body='Hello',      
                              to='+919398388460' 
                          ) 
 
print(message.sid)