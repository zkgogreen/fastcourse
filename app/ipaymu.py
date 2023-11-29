import requests
import json
from datetime import datetime
import hashlib
import hmac
from user.models import Users


ipaymuVa  = "0000002211550124" #your iPaymu VA
ipaymuKey = "SANDBOX8D4C5345-E4D0-42C7-91B0-527ED25FF18E-20220729234011" #your iPaymu API Key
ipaymuUrl = "https://sandbox.ipaymu.com/api/v2/payment" #production: https://my.ipaymu.com

def pay(request, product, price, ref_id):
    ref_id = str(ref_id)
    user = Users.objects.get(user=request.user)
    name  = request.user.first_name+" "+request.user.last_name
    phone = user.phone
    email = request.user.email
    body =  {
                "product":[product],
                "qty":["1"],
                "price":[price],
                "fee":3500,
                "returnUrl":"http://"+request.get_host()+"/user/bootcamp/confirm/thank", #your thank you page url
                "notifyUrl":"http://"+request.get_host()+"/user/bootcamp/confirm/callback/"+ref_id, #your callback url
                "referenceId":ref_id, #your reference id or transaction id
                "buyerName":name, #optional
                "buyerPhone":phone, #optional
                "buyerEmail":email, #optional
                "feeDirection":"BUYER"
            } 

    data_body    = json.dumps(body)
    data_body    = json.dumps(body, separators=(',', ':'))
    encrypt_body = hashlib.sha256(data_body.encode()).hexdigest()
    stringtosign = "{}:{}:{}:{}".format("POST", ipaymuVa, encrypt_body, ipaymuKey)
    signature    = hmac.new(ipaymuKey.encode(), stringtosign.encode(), hashlib.sha256).hexdigest().lower()

    timestamp    = datetime.today().strftime('%Y%m%d%H%M%S')

    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json',
        'signature': signature,
        'va':ipaymuVa,
        'timestamp':timestamp
    }
    response = requests.post(ipaymuUrl, headers=headers, data=data_body)
    data = json.loads(response.text)
    if data["Success"]:
        return data["Data"]["Url"], data["Data"]["SessionID"]
    else:
        print(data["Message"])

def callback(request, ref_id):
    url = "http://"+request.get_host()+"/user/bootcamp/confirm/callback/"+str(ref_id),
    payload={}
    files={}
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

def transaksi(id):
    ipaymuUrl = "https://sandbox.ipaymu.com/api/v2/transaction" #production: https://my.ipaymu.com
    body =  {
                "transactionId":id #ipaymu transaction id
            } 

    data_body    = json.dumps(body)
    data_body    = json.dumps(body, separators=(',', ':'))
    encrypt_body = hashlib.sha256(data_body.encode()).hexdigest()
    stringtosign = "{}:{}:{}:{}".format("POST", ipaymuVa, encrypt_body, ipaymuKey)
    signature    = hmac.new(ipaymuKey.encode(), stringtosign.encode(), hashlib.sha256).hexdigest().lower()

    timestamp    = datetime.today().strftime('%Y%m%d%H%M%S')

    headers = {
        'Content-type': 'application/json',
        'Accept': 'application/json',
        'signature': signature,
        'va':ipaymuVa,
        'timestamp':timestamp
    }
    response = requests.post(ipaymuUrl, headers=headers, data=data_body)

    data = json.loads(response.text)
    if data["Success"]:
        return data
    else:
        print(data["Message"])