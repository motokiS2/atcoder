<?php
fscanf(STDIN, "%d", $n);
$l = array_map('intval', explode(' ', trim(fgets(STDIN))));

sort($l); // 棒の長さを短い順にソート

if($n <= 3) {
    echo 0;
    exit;
}

$count = 0;

function checkTriangle($a, $b, $c) { // $a < $b < $cの制約付き
    if($a + $b -$c > 0) {
        return true;
    } else {
        return false;
    }
}

if(checkTriangle($l[0], $l[1], $l[3])) {
    echo "aaa";
    jump:
    echo "bbb";
} else {
    goto jump;
}