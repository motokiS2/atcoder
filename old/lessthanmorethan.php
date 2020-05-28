<?php
fscanf(STDIN, "%s", $s);
$n = strlen($s);
$a = array_fill(0, $n+1, 0);
for($i = 0; $i < $n; $i++) {
    if($s[$i] === "<") {
        $a[$i+1] = max($a[$i+1], $a[$i]+1);
    }
}

for($i = $n-1; $i >= 0; $i--) {
    if($s[$i] === ">") {
        $a[$i] = max($a[$i], $a[$i+1]+1);
    }
}

$ans = array_sum($a);
echo $ans;