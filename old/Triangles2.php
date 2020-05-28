<?php
fscanf(STDIN, "%d", $n);
$l = array_map('intval', explode(' ', trim(fgets(STDIN))));

sort($l); // 棒の長さを短い順にソート

$count = 0;

function checkTriangle($a, $b, $c) { // $a < $b < $cの制約付き
    if($a + $b - $c > 0) {
        return true;
    } else {
        return false;
    }
}

for($i = 0; $i < $n-2; $i++) {
    for($j = $i+1; $j < $n-1; $j++) {
        $startNumber = $j + 1; // 調査する左端を初期化
        $endNumber = $n - 1; // 調査する右端を初期化
        $goalNumber = floor(($j + $n) / 2); // 調べる初期値
        reCheck:
        if(checkTriangle($l[$i], $l[$j], $l[$goalNumber]) && !checkTriangle($l[$i], $l[$j], $l[$goalNumber + 1])) {
            $count += $goalNumber - $j;
            break;
        } else if (checkTriangle($l[$i], $l[$j], $l[$goalNumber]) && checkTriangle($l[$i], $l[$j], $l[$goalNumber + 1])) {
            $startNumber = $goalNumber;
            $goalNumber = ceil(($goalNumber + $endNumber) / 2);
            goto reCheck;
        } else if(!checkTriangle($l[$i], $l[$j], $l[$goalNumber]) && !checkTriangle($l[$i], $l[$j], $l[$goalNumber + 1])) {
            $endNumber = $goalNumber;
            $goalNumber = floor(($startNumber + $goalNumber) / 2);
            goto reCheck;
        }
    }
}
echo $count;