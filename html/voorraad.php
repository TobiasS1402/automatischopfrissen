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
<html>
<head>    
    <title>Edit Data</title>
</head>
 
<body>
    <a href="index.php">Home</a>
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
