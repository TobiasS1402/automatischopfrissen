<!DOCTYPE html>
<html>
<head>
<link rel='icon' href='favicon.png' type='image/x-icon'/>
<title>Frisdrankautomaat webpagina</title>
<style>
	
table.table1 {
float: left;
border-collapse: collapse;
width: 49%;
color: #588c7e;
font-family: monospace;
font-size: 25px;
border: 5px solid black;
text-align: center;
margin: 9px;
}

th {
background-color: #588c7e;
color: #FFE4E1;
}
  
caption {
font-size: 40px;
}

body {
background-color: #ffcaca;
}
tr:nth-child(even) {background-color: #f2f2f2}
</style>
</head>
<body>

<?php
include "/var/www/html/database/dbconnect.php";
// Check connection
if($con->connect_error){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}
// sql query
$query = ("SELECT productnaam, voorraadaantal FROM voorraad ORDER BY voorraadaantal ASC");
$result = $con->query($query);
?>

</table>
<img src="favicon.png">
</body>
</html>
