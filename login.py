#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import pymysql
db=pymysql.Connect(host="localhost",user="root",password="satheesh29")
cur=db.cursor()
#cur.execute("create database hcm")
#cur.execute("use hcm")
#cur.execute("create table hcms(name varchar(12),age int(3),dob DATE,email varchar(15),address varchar(20),password varchar(10))")

import cgi
form=cgi.FieldStorage()

name=form.getvalue("n")
email=form.getvalue("e")
passw=form.getvalue("p")
age=form.getvalue("a")
add=form.getvalue("add")
dob=form.getvalue("d")

'''query="insert into hcms values(%s,%s,%s,%s,%s,%s)"
val=[name,age,dob,email,add,passw]
cur.execute(query,val)
db.commit()'''

print('''
<html>
<style>
body{
background-image:url('img.jpg');
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
  <li><a href="first-page.html">Home</a></li>
  <li><a href="signup.py">sign up</a></li>
  <li><a class="active" href="login.py">log in</a></li>
  <br>
    Contact Us : +91 9345067935
</ul>

<form action="home.py" srtyle="height:600px; width:450px; background-color:rgb(223,255,255,0.3;">

<br><br>
<br><br>
<center>

EMAIL    :<input type:"email" name="e" style="margin-left:39px;">
<br><br>

PASSWORD :<input type:"password" name="p" style="margin-left:4px;">
<br><br>

<input type="submit" value="LOG IN"><br><br>
</center>
</form></body>
</html>
''')
