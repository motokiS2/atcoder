<?php
fscanf(STDIN, "%d", $n);
$d = explode(" ", trim(fgets(STDIN)));
$ans = 0;
for($i = 0; $i < $n; $i++) {
    for($j = $i+1; $j < $n; $j++) {
        $ans += $d[$i] * $d[$j];
    }
}

echo $ans;

// var_dump($d);
