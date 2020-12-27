<?php

// initializing variables
$matricula = $_POST['matricula'];
$nome= $_POST['nome'];
$sexo= $_POST['sexo'];
$site= $_POST['site'];
$observacoes= $_POST['observacoes'];

if (!empty($matricula) || !empty($nome) || !empty($sexo) || !empty($site) || !empty($observacoes)) {
    $host = "localhost";
    $dbUsername = "root";
    $dbPassword = "";
    $dbname = "registro";

    //create connection
    $conn = new mysqli($host, $dbUsername, $dbPassword, $dbname);

    if (mysqli_connect_error()) {
     die('Connect Error('. mysqli_connect_errno().')'. mysqli_connect_error());
    } else {
        $INSERT = "INSERT Into matricula (id, matricula, nome, sexo, site, observacoes) values(?, ?, ?, ?, ?, ?)";
        $stmt = $conn->prepare($INSERT);
        $stmt->bind_param("iissss", $id, $matricula, $nome, $sexo, $site, $observacoes);
        $stmt->execute();
        echo "New record inserted sucessfully";
     }
     $stmt->close();
     $conn->close();
} else {
 echo "All field are required";
 die();
}
?>