<?php
fscanf(STDIN, "%d %d %d", $n, $k, $q);
$p = array_fill(0,$n,$k-$q);
for($i=0; $i<$q; $i++) {
    fscanf(STDIN, "%d", $a);
    $p[$a-1] += 1;
}
for($i=0; $i<$n; $i++) {
    if($p[$i] > 0){
        echo "Yes"."\n";
    } else {
        echo "No"."\n";
    }
}