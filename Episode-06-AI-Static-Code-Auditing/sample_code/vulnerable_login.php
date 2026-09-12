<?php
// Vulnerable Authentication Handler (SQL Injection)
$conn = mysqli_connect("localhost", "db_user", "db_pass", "company_db");

$user = $_POST['username'];
$pass = $_POST['password'];

// Unsanitized dynamic query concatenation
$query = "SELECT * FROM users WHERE username = '$user' AND password = '$pass'";
$result = mysqli_query($conn, $query);

if (mysqli_num_rows($result) > 0) {
    echo "Login successful! Welcome admin.";
} else {
    echo "Invalid credentials.";
}
?>
