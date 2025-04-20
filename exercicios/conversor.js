<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Conversor Decimal Binário</title>
    <script>
        function converter(){
            //Pegar o valor do input
            let decimal = document.getElementById("decimalInput").value;
            //Converter o valor para binário
            let binario = parseInt(decimal, 10).toString(2);
            //Mostrar o resultado
            document.getElementById("resultado").innerHTML = "O número " + decimal + " em binário é " + binario;
        }
    </script>
</head>
<body>
    <h1>Conversor Decimal Binário</h1>
    <hr>
    <br>
    <p>Digite um número em Decimal</p>
    <!--Caixa de entrada de  número decimal-->
    <input type ="number" id="decimalInput" placeholder="Digite um número em Decimal">
    <button onclick="converter()">converter</button>
    <p id="resultado"></p>
    <!--Caixa de resultado-->
</body>
</html>