<?php
fscanf(STDIN, "%d %d %d", $n, $a, $b);
$ans = 0;
for ($i = 1; $i <= $n; $i++) {
    $sum = 0;
    $j = $i;
    while($i > 0.1) {
        $sum += $i % 10;
        $i = floor($i/10);
        var_dump($i);
    }
    if($sum >= $a && $sum <= $b) {
        $ans += $j;
    }
}
echo $ans;
