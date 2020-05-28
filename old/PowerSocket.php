<?php
fscanf(STDIN, "%d %d", $a, $b);
$n = 0;
while( $n*($a-1)+1 < $b){
    $n++;
}

echo $n;