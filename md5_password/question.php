<?php

  // ... 

  $row = @mysqli_fetch_array(mysqli_query($conn, "select * from admin_password where password='".md5($ps,true)."'"));

?>
