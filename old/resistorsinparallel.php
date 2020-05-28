<?php
fscanf(STDIN, "%d", $n);
$a = explode(" ",fgets(STDIN));

$ans = 0;

for($i=0; $i<$n; $i++) {
    $a[$i] = 1/$a[$i];
    $ans += $a[$i];
}

$ans = 1/$ans;

echo $ans;