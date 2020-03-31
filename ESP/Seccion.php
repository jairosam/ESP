<?php

$conecta = mysqli_connect("localhost", "root", "passtoor", "ESP") or die ("Error con la conexion");
$sql = "SELECT nivelhumo FROM Datos ORDER BY id DESC";
$result = mysqli_query($conecta, $sql);
$impresion = mysqli_fetch_row($result);
echo $impresion[0] . " PPM";
if($impresion[0]>95){
    echo "<script type='text/javascript'>alert('Alerta de Incendio')</script>";
}
?>
