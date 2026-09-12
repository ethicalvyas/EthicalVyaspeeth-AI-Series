<?php
// Vulnerable Comment System (Reflected / Stored XSS)
if (isset($_GET['comment'])) {
    $user_comment = $_GET['comment'];
    
    // Direct output without HTML entity escaping
    echo "<h3>User Comment:</h3>";
    echo "<div>" . $user_comment . "</div>";
}
?>
