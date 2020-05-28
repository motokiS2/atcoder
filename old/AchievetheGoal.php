<?php

fscanf(STDIN, "%d %d %d", $n, $k, $m);
$a = array_map('intval', explode(' ', trim(fgets(STDIN))));

$sumA = 0;
foreach($a as $value) {
    $sumA+=$value;
}
$x = $m * $n - $sumA;
if($x > $k) {
    echo -1;
} else {
    echo max(0, $x);
}