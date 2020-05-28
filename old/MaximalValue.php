<?php
fscanf(STDIN, "%d", $n);
$b = explode(" ",fgets(STDIN));
$a = array();
$b = array_map("intval", $b);

$a[0] = $b[0];

for($i=0; $i<$n-2; $i++) {
    if($b[$i]<$b[$i+1]) {
        $a[$i+1] = $b[$i];
    } else {
        $a[$i+1] = $b[$i+1];
    }
}

$a[$n-1] = $b[$n-2];

$maxA = array_sum($a);

echo $maxA;