<?php
fscanf(STDIN, "%d", $n);
$a = explode(" ",fgets(STDIN));
$b = explode(" ",fgets(STDIN));
$c = explode(" ",fgets(STDIN));

$a = array_map("intval", $a);
$b = array_map("intval", $b);
$c = array_map("intval", $c);

$bs = array_sum($b);
$cs = 0;
$s = 0;

for ($i=0; $i<$n-1; $i++) {
    if($a[$i]+1 === $a[$i+1]) {
        $cs += $c[$a[$i]-1];
    }
}

$s = $bs + $cs;
echo $s;