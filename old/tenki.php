<?php
$s = fgets(STDIN);
$t = fgets(STDIN);
$s_sp = str_split($s);
$t_sp = str_split($t);
$ans = 0;
for($i=0; $i<3; $i++) {
    if ($s_sp[$i] == $t_sp[$i]) {
        $ans++;
    }
}

echo $ans;