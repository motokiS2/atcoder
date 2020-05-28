<?php
$coin500 = intval(trim(fgets(STDIN)));
$coin100 = intval(trim(fgets(STDIN)));
$coin50 = intval(trim(fgets(STDIN)));
$goal = intval(trim(fgets(STDIN)));
$pattern = 0;
$total500 = 0;
$total100 = 0;
$total50 = 0;
$total = 0;
for ($k=0; $k<=$coin500; $k++){
    $total500 = 500 * $k;
    $total = $total500;
    for ($j=0; $j<=$coin100; $j++){
        $total100 = 100 * $j;
        $total = $total500 + $total100;
        for ($i=0; $i<=$coin50; $i++) {
            $total50 = 50*$i;
            $total = $total500 + $total100 + $total50;
            if ($total == $goal) {
                $pattern++;
                break 1;
            }
        }
    }
}
echo $pattern;