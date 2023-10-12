#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")
import pymysql
db=pymysql.Connect(host="localhost",user="root",password="satheesh29",database="satheesh")
cur=db.cursor()
#cur.execute("use satheesh")
#cur.execute("create table bid2(email varchar(35),bid int(6))")
import cgi
form=cgi.FieldStorage()

email=form.getvalue("e1")
b_amt=form.getvalue("b")


query="insert into bid2 values(%s,%s)"
val=[email,b_amt]
cur.execute(query,val)
db.commit()

print('''
<html>
  <head>
    <style>
      /* Center label */
      .center {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
      }
    </style>
  </head>
  <body>
    <div class="center">
      <h1>YOU ARE SUCCESSFULLY SUBMITTED YOUR BID AMOUNT..</h1>
    </div>
  </body>
</html>''')











































'''form=cgi.FieldStorage()
img=str(form.getvalue("image"))
bp=form.getvalue("a")
idy=form.getvalue("n")
with open(img, "rb") as f:
    fi2 = f.read()
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="satheesh29",
    database="satheesh"
)
cursor = conn.cursor()
sql = "INSERT INTO img2 VALUES (%s,%s,%s)"
values = (idy,fi2,bp)
cursor.execute(sql, values)
conn.commit()
conn.close()

'''
