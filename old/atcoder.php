<?php
fscanf(STDIN, "%d %d", $n, $m);
$s = array_fill(1,$m,NULL);
for($i=0; $i<$n; $i++){
    fscanf(STDIN, "%d %d", $a, $b);
    $s[$a][] = $b;
}
$avail = [];
$list = [];
$ans = 0;
$max = 0;
for($i=1; $i<=$m; $i++){
    foreach($s[$i] as $value){

    }
}