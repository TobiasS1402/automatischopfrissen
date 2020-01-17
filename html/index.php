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

img {
height: 700px;
position: absolute;
left: 53%;
top: 8%;
}

th {
background-color: #588c7e;
color: #FFE4E1;
}

caption {
font-size: 40px;
}

.button {
background-color: #588c7e;
border: none;
color: white;
padding: 15px 32px;
text-align: center;
text-decoration: none;
display: inline-block;
font-size: 16px;
position: absolute;
top: 9%;
left: 71%;
cursor: pointer;
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
$query = ("select * from voorraad ORDER BY voorraadaantal ASC");
$query1 = ("select voorraad.productnaam, mutatie.datum, mutatie.tijd from mutatie INNER JOIN voorraad ON mutatie.productid = voorraad.productid ORDER BY mutatie.datum, mutatie.tijd DESC LIMIT 10");

$result = $con->query($query);
$result1 = $con->query($query1);
?>
<table class="table1">
<caption>Voorraad database</caption>
<tr>
    <th>Id</th>
    <th>Naam</th>
    <th>Aantal</th>
    <th>Prijs</th>
</tr>

<?php
	while($row = $result->fetch_assoc()) {
	echo "<tr><td>" . $row["productid"]. "</td><td>" . $row["productnaam"] . "</td><td>" . $row["voorraadaantal"] . "</td><td>" . $row["prijs"]. "</td></tr>";
	}
?>
</table>
<table class=table1>
<caption>Mutatie database: laatste 10 mutaties</caption>
<tr>
    <th>Product</th>
    <th>Datum</th>
    <th>Tijd</th>
</tr>

<?php
	while($row = $result1->fetch_assoc()) {
	echo "<tr><td>" . $row["productnaam"]. "</td><td>" . $row["datum"] . "</td><td>" . $row["tijd"] . "</td></tr>";
	}
	mysqli_close($con);
?>
</table>
<img src="favicon.png">
<a href="voorraad.php" class="button">voorraad aanpassen</a>
</body>
</html>
