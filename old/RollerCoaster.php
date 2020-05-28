<?php
fscanf(STDIN, "%d %d", $n, $k);
$h = explode(" ",fgets(STDIN));
$ans = 0;
for($i=0; $i<$n; $i++) {
    if($h[$i] >= $k) {
        $ans++;
    }
}
echo $ans;