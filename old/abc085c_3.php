<?php
fscanf(STDIN, "%d %d", $num, $sum);
$yukichi    = 0;
$ichiyo     = 0;
$hideyo     = 0;
$total      = 0;
for ($i=0; $i<=$num; $i++){
    for ($j=0; $j<=$num-$i; $j++){
        $k = $num - $j - $i;
        $total = $i*10000 + $j*5000 + $k*1000;
        if ($total == $sum) {
            $yukichi    = $i;
            $ichiyo     = $j;
            $hideyo     = $k;
            break 2;
        }
    }
}
if ($yukichi == 0 and $ichiyo == 0 and $hideyo == 0) {
    echo "-1 -1 -1";
} else {
    echo $yukichi." ".$ichiyo." ".$hideyo;
}