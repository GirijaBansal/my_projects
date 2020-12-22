from twilio.rest import Client 
 
account_sid = 'ACec33ea0a8ba567843473a3ea67e9fecf' 
auth_token = '5074b6c51131a1f9b89b9750942a19a5' 
client = Client(account_sid, auth_token) 
def job_function(): 
        message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Gudmorning ',      
                              to='whatsapp:+918923397522' 
                          ) 
 
        print(message.sid)

