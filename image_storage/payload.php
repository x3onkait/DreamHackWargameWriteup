<?php
  $fp = fopen("/flag.txt", "r") or die("파일을 열 수 없습니다！");

  while( !feof($fp) ) {
    echo fgets($fp);
  }

  fclose($fp);
?>
