<?php
$n = trim(fgets(STDIN));
fscanf(STDIN, "%s %s", $s, $t);
$ans = "";
for($i = 0; $i < $n; $i++) {
    $ans = $ans . $s[$i] . $t[$i];
}
echo $ans;