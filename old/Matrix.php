<?php
fscanf(STDIN, "%d %d %d %d", $h, $w, $a, $b);
$matrix = array();
for($i=0; $i<$b; $i++) {
    $matrix0[$i] = array_fill(0, $w, 0);
    $matrix1[$i] = array_fill($a, $w-$a, 1);
    $matrix[$i]  = array_replace($matrix0[$i],$matrix1[$i]);
}
for($i=$b; $i<$h; $i++) {
    $matrix0[$i] = array_fill(0, $w, 1);
    $matrix1[$i] = array_fill($a, $w-$a, 0);
    $matrix[$i]  = array_replace($matrix0[$i],$matrix1[$i]);
}
for($i=0; $i<$h; $i++) {
    for($j=0; $j<$w; $j++) {
        echo $matrix[$i][$j];
    }
    echo PHP_EOL;
}
?>