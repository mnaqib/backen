import requests
from bs4 import BeautifulSoup
import smtplib
from flask import Flask, redirect, url_for, request
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"/api": {"origins": "*"}})

@app.route('/',methods = ['POST', 'GET'])
def login():
        user = request.args.get('val')
        headers={"USER-AGENT":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
        check_price(user,headers)

def check_price(user,headers):
         page=requests.get(user,headers=headers)
         soup=BeautifulSoup(page.content,'html.parser')
         title=soup.find(id="productTitle")
         title=title.get_text()
         price=soup.find(id="priceblock_dealprice")
         price=price.get_text()
         converted_price=float(price[8:14])
         print(converted_price)
         if(converted_price<45000):
             send_mail()
         print(converted_price)
         print(title.strip())
         if(converted_price>50000):
             send_mail()
         return "hello"
def send_mail():
             server=smtplib.SMTP('smtp.gmail.com',587)
             server.ehlo()
             server.starttls()
             server.ehlo()
             server.login('siddarthsuvarna99@gmail.com','hrum nyrr qmvl twyt')
             subject="yaayyyyy "
             body='maadarkutta'
             msg=f"Subject:{subject}\n\n{body}"
             server.sendmail(
                 'siddarthsuvarna99@gmail.com',
                 'naqibdargaroad@gmail.com',
                 msg
             )
             print('hey mail was sent')
             server.quit()
             return "sendm"




if __name__ == '__main__':
     app.run(debug = True)
