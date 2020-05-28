<?php
fscanf(STDIN, "%d %d %d", $a, $b, $x);

function checkValue($a, $b, $n, $x) {
    return $a * $n + $b * strlen($n) <= $x; //買えたらtrueを返す
}

if($a * 1000000000 + $b * 10 <= $x) {
    $ans = 1000000000;
    echo $ans;
    return;
}

if($a + $b > $x) {
    echo 0;
    return;
}

$max = ceil($x / $a);
$min = 0;
$n = $max / 2;
$fin = 0;
while($fin === 0){
    if(checkValue($a, $b, $n, $x)) {
        $min = $n;
        $n = ceil(($max + $min) / 2);
        if($n === $max) {
            $fin = 1;
            $ans = $n - 1;
        }
    } else {
        $max = $n;
        $n = floor(($max + $min) / 2);
        if($n === $min) {
            $fin = 1;
            $ans = $n;
        }
    }
}

echo $ans;
