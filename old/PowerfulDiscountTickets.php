<?php
fscanf(STDIN, "%d %d", $n, $m);
$a = explode(" ",fgets(STDIN));
for($i=0; $i<$m; $i++) {
    $expensive = array_search(max($a), $a);
    $a[$expensive] = floor($a[$expensive]/2);
}
echo array_sum($a);
