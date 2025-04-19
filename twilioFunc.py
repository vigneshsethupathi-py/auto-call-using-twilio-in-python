from twilio.rest import Client
# from urllib.parse import urlencode
import time

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACa2d7e4a05d02160c89d30ac181626757'
auth_token = '0a33a9b3c24ce23f76d204b0aef46ce9'
client = Client(account_sid, auth_token)

def makeCall():
    call = client.calls.create(
        to='+919944658682',
        from_='+17433306905',
        # url='https://handler.twilio.com/twiml/EHfbb90737b757304c9b3cbcb81ba73770?' + urlencode(
        #     {'Message': "hey sorry to say that application has failed"})
        # url = 'https://www.twilio.com/console/twiml-bins/EHfbb90737b757304c9b3cbcb81ba73770'

    )

    print(call.sid)
    call_sid = call.sid

    time.sleep(10)

    call = client.calls(call_sid).fetch()
    print(call.status)


# def sendSMS(msg):
#     message = client.messages \
#         .create(
#         body=msg,
#         from_='+17433306905',
#         to='+917824924825'
#     )

    # print(message.sid)

# from twilio.rest import Client
# sid = 'ACa2d7e4a05d02160c89d30ac181626757'
# token = '0a33a9b3c24ce23f76d204b0aef46ce9'
# ct = Client(sid,token)
# to=''
# ct.messages.create(body="welcome to learn python",from_='+17433306905',to='+917824924825')
