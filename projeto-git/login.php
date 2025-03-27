<?php
session_start();

// Simulando um banco de dados (troque isso por conexão com MySQL, se necessário)
$usuarios = [
    "usuario@email.com" => "senha123",
    "admin@email.com" => "admin123"
];

// Verifica se os campos foram preenchidos
if (!isset($_POST['email'], $_POST['senha'])) {
    die("Preencha todos os campos!");
}

$email = trim($_POST['email']);
$senha = trim($_POST['senha']);

if (isset($usuarios[$email]) && $usuarios[$email] === $senha) {
    // Criando sessão para o usuário autenticado
    $_SESSION['usuario'] = $email;
    
    // Redirecionamento correto
    header("Location: dashboard.html");
    exit(); // Garante que o script para de rodar após o redirecionamento
} else {
    echo "<script>alert('E-mail ou senha incorretos!'); window.location.href='index.html';</script>";
    exit();
}
?>
