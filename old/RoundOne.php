<?php
$a = intval(trim(fgets(STDIN)));
$b = intval(trim(fgets(STDIN)));
if($a + $b === 3) {
    $c = 3;
} elseif($a + $b === 4) {
    $c = 2;
} elseif($a + $b === 5) {
    $c = 1;
}
echo $c;

// 別解
// $c = 6 - $a - $b;