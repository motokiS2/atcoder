<?php
fscanf(STDIN, "%d %d", $num, $sum);
$total = 0;

for ($i=0; $i<=$num; $i++){
    if($i*10000 == $sum){
        $yukichi = $i;
        echo $yukichi." 0 0";
        break;
    } elseif ($i*10000 > $sum) {
        $yukichi = $i-1;
        break;
    }
}
$yukichiYen = $yukichi * 10000;
for ($j=0; $j<=$num-$yukichi; $j++){
    if($yukichiYen+$j*5000 == $sum) {
        $ichiyo = $j;
        echo $yukichi." ".$ichiyo." 0";
        break;
    } elseif($yukichiYen+$j*5000 > $sum){
        $ichiyo = $j-1;
        break;
    }
}
$ichiyoYen = $ichiyo * 5000;
for ($k=0; $k<=$num-$yukichi-$ichiyo; $k++) {
    if($yukichiYen+$ichiyoYen+$k*1000 == $sum) {
        $hideyo = $k;
        echo $yukichi." ".$ichiyo." ".$hideyo;
        break;
    }
}
