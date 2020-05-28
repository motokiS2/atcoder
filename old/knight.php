<?php
fscanf(STDIN, "%d %d", $x, $y);

$m = (2*$x - $y)/3;
$n = (2*$y - $x)/3;

$o = $m + $n;
$meth = 1;
for($i = $n; $i <= $o; $i++) {
    $meth *= $i;
}
$ans = $meth % (10**9+7);
if(($x+$y) % 3 === 0) {
    echo $ans;
} else {
    echo 0;
}

var_dump(($x+$y) % 3);