<?php
fscanf(STDIN,"%d %d %d", $n ,$a, $b);
$ans = 0;
for($i=0; $i<=$n; $i++){
    $array = str_split($i);
    $sum = 0;
    foreach($array as $value) {
        $sum += $value;
    }
    if($sum >= $a and $sum <= $b){
        $ans += $i;
    }

}

echo $ans;