<!DOCTYPE html>
<html>
<head>
<title>Frisdrankautomaat webpagina</title>
<style>
    table {
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
$query1 = ("select voorraad.productnaam, mutatie.datum, mutatie.tijd from mutatie INNER JOIN voorraad ON mutatie.productid = voorraad.productid ORDER BY datum ASC LIMIT 10");

$result = $con->query($query);
$result1 = $con->query($query1);
?>
<table>
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
<table>
<caption>Mutatie database: laatste 10 mutaties</caption>
<tr>
    <th>Product</th>
    <th>Datum</th>
    <th>Naam</th>
</tr>

<?php
	while($row = $result1->fetch_assoc()) {
	echo "<tr><td>" . $row["productnaam"]. "</td><td>" . $row["datum"] . "</td><td>" . $row["tijd"] . "</td></tr>";
	}
	mysqli_close($con);
?>
</table>
</body>        
</html>

