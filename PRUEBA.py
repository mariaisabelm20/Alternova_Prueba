import requests #Para realizar solicitudes a un HTTP
import json #Almacena datos
from twilio.rest import Client



result = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,binancecoin&vs_currencies=usd").text 
result = json.loads(result) #Convierte la info del Json en data de Python

binancecoin_price = float(result["binancecoin"]["usd"])
bitcoin_price = float(result["bitcoin"]["usd"])
ethereum_price = float(result["ethereum"]["usd"])

#Archivo json editable
credenciales = open('credenciales.json') # Abre el json
data = json.load(credenciales) 

account_sid = (data["account"])
auth_token = (data["token"])
client = Client(account_sid, auth_token)

#Numeros de emisor y receptor
from_whatsapp_number = (data["from_whatsapp_number"])
to_whatsapp_number = (data["to_whatsapp_number"])


#Automatización
messages = [] #Lista que almacena los mensajes
if binancecoin_price>= 300:
    messages.append(f"Alerta! el precio del Binancecoin ha superado los 300 USD.\nPrecio actual: {binancecoin_price} USD")
    
if bitcoin_price>= 30000:
    messages.append(f"Alerta! el precio del Bitcoin ha superado los 30,000 USD.\nPrecio actual: {bitcoin_price} USD")
    
if ethereum_price>= 2000:
    messages.append(f"Alerta! el precio del Ethereum ha superado los 2,000 USD.\nPrecio actual: {ethereum_price} USD")
        
#Para imprimir todos los mensajes
if messages:
    final_message = "\n\n".join(messages) #Aquí se unen los mensajes
    message = client.messages.create(body=final_message ,
                       from_ = from_whatsapp_number, 
                       to = to_whatsapp_number)    
        
    print(final_message)
        
else:
    print("No hay alertas")
 

