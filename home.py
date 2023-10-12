#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import pymysql
#pymysql.install_as_MySQLdb()
#import MySQLdb

db=pymysql.Connect(host="localhost",user="root",password="satheesh29",database="satheesh")
cur=db.cursor()
'''sql = "SELECT image FROM img2 WHERE id=%s"
values = (2313)
cur.execute(sql, values)
image= cur.fetchone()[0]
content_type = "img2/jpg" if image.startswith(b'\x89JPG\r\n\x1a\n') else "img2/jpg"

print("Content-Type: img2/jpg")  # Replace "image/jpeg" with the appropriate content type for your image
print("Content-Length: " + str(len(image)))
print()
print(image)

# Close the database connection
db.close()'''
sql = "SELECT email FROM bid2"
cur.execute(sql)
email = [row[0] for row in cur.fetchall()]
sql = "SELECT bid FROM bid2"
cur.execute(sql)
amt = [row[0] for row in cur.fetchall()]

db.close()
auction={}
for i in email:
    for j in amt:
        auction[i]=j


highest_bidder = max(auction)


highest_bid = max(auction.values())







print('''
<html>
<style>
body{
background-image:url('im.jpg');
background-repeat:no-repeat;
background-size:cover;}
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
  color: white;
}

li {
  float: right;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover:not(.active) {
  background-color: #111;
}
h1{
    background-color: red}
.active {
  background-color: #FF0000;
}
#st1
{
position:absolute;
height:600px;
width:400px;
margin-left:360px;
margin-top:30px;



}
</style>
<body>

<ul>
  <li><a class="active" href="home.py">Home</a></li>
  <li><a href="signup.py">log out</a></li>
  <br>
    Contact Us : +91 9345067935
</ul>
</body>
<br>
<div style="display: flex; align-items: center;">
  <img src="img1.jpg" style="max-width: 50%;">
  <div style="margin-left: 20px;">
    <h2>NIGHT SKY(2023)</h2>
    <p>Oil painting by SatheeshKumar.</p>
    <p>One of kind art work</p>
    <p>size: 30x40x2 cm(Unframed)</p>
    <br>
    <label>Base price : 2000$</label><br>
    <br><form action="save.py">
    EMAIL    :<input type:"email" name="e1" style="margin-left:39px;"><br><br>
    BID AMT :<input type:"number" name="b" style="margin-left:26px;">
    <input type="submit" value="ASK BID"><br><br>
   </form>
<br><br>


  </div>
</div>
    <h2>ARTIST DESCRIPTION :</h2>
    <P>Night Sky, oil painting on canvas without frame as edges are painted 100%,handmade high Quality oil.
    For interior or gift,Ready to hang</P>
    <h2>Material used:</h2>
    <p>oil</p>

<center>---HIGHEST BID---</center>
</html>
''')
print('''<center><h1>''')
print(highest_bid)

print('''</center></h1>''')
print('''<center>---HIGHEST BIDDER---</center>''')
print('''<center><h1>''')
print(highest_bidder)

print('''</center></h1>''')
from email.message import EmailMessage
import ssl
import smtplib
import time

# Wait for 10 minutes (600 seconds)
time.sleep(25)
email_s='sksatheeshu29@gmail.com'
email_p='hryxjtanyuzeckmb'
email_r=highest_bidder
subject="cofirmation mail for winning a bid"
body=("Congratulation,You are successfully won your art auction in a amount of "+str(highest_bid))

em=EmailMessage()
em["From"]=email_s
em["To"]=email_r
em["Subject"]=subject
em.set_content(body)
context=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
    smtp.login(email_s,email_p)
    smtp.sendmail(email_s,email_r,em.as_string())

print('''<center><h1 style="background-color:powderblue;>---SOLD---</h1></center>''')
