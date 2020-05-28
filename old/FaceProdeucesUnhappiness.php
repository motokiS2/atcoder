<?php
fscanf(STDIN, "%d %d", $n, $k);
$s = trim(fgets(STDIN));
$arrayS = str_split($s);
$h = 0;
for($i=0; $i<$n-1; $i++) {
    if($arrayS[$i] == $arrayS[$i+1]) {
        $h++;
    }
}
$h = $h + 2*$k;
echo min($h,$n-1);
