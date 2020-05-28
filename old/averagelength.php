<?php
fscanf(STDIN, "%d", $n);
for($i = 0; $i < $n; $i++) {
    fscanf(STDIN, "%d %d", $x[], $y[]);
}

$route = 1;
for($i = 1; $i <= $n; $i++) {
    $route = $route * $i; // 全部の街を通るルートは何通りあるか
}
$pair = 1;
for($i = 1; $i <= $n-1; $i++) {
    $pair = $pair * $i; // ある街からある街への移動は何通りあるか 1-2,2-1は同じでカウント
}
$move = $route * ($n-1) / $pair; // A街からB街への移動は何回するか
$totalLength = 0;
for($i = 0; $i < $n-1; $i++) {
    for($j = $i+1; $j < $n; $j++) {
        $totalLength += $pairLength = sqrt(pow($x[$i] - $x[$j], 2) + (pow($y[$i] - $y[$j], 2)));
    }
}
$totalLength = $totalLength * $move;
$averageLength = $totalLength / $route;
echo $averageLength;

var_dump($route);
?>