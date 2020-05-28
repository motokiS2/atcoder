<?php
fscanf(STDIN, "%d", $n);
$l = array_map('intval', explode(' ', trim(fgets(STDIN))));

sort($l); // 棒の長さを短い順にソート

$count = 0;

for($i = 0; $i < $n-2; $i++) {
    for($j = $i+1; $j < $n-1; $j++) {
        $startNumber = $j + 1; // 調査する左端を初期化
        $endNumber = $n - 1; // 調査する右端を初期化
        $goalNumber = floor(($j + $n) / 2); // 調べる初期値

        if(($l[$i] + $l[$j] - $l[$goalNumber]) > 0 && ($l[$i] + $l[$j] - $l[$goalNumber + 1]) <= 0) {
            $count += $goalNumber - $j;
            break;
        }
    }
}
echo $count;