<?php
fscanf(STDIN, "%d %d", $num, $sum);
$totalYukichi = 0;
$totalIchiyo = 0;
$totalHideyo = 0;
$total = 0;
for ($k=0; $k<=$num; $k++){
    $totalYukichi = 10000 * $k;
    $total = $totalYukichi;
    for ($j=0; $j<=$num-$k; $j++){
        $totalIchiyo = 5000 * $j;
        $total = $totalYukichi + $totalIchiyo;
        for ($i=0; $i<=$num-($j+$k); $i++) {
            $totalHideyo = 1000 * $i;
            $total = $totalYukichi + $totalIchiyo + $totalHideyo;
            if ($total == $sum) {
                echo $k." ".$j." ".$i;
                break 3;
            }
        }
    }
}
if ($k = $num and $total != $sum) {
    echo "-1 -1 -1";
}