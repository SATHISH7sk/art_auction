#!C:\Python311\python.exe
print("Content-Type:text/html\n\r")

import cgi

print('''
<html><head>
<style>
body{
background-image:url('img3.jpg');
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

.l1
{
position:absolute;
height: 500px;
width: 500px;
background-color:pink;


}
</style></head>
<body>

<ul>
  <li><a href="home.py">Home</a></li>
  <li><a href="hcm.html">log out</a></li>
  <li><a href="about.py">About</a></li>
  <li><a class="active">+ Add Patient </a></li>
  <br>
    Contact Us : +91 9345067935
</ul>
<br><br>
<b><center>Art</center><br><br>
<br><br>
<center>
<html>

<form action="save.py" enctype="multipart/form-data">
art id     :<input type="number" name="n" style="margin-left:37px;">
<br><br>
base price      :<input type="number" name="a" style="margin-left:53px;">
<br><br>
<input type="file" name="image">
<input type="submit" value="Upload">
</form>
</center>

</div></center>
</body>
</html>
''')
