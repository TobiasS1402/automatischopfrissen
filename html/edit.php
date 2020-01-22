<?php
// including the database connection file
include_once("database/dbconnect.php");
 
if(isset($_POST['update']))
{    
    $productid = $_POST['id'];
    $productnaam=$_POST['productnaam'];
    $voorraadaantal=$_POST['voorraadaantal'];
    $prijs=$_POST['prijs'];    
    
 {    
    //updating the table
    $result = $con->query("UPDATE voorraad SET voorraadaantal=$voorraadaantal WHERE productid=$productid");

    //redirectig to the display page. In our case, it is index.php
    header("Location: index.php");
    }
}
?>
<?php
//getting id from url
$productid = $_GET['id'];
 
//selecting data associated with this particular id
$result = $con->query("SELECT * FROM voorraad WHERE productid=$productid");

while($res = $result->fetch_assoc())
{
    $productnaam = $res['productnaam'];
    $voorraadaantal = $res['voorraadaantal'];
    $prijs = $res['prijs'];
}
?>
<!DOCTYPE html>
<html>
<head>    
<link rel='icon' href='favicon.png' type='image/x-icon'/>
<title>Edit voorraadaantallen</title>
</head>
 
<style>
form {
float: left;
position: absolute;
top: 5.5%;
left: -0.75%;
border-collapse: collapse;
color: #588c7e;
font-family: monospace;
font-size: 25px;
border: 5px solid black;
text-align: center;
margin: 9px;
background-color: #ffffff;
}

body {
background-color: #FFE4E1;
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
top: 0%;
left: 0%;
cursor: pointer;
}

td {
background-color: #ffffff;
}

</style>
 
<body>
    <a href="index.php" class=button>Home</a>
    <br/><br/>
    
    <form name="form1" method="post" action="edit.php">
        <table border="0">
            <tr> 
                <td>Productnaam</td>
                <td><?php echo $productnaam;?></td>
            </tr>
            <tr> 
                <td>Prijs</td>
                <td><?php echo $prijs;?></td>
            </tr>
            <tr> 
                <td>Aantal</td>
                <td><input type="text" name="voorraadaantal" value="<?php echo $voorraadaantal;?>"></td>
            </tr>
            <tr>
                <td><input type="hidden" name="id" value=<?php echo $_GET['id'];?>></td>
                <td><input type="submit" name="update" value="Update"></td>
            </tr>
        </table>
    </form>
</body>
</html>
