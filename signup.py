#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

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
  <li><a class="active" href="signup.py">sign up</a></li>
  <li><a href="login.py">log in</a></li>
  <br>
    Contact Us : +91 9345067935
</ul>

<form action="login.py"> 
<br><br>
<br><br>
<center>
NAME     :<input type="text" name="n" style="margin-left:37px;">
<br><br>
AGE      :<input type="number" name="a" style="margin-left:53px;">
<br><br>
DOB      :<input type="date" name="d" style="margin-left:112px;">
<br><br>
<input type="radio" name="g" value="1"> MALE
<input type="radio" name="g" value="1"> FEMALE
<input type="radio" name="g" value="0"> OTHERS
<br><br>
EMAIL    :<input type="email" name="e" style="margin-left:39px;">
<br><br>
ADDRESS  :<input type="text" name="add" style="margin-left:17px;">
<br><br>
PASSWORD :<input type="password" name="p" style="margin-left:4px;">
<br><br>

<input type="submit" value="SIGN UP"><br><br>
</center>
</form></body>
</html>
''')

