<?php
$c = trim(fgets(STDIN));

$tmp = ord($c) + 1;
$ans = chr($tmp);

echo $ans;