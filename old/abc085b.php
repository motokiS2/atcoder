<?php
$n = intval(trim(fgets(STDIN)));
$a = array();
for($i=0; $i<$n; $i++){
    $a[$i] = intval(trim(fgets(STDIN)));
}
echo count(array_unique($a));