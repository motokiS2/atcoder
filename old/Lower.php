<?php
fscanf(STDIN, "%d", $n);
$h = explode(" ",fgets(STDIN));
$h = array_map("intval", $h);
$move = 0;
$moveMax = 0;

for($i=0; $i<$n-1; $i++) {
    if($h[$i] >= $h[$i+1]) {
        $move++;
    } else {
        $moveMax = max($move, $moveMax);
        $move = 0;
    }
}
echo max($move, $moveMax);